from bottle import route, run
import sys


@route('/')
def hello():
    return "Hello main"

run(host='localhost', port=8080, debug=False)