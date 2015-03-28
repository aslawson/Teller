# General application libraries
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
# Databasing libraries
from firebase import firebase
import hashlib

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='fortuneteller'
))

firebase = firebase.FirebaseApplication('https://teller.firebaseio.com', None)

@app.route('/login', methods=['GET', 'POST'])
def login():
  # Handle data after the user clicks login or register
  if request.method == 'POST':
    if 'password2' not in request.form.keys(): # Logging in, not registering
      print 'login', request.form['phonenumber'], request.form['password']
    else: # Registering
      phone_number = request.form['phonenumber']
      password1 = request.form['password1']
      password2 = request.form['password2']
      if password1 == password2:
        print 'here'
        user_exists = firebase.get('/users/'+phone_number, None)
        # Do they already have an account?
        if user_exists == None:
          hash_password = hashlib.sha224(password1).hexdigest()
          insert_data = {
            'hash_password': hash_password
          }
          inserted_user = firebase.post('/users/'+phone_number, insert_data)
          # All is good, the user is logged in!
          session['logged_in'] = True
      print 'register', request.form['phonenumber'], request.form['password2']
  if session.get('logged_in'):
    return redirect(url_for('main'))
  return render_template('login.html')

@app.route('/')
def main():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  # Application logic
  return render_template('main.html')

if __name__ == '__main__':
    app.run()


