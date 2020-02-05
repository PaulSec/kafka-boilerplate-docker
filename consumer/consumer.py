from kafka import KafkaConsumer
consumer = KafkaConsumer('test', auto_offset_reset='earliest', enable_auto_commit=True, group_id='booya', bootstrap_servers='0.0.0.0:9092')
# print(consumer)
for message in consumer:
    print (message)