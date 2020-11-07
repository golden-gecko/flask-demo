import pika

from log import get_logger


class RabbitQueue:
    def __init__(self, host: str, port: int):
        self.logger = get_logger()

        self.connection_parameters = pika.ConnectionParameters(host=host, port=port)
        self.basic_properties = pika.BasicProperties(delivery_mode=2)

        self.connection = None
        self.channel = None

    def connect(self, prefetch_count=10):
        self.logger.info('Connecting to RabbitMQ...')

        self.connection = pika.BlockingConnection(parameters=self.connection_parameters)

        self.channel = self.connection.channel()
        self.channel.basic_qos(prefetch_count=prefetch_count)

    def disconnect(self):
        self.logger.info('Disconnecting from RabbitMQ...')

        if self.connection:
            self.connection.close()

    def declare(self, queue):
        self.channel.queue_declare(queue=queue, durable=True)
        self.channel.queue_declare(queue='{}_failed'.format(queue), durable=True)

    def add_callback(self, queue, callback):
        self.channel.basic_consume(queue=queue, on_message_callback=callback)

    def publish(self, queue, value):
        self.channel.queue_declare(queue=queue, durable=True)
        self.channel.basic_publish(exchange='', routing_key=queue, body=value, properties=self.basic_properties)

    def ack(self, delivery_tag):
        self.channel.basic_ack(delivery_tag=delivery_tag)

    def nack(self, delivery_tag):
        self.channel.basic_nack(delivery_tag=delivery_tag)

    def start_consuming(self):
        self.channel.start_consuming()
