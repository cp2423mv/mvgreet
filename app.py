from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
  return "Hello world!"

@app.route('/greet')
def greet(person):
  return "Hello " + request.args.get('person', '')
