# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def addition():
    """adds 2 ints, a and b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)


@app.route("/sub")
def subtraction():
    """subtracts 2 ints, a and b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)


@app.route("/mult")
def multiply():
    """multiplies 2 ints, a and b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)


@app.route("/div")
def divide():
    """divides 2 ints, a and b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)
