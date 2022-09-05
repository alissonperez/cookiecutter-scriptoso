import os
from contextlib import contextmanager

from kafka import KafkaConsumer, KafkaProducer


def consume(topic):
    '''
    Just:

        for msg in consume('my.topic.name'):
            pprint.pprint(msg)
    '''

    # To consume latest messages and auto-commit offsets
    consumer = KafkaConsumer(topic,
                             client_id=os.environ['KAFKA_CLIENT_ID'],
                             bootstrap_servers=os.environ['KAFKA_BOOTSTRAP_SERVERS'].split(','),
                             # AUTH
                             sasl_mechanism=os.environ['KAFKA_SASL_MECHANISM'],
                             security_protocol=os.environ['KAFKA_SECURITY_PROTOCOL'],
                             sasl_plain_password=os.environ['KAFKA_SASL_PLAIN_PASSWORD'],
                             sasl_plain_username=os.environ['KAFKA_SASL_PLAIN_USERNAME'])

    for message in consumer:
        yield {
            'topic': message.topic,
            'partition': message.partition,
            'offset': message.offset,
            'key': message.key.decode(),
            'value': message.value.decode(),
        }


def _on_send_success(record_metadata):
    print(f'Success record set to topic {record_metadata.topic}, ',
          f'partition {record_metadata.partition} with offset {record_metadata.offset}')


def _on_send_error(excp):
    print('Error sending msg to kafka:', excp)


@contextmanager
def createProducer():
    '''
    Just:

        with createProducer() as produce:
            produce('my-topic', 'my-key', 'my-value')
    '''

    producer = KafkaProducer(client_id=os.environ['KAFKA_CLIENT_ID'],
                             bootstrap_servers=os.environ['KAFKA_BOOTSTRAP_SERVERS'].split(','),
                             # AUTH
                             sasl_mechanism=os.environ['KAFKA_SASL_MECHANISM'],
                             security_protocol=os.environ['KAFKA_SECURITY_PROTOCOL'],
                             sasl_plain_password=os.environ['KAFKA_SASL_PLAIN_PASSWORD'],
                             sasl_plain_username=os.environ['KAFKA_SASL_PLAIN_USERNAME'])

    def _produce(topic, key, value):
        producer.send(topic,
                      key=key.encode(),
                      value=value.encode()).add_callback(_on_send_success).add_errback(_on_send_error)

    try:
        yield _produce
    finally:
        producer.flush()
