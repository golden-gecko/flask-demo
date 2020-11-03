from flask import request

from handlers import bad_request, ok
from log import get_logger
from models import db, User
from messages import Message
from validators import is_uuid


logger = get_logger()


def get_all() -> tuple:
    return ok(data=User.get_all())


def create() -> tuple:
    data = request.json

    user = User(
        name=data.get('name')
    )

    db.session.add(user)
    db.session.commit()

    logger.debug('User created')

    return ok(data=User.get_by_id(user.id))


def delete(user_id: str) -> tuple:
    db.session.query(User).filter(User.id == user_id).delete()
    db.session.commit()

    return ok()


def get(user_id: str) -> tuple:
    if not is_uuid(user_id):
        return bad_request(message=Message.Invalid_User_Id)

    return ok(data=User.get_by_id(user_id))
