import os
from flask import Flask
from flask import request
from pymongo import MongoClient
app = Flask(__name__)
#test

c
@app.route('/')
def hello_world():
    
    return 'Hello Tamim!!! How are Boy!!!'

if __name__ == '__main__':
   app.run(debug=True)
