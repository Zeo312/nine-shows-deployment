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
1. 
