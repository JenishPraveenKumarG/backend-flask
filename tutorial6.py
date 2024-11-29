'''Message flashing '''

from flask import Flask,render_template,url_for,request,redirect,session,flash

from datetime import timedelta

app = Flask(__name__)
'''session is stored on the server where we need a secret key to encrypy and decrypt it'''

app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5) # this keeps the data for 5 minuted and then again theuser has to login we can also set it for days


@app.route('/')
def home():
    return render_template('index4.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        flash("Login successfull!")
        return redirect(url_for('user'))
    
    else:
        if 'user' in session:
            flash("Already Logged in")
            return redirect(url_for('user'))
        
        return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template("user.html",user = user)
    
    else:
        flash("You are not Logged in!")
        return redirect(url_for('login'))
    

@app.route('/logout')
def logout():

    flash("You have been logged out!")
    session.pop('user',None)
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    app.run(debug = True)