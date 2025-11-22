from flask import request

from handlers import bad_request, ok
from log import get_logger
from models import db, Product
from messages import Message
from validators import is_uuid


logger = get_logger()


def get_all() -> tuple:
    return ok(data=Product.get_all())


def create() -> tuple:
    data = request.json

    product = Product(
        name=data.get('name'),
        price=data.get('price')
    )

    db.session.add(product)
    db.session.commit()

    logger.debug('Product created')

    return ok(data=Product.get_by_id(product.id))


def delete(product_id: str) -> tuple:
    db.session.query(Product).filter(Product.id == product_id).delete()
    db.session.commit()

    return ok()


def get(product_id: str) -> tuple:
    if not is_uuid(product_id):
        return bad_request(message=Message.Invalid_Product_Id)

    return ok(data=Product.get_by_id(product_id))
