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
      phone_number = request.form['phonenumber']
      password = request.form['password']
      
      result = firebase.get('/users/'+phone_number, None)
      print result
      # Are they a registered user?
      if result == None:
        print ('')#TODO - change "Invalid log in" statement to visabe
      else:
        hash_password = hashlib.sha224(password).hexdigest()
        print result['hash_password']
        print hash_password
        if hash_password == result['hash_password']:
          # Successful Log In
          session['logged_in'] = True
        else: 
          print ('')#TODO - change "Invalid log in" statement to visabe
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
          inserted_user = firebase.put('/users/'+phone_number, 'hash_password', hash_password)
          # All is good, the user is logged in!
          session['logged_in'] = True
      print 'register', request.form['phonenumber'], request.form['password2']
  if session.get('logged_in'):
    return redirect(url_for('main'))
  return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def main():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  # Application logic
  if request.method == 'POST':
    session['logged_in'] = False
    return redirect(url_for('login'))
  return render_template('main.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0")
    


