import uuid


def is_uuid(value):
    try:
        uuid.UUID(str(value))
    except ValueError:
        return False
    else:
        return True
