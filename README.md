# Nine shows

A Flask-based JSON API that accepts data on nine shows (https://www.nine.com.au/) and returns a filtered response.

Example request: http://codingchallenge.nine.com.au/sample_request.json
<br>Example response: http://codingchallenge.nine.com.au/sample_response.json


If invalid JSON is sent, a JSON response with HTTP status 400 Bad Request, and with an "error" key containing the string "Could not decode request". For example:

{
    "error": "Could not decode request: JSON parsing failed"
}

## Run development server

### Installation steps:

Note: This service was built using Python 3.6.4
1. Clone the repository
2. cd into cloned folder
3. Create a python virtual environment (See https://docs.python.org/3/library/venv.html)
   `python3 -m venv venv` works on mac
4. Activate the virtualenv: `source ./venv/bin/activate`
5. Now run `pip install -r requirements.txt` 
6. Run `export FLASK_APP=app.api`
7. Run `flask run`

Now, you should be able to post your json data to the endpoint '/processjson' on localhost like 'localhost:\<port\>/processjson'

### Testing

1. cd into /tests
2. Run `pytest`

## Deployment

This API is deployed on heroku.
You can post your data to https://nine-shows-deployment.herokuapp.com/processjson using a service like postman (https://www.postman.com/)
