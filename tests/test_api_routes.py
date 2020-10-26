from flask import Flask
import json

from nine_coding_test_master.app.api import setup_api_routes

#Create new instance of app to not disrupt the instance that's being served
def create_app():
	app = Flask(__name__)
	setup_api_routes(app)
	client = app.test_client()
	return client

def test_post_success():
	client = create_app()
	url = '/processjson'

	path = "./test_data/valid_data.json"
	f = open(path, "r")
	test_data = f.read()

	response = client.post(url, data=test_data)
	assert response.status_code == 200

def test_post_fail_bad_request():
	client = create_app()
	url = '/processjson'

	#Testing with invalid data
	path = './test_data/invalid_data.json'
	f = open(path, "r")
	test_data = f.read()

	response = client.post(url, data=test_data)
	assert response.status_code == 400

	#Testing with empty data
	path = './test_data/empty_data.json'
	f = open(path, "r")
	test_data = f.read()

	response = client.post(url, data=test_data)
	assert response.status_code == 400



