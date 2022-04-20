from kafka import KafkaConsumer, KafkaProducer


consumer = KafkaConsumer('RawSensorData', auto_offset_reset='earliest',bootstrap_servers=['localhost:9092'])
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for msg in consumer:
    #water_temperature = list(msg.value.decode("utf-8").split(" "))[1]
    print(msg)
    producer.send('CleanSensorData', msg.value)
    