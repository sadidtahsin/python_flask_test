import os
from flask import Flask
from flask import request
app = Flask(__name__)
#test

@app.route('/')
def hello_world():
    
    return 'Hello Sadid Tahsin Tamim!!! How are Boy!!!'



if __name__ == '__main__':
   app.run(debug=True)
