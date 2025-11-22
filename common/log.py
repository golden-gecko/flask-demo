import logging
import os

from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.handler import LogstashFormatter


logger = None


def get_logger() -> logging.Logger:
    global logger

    if not logger:
        logstash_formatter = LogstashFormatter(
            message_type='python-logstash',
            tags={
                'application_name': os.getenv('LOG_APPLICATION_NAME')
            }
        )

        logstash_handler = AsynchronousLogstashHandler(
            host=os.getenv('LOGSTASH_HOST'),
            port=int(os.getenv('LOGSTASH_PORT')),
            database_path='',
            ssl_enable=False,
            ssl_verify=False
        )
        logstash_handler.setFormatter(logstash_formatter)

        stream_formatter = logging.Formatter('[%(asctime)s] [%(filename)s] [%(lineno)d] [%(levelname)s] %(message)s')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(stream_formatter)

        logger = logging.getLogger()
        logger.setLevel(os.environ.get('LOG_LEVEL', 'DEBUG'))
        logger.addHandler(stream_handler)
        logger.addHandler(logstash_handler)

    return logger
