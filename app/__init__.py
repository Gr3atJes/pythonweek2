from flask import flask
from config import config_options

def create_app(config_name):
    # Creating instance
    app = Flask(__name__)

    # Creating the app conifgurations
    app.config.from_object(config_options[config_name])

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Setting config
    from .requests import configure_requests
    configure_requests(app)

    return app