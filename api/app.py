import connexion
import os

from flask_migrate import Migrate

from models import db

app = connexion.FlaskApp(__name__)
app.add_api('v1.yaml')

flask_app = app.app
flask_app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
flask_app.config['SQLALCHEMY_ECHO'] = True
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
    os.environ.get('POSTGRES_USER'),
    os.environ.get('POSTGRES_PASSWORD'),
    os.environ.get('POSTGRES_HOST'),
    os.environ.get('POSTGRES_DATABASE_NAME')
)
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(flask_app)
migrate = Migrate(flask_app, db)
