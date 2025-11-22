import datetime


def get_time() -> str:
    return str(datetime.datetime.utcnow())
