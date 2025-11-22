import connexion
import os

from models import db


def create_app(specification_dir: str) -> tuple:
    connexion_app = connexion.App(__name__, specification_dir=specification_dir)

    app = connexion_app.app
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ.get('POSTGRES_USER'), os.environ.get('POSTGRES_PASSWORD'),
        os.environ.get('POSTGRES_HOST'), os.environ.get('POSTGRES_DATABASE_NAME')
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    return connexion_app, app


connexion_app, app = create_app(specification_dir=os.path.abspath(os.path.dirname(__file__)))
connexion_app.add_api('v1.yaml', validate_responses=True)

db.init_app(app)
