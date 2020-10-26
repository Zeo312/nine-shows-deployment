from flask import Flask, Blueprint, request
from flask import jsonify
from werkzeug.exceptions import HTTPException, BadRequest
import json


api = Blueprint('api', __name__)

def setup_api_routes(api):

	@api.route('/processjson', methods=['POST'])
	def processjson():
	    data = request.get_json(force=True)

	    if "payload" not in data:
	    	response_msg = {"error": "Could not decode request: JSON parsing failed"}
	    	return jsonify(response_msg), 400

	    response_shows = []
	    response = {}

	    for show in data["payload"]:
	        if("drm" in show and "episodeCount" in show and "image" in show and
	                "slug" in show and "title" in show and show["drm"] is True and 
	                show["episodeCount"] > 0):
	            if "showImage" in show["image"]:
	                image = show["image"]["showImage"]
	            else:
	                image = ""
	            slug = show["slug"]
	            title = show["title"]
	            filtered_show = {"image": image, "slug": slug, "title": title}
	            response_shows.append(filtered_show)

	    response = {"response": response_shows}
	    return jsonify(response)


	@api.errorhandler(BadRequest)
	def handle_bad_request(e):
	    response_msg = {"error": "Could not decode request: JSON parsing failed"}
	    return jsonify(response_msg), 400


	@api.errorhandler(HTTPException)
	def handle_exception(e):
	    response = e.get_response()
	    response.data = json.dumps({
	        "code": e.code,
	        "name": e.name,
	        "description": e.description,
	    })
	    response.content_type = "application/json"
	    return response


def create_app():
	app = Flask(__name__)

	app.register_blueprint(api)

	setup_api_routes(app)
 
	return app
