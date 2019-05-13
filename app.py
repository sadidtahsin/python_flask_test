import os
from flask import Flask
from flask import request
from flask import json
app = Flask(__name__)
#test

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    #msg={"text": {"text": ["We could find few matching products based on your query"]}},{"text": {"text": ["2nd text"]}}
    msg={ "fulfillmentText": "This is a text response", "fulfillmentMessages": [], "source": "example.com", "payload": { "google": { "expectUserResponse": True, "richResponse": { "items": [ { "simpleResponse": { "textToSpeech": "This is a Basic Card:" } }, { "basicCard": { "title": "card title", "image": { "url": "https://cdn1.imggmi.com/uploads/2019/5/13/cb54c19ac65af5acb8e495d0d69cba75-full.png", "accessibilityText": "Google Logo" }, "buttons": [ { "title": "Button Title", "openUrlAction": { "url": "https://www.google.com" } } ], "imageDisplayOptions": "WHITE" } } ] } } }, "outputContexts": [], "followupEventInput": {} }
    data= {"fulfillmentText":" Well Done ","fulfillmentMessages":[{"text": {"text": ["We could find few matching products based on your query"]}},{"text": {"text": ["2nd text"]}}],"source":""}
    response = app.response_class(
        response=json.dumps(msg),
        status=200,
        mimetype='application/json'
    )
    return response



if __name__ == '__main__':
   app.run(debug=True)
