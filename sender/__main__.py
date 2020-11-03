import datetime
import random
import requests
import time

from log import get_logger


def get_random_name():
    names = ['Temperature', 'Load', 'Size']

    return random.choice(names)


def get_random_value():
    return random.randint(1, 9)


def main():
    logger = get_logger()
    logger.info('Starting...')

    try:
        while True:
            body = []

            for _ in range(random.randint(1, 9)):
                body.append({
                    'name': get_random_name(),
                    'value': get_random_value(),
                    'timestamp': str(datetime.datetime.utcnow())
                })

            requests.post('http://192.168.10.22:7000/v1/readings', json=body)

            time.sleep(1)
    except KeyboardInterrupt as e:
        logger.warning('Processing stopped: %s', e)
    except Exception as e:
        logger.exception('Processing failed: %s', e)

    logger.info('Exiting...')


if __name__ == '__main__':
    main()
