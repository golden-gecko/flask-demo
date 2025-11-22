import connexion
import os


def create_app(specification_dir: str) -> tuple:
    connexion_app = connexion.App(__name__, specification_dir=specification_dir)

    app = connexion_app.app
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

    return connexion_app, app


connexion_app, app = create_app(specification_dir=os.path.abspath(os.path.dirname(__file__)))
connexion_app.add_api('v1.yaml', validate_responses=True)
