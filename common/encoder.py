import datetime

from json import JSONEncoder
from uuid import UUID


class Encoder(JSONEncoder):
    def default(self, o):
        if hasattr(o, 'to_dict'):
            return o.to_dict()

        if isinstance(o, datetime.datetime):
            return str(o)

        if isinstance(o, UUID):
            return str(o)

        return JSONEncoder.default(self, o)
