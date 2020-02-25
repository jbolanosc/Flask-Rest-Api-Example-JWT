from flask_bcrypt import Bcrypt
from database.db import initialize_db
import json
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.errors import errors



app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
mail = Mail(app)

from flask import Flask
from flask_mail import Mail
from resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)

initialize_routes(api)

