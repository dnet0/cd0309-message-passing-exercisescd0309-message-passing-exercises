import json
from .app import g
from .enums import Status


def create_order(order_data):
    """
    This is a stubbed method of retrieving a resource. It doesn't actually do anything.
    """
    # Turn order_data into a binary string for Kafka
    # kafka_data = json.dumps(order_data).encode()
    # Kafka producer has already been set up in Flask context
    # kafka_producer = g.kafka_producer
    # TODO: send the data using kafka_producer using .send()
    kafka_data = json.dumps(order_data).encode()
    kafka_producer = g.kafka_producer
    kafka_producer.send("computers", kafka_data)


def retrieve_orders():
    """
    This is a stubbed method of retrieving multiple resources. It doesn't actually do anything.
    """
    kafka_consumer = g.kafka_consumer
    orders = []
    print(kafka_consumer)
    for msg in kafka_consumer:
        print(msg)
        orders.append(json.loads(msg.value))

    return orders
