# Real-time-data-pipeline-
run kafka
cd $KAFKA
bin/zookeeper-server-start.sh config/zookeeper.properties 
bin/kafka-server-start.sh config/server.properties
tạo topic RawSensorData
bin/kafka-topics.sh --create --topic RawSensorData --bootstrap-server localhost:9092

Chạy file tạo dữ liệu cho sensor 
python3 sensor.py 

Đẩy dữ liệu vào kafka
python3 push_data_to_kafka.py 

Lưu dữ liệu vào  cassandra
mở cassandra lên tạo test_keyspace
python3 push_data_to_cassandara.py 

Xem dữ liệu ở  Kafka Consumer
 
 
![alt text](https://ibb.co/QnD735d)
