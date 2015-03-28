# General application libraries
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
# Databasing libraries
from firebase import firebase
import hashlib
import lib.sendmoney as sendmoney

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='fortuneteller'
))


firebase = firebase.FirebaseApplication('https://teller.firebaseio.com', None)

send_money = sendmoney.SendMoney()

@app.route('/login', methods=['GET', 'POST'])
def login():
  # Handle data after the user clicks login or register
  if request.method == 'POST':
    if 'password2' not in request.form.keys(): # Logging in, not registering
      print('login', request.form['phonenumber'], request.form['password'])
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
          session['phone_number'] = phone_number
          session['logged_in'] = True
        else: 
          print ('')#TODO - change "Invalid log in" statement to visabe
      print 'login', request.form['phonenumber'], request.form['password']
    else: # Registering
      phone_number = request.form['phonenumber']
      password1 = request.form['password1']
      password2 = request.form['password2']
      if password1 == password2:
        print ('here')
        user_exists = firebase.get('/users/'+phone_number, None)
        # Do they already have an account?
        if user_exists == None:
          hash_password = hashlib.sha224(password1).hexdigest()          
          inserted_user = firebase.put('/users/'+phone_number, 'hash_password', hash_password)
          # All is good, the user is logged in!
          session['phone_number'] = phone_number
          session['logged_in'] = True
      print('register', request.form['phonenumber'], request.form['password2'])
  if session.get('logged_in'):
    return redirect(url_for('main'))
  return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def main():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  # Application logic -- Set up a phone
  dummy_card = "5184680430000279"
  dummy_expiry = "202001"
  send_money.setup_phone(session['phone_number'], dummy_card, dummy_expiry)
  if request.method == 'POST' and 'submit2' in request.form.keys():
    session['logged_in'] = False
    return redirect(url_for('login'))
  return render_template('main.html', phone_number=session['phone_number'])


@app.route('/sendmoney', methods=['GET', 'POST'])
def sendmoney():
  if request.method == 'POST': # sending money
    sender_phone = ""
    receiver_phone = request.form['receiver_phone']
    amount = request.form['amount']
    transfer_request(self, sender_phone, receiver_phone, amount)
  return render_template('sendmoney.html')

@app.route('/inserttransaction', methods=['POST'])
def inserttransaction():
  # insert into firebase
  amount = float(request.form['amount'])

  if request.form['transaction_type'] == "Deposit":
    amount = 0 - amount
  firebase.post('/transactions/', {'amt': amount, 'to': None, 'from': session.get('phone_number')})
  need = 0 - amount
  
  matchlist = []
  diction = firebase.get('transactions', None)
  for k,v in diction.iteritems():
    if (need > 0 and v['amt'] < 1.1*need and v['amt'] > .9*need):
      matchlist.append(v)
    elif (need < 0 and v['amt'] > 1.1*need and v['amt'] < .9*need):
      matchlist.append(v)
  
  for v in matchlist:
    print v
  #result = firebase.get('/transactions/amt' < 1.1*need or '/transactions/amt' > .9*need, None)
  #print result
  return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(host = "0.0.0.0")
    


