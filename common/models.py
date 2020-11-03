from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, Float, sql, String
from sqlalchemy.dialects.postgresql import UUID


db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'products'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, server_default=sql.func.gen_random_uuid())
    name = Column(String(200), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    creation_time = Column(DateTime, nullable=False, server_default=sql.func.now())

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'creation_time': self.creation_time
        }

    def __repr__(self):
        return '<Product(id={}, name={}, price={}, creation_time={})>'.format(self.id, self.name, self.price, self.creation_time)

    @classmethod
    def get_all(cls) -> dict:
        return db.session.query(cls).all()

    @classmethod
    def get_by_id(cls, product_id: str) -> dict:
        return db.session.query(cls).filter(cls.id == product_id).one()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, server_default=sql.func.gen_random_uuid())
    name = Column(String(200), unique=True, nullable=False)
    creation_time = Column(DateTime, nullable=False, server_default=sql.func.now())

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'creation_time': self.creation_time
        }

    def __repr__(self):
        return '<User(id={}, name={}, creation_time={})>'.format(self.id, self.name, self.creation_time)

    @classmethod
    def get_all(cls) -> dict:
        return db.session.query(cls).all()

    @classmethod
    def get_by_id(cls, user_id: str) -> dict:
        return db.session.query(cls).filter(cls.id == user_id).one()
