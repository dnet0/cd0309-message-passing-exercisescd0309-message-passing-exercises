from kafka import KafkaConsumer


TOPIC_NAME = 'orders'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)
