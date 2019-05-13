import os
from flask import Flask
from flask import request
from flask import json
app = Flask(__name__)
#test

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    msg={"text": {"text": ["We could find few matching products based on your query"]}},{"text": {"text": ["2nd text"]}}
    data= {"fulfillmentText":" Well Done ","fulfillmentMessages":[{"text": {"text": ["We could find few matching products based on your query"]}},{"text": {"text": ["2nd text"]}}],"source":""}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response



if __name__ == '__main__':
   app.run(debug=True)
