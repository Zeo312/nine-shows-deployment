from flask import Flask, request
from flask import jsonify
from werkzeug.exceptions import HTTPException, BadRequest
import json

app = Flask(__name__)


@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json(force=True)

    response_shows = []
    response = {}

    for show in data["payload"]:
        if("drm" in show and "episodeCount" in show and "image" in show and
                "slug" in show and "title" in show and show["drm"] is True and
                show["episodeCount"] > 0):
            image = show["image"]["showImage"]
            slug = show["slug"]
            title = show["title"]
            filtered_show = {"image": image, "slug": slug, "title": title}
            response_shows.append(filtered_show)

    response = {"response": response_shows}
    return jsonify(response)


@app.errorhandler(BadRequest)
def handle_bad_request(e):
    response_msg = {"error": "Could not decode request: JSON parsing failed"}
    return jsonify(response_msg), 400


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == '__main__':
    app.run(debug=True)
