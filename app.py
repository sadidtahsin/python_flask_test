import os
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)
#test

@app.route('/')
def hello_world():
    msg="Hello Tamim"
    return jsonify(
        fulfillmentText=" ",
        fulfillmentMessage=[{'text': {'text':[msg]}}],
        source=""
    )



if __name__ == '__main__':
   app.run(debug=True)
