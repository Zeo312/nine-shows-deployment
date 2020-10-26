# Nine shows

A Flask-based JSON API that accepts data on nine shows (https://www.nine.com.au/) and returns a filtered response.

Example request: http://codingchallenge.nine.com.au/sample_request.json
<br>Example response: http://codingchallenge.nine.com.au/sample_response.json


If invalid JSON is sent, a JSON response with HTTP status 400 Bad Request, and with an "error" key containing the string "Could not decode request" is returned. For example:

{
    "error": "Could not decode request: JSON parsing failed"
}

## Run development server

### Installation steps:

Note: This API was written using Python 3.6.4 and tested on MacOS
1. Clone the repository by copying the SSH link and running `git clone <paste_link_here>` in the directory you want to clone into
2. cd into the cloned diretory, then create a python virtual environment (See https://docs.python.org/3/library/venv.html)
   <br>`python3 -m venv venv` works on mac ]
3. Activate the virtualenv: `source ./venv/bin/activate`
4. Now run `pip install -r requirements.txt` 
5. Run `export FLASK_APP=app.api`
6. Run `flask run`

Now, you should be able to POST your json data to the endpoint '/processjson' on localhost like 'localhost:\<port\>/processjson'

### Testing

1. cd into /tests
2. Run `pytest`

## Deployment

This API is deployed on heroku.
You can POST your data to https://nine-shows-deployment.herokuapp.com/processjson using a service like postman (https://www.postman.com/)
