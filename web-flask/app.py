#!/usr/bin/python3
""" Starts a Flash Web Application C is FUN"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def portfolio():
    """ portfolio home page """
    return render_template("index.html")


@app.route('/signin', strict_slashes=False)
def signin():
    """ Signin page """
    return render_template('signin.html')

@app.route('/signup', strict_slashes=False)
def signup():
    """ Signup page """
    return render_template('signup.html')

@app.route('/cart', strict_slashes=False)
def cart():
    """ Cart items page """
    return render_template('cart.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)