import json
import pika

from flask import request

from handlers import ok


def create() -> tuple:
    with pika.BlockingConnection(pika.ConnectionParameters('192.168.10.18')) as connection:
        channel = connection.channel()
        channel.queue_declare(queue='readings')
        channel.basic_publish(exchange='', routing_key='readings', body=json.dumps(request.json))

    return ok()
