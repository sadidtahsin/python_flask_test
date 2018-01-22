import os
from flask import Flask
from flask import request
# from pymongo import MongoClient
app = Flask(__name__)
#test
# client = MongoClient('localhost:27017')
# db=client.sensor


@app.route('/')
def hello_world():
    return 'Hello Tamim!!! How are You!!!'

@app.route('/sensor/<name>/<age>',methods = ['POST', 'GET'])
def sensor(name=None,age=None):
   if request.method == 'POST':
      print (request.is_json)
      print("hello\n")
      content = request.json
    #   db.value.insert_one(content)
      print (content)
      
      return "done"
   else:

      return "done " +name+" "+age

if __name__ == '__main__':
   app.run(debug=True)
