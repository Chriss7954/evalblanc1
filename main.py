from bottle import route, run
from test import hello
import sys


@route("/")
def page():
    return hello()


run(host="0.0.0.0", port=sys.argv[1], reloader=True)
