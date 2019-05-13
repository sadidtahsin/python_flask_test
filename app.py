import os
from flask import Flask
from flask import request
from flask import json
app = Flask(__name__)
#test

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    #msg={"text": {"text": ["We could find few matching products based on your query"]}},{"text": {"text": ["2nd text"]}}
    msg={ "fulfillmentText": "This is a text response", "fulfillmentMessages": [ { "card": { "title": "card title", "subtitle": "card text", "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png", "buttons": [ { "text": "button text", "postback": "https://assistant.google.com/" } ] } } ], "source": "example.com", "payload": { "google": { "expectUserResponse": True, "richResponse": { "items": [ { "simpleResponse": { "textToSpeech": "this is a simple response" } } ] } }, "facebook": { "text": "Hello, Facebook!" }, "slack": { "text": "This is a text response for Slack." } }, "outputContexts": [ { "name": "projects/${PROJECT_ID}/agent/sessions/${SESSION_ID}/contexts/context name", "lifespanCount": 5, "parameters": { "param": "param value" } } ], "followupEventInput": { "name": "event name", "languageCode": "en-US", "parameters": { "param": "param value" } } }
    data= {"fulfillmentText":" Well Done ","fulfillmentMessages":[{"text": {"text": ["We could find few matching products based on your query"]}},{"text": {"text": ["2nd text"]}}],"source":""}
    response = app.response_class(
        response=json.dumps(msg),
        status=200,
        mimetype='application/json'
    )
    return response



if __name__ == '__main__':
   app.run(debug=True)
