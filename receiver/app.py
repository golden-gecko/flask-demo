import connexion

app = connexion.FlaskApp(__name__)
app.add_api('v1.yaml')
