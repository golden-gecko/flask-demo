import json

from influxdb import InfluxDBClient

from log import get_logger
from rabbitqueue import RabbitQueue


client = InfluxDBClient(host='192.168.10.21', port=8086)
logger = get_logger()
queue = RabbitQueue('192.168.10.18', 5672)


def process_readings(channel, method_frame, header_frame, body):
    readings = json.loads(body.decode('utf-8'))

    logger.debug('Received message %s from %s', readings, channel)

    for reading in readings:
        client.write_points(
            [
                {
                    'measurement': reading['name'],
                    'time': reading['timestamp'],
                    'fields': {
                        'value': reading['value']
                    }
                }
            ]
        )

    queue.ack(method_frame.delivery_tag)


def main():
    logger.info('Starting...')

    try:
        client.create_database('readings')
        client.switch_database('readings')

        queue.connect()
        queue.add_callback('readings', process_readings)
        queue.start_consuming()
    except KeyboardInterrupt as e:
        logger.warning('Processing stopped: %s', e)
    except Exception as e:
        logger.exception('Processing failed: %s', e)

    logger.info('Exiting...')


if __name__ == '__main__':
    main()
