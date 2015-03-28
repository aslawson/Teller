# General application libraries
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
# Databasing libraries
from firebase import firebase

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True
))

firebase = firebase.FirebaseApplication('https://teller.firebaseio.io', None)

@app.route("/")
def hello():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()