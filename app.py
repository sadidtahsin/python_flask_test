import os
from flask import Flask
from flask import request
from flask import json
app = Flask(__name__)
#test

@app.route('/')
def hello_world():
    msg="Hello Tamim"
    data= '{fulfillmentText=" ",fulfillmentMessages=[{'text': {'text':[msg]}}],source=""}'
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response



if __name__ == '__main__':
   app.run(debug=True)
