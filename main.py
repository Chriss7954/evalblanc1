from bottle import route, run
from test import hello

@route('/')
def page():
    return hello()


run(host='localhost', port=8080, debug=False)
