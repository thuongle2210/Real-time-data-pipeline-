from kafka import KafkaConsumer
from cassandra.cluster import Cluster

clstr=Cluster()
session=clstr.connect('test_keyspace')
qry= '''
create table sensordata (
   timestampid timestamp,
   water_temperature float,
   turbidity float,
   battery_life float,
   beach text,
   measurement_id int,
   primary key(beach, timestampid)
)WITH CLUSTERING ORDER BY (timestampid DESC);'''
session.execute(qry)
consumer = KafkaConsumer('CleanSensorData', auto_offset_reset='earliest',bootstrap_servers=['localhost:9092'], consumer_timeout_ms=1000)
print(consumer)
i=0
while True:
    for msg in consumer:
        #print(msg)
        list_msg = msg.value.decode("utf-8").split(' ')
        print(list_msg)
        if len(list_msg)!=6:
            break   
        qry = """
        INSERT INTO sensordata (timestampid , water_temperature, turbidity, battery_life, beach, measurement_id) 
        VALUES
        """ + str((list_msg[0], float(list_msg[1]), float(list_msg[2]), float(list_msg[3]), list_msg[4], int(list_msg[5])))
        session.execute(qry)
