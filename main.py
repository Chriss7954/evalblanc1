from bottle import route, run


@route('/')
def hello():
    return "Hello main"


run(host='localhost', port=8080, debug=False)
