from flask import Flask

from api.routes import api
from api.routes import setup_api_routes

def create_app():
	app = Flask(__name__)

	app.register_blueprint(api)

	setup_api_routes(app)
 
	return app



