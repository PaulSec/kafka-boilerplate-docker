from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='0.0.0.0:9092')
producer.send('test', b'Hello, World!')
producer.send('test', key=b'message-two', value=b'This is Kafka-Python')
producer.flush()
print('We are done sending messages.')