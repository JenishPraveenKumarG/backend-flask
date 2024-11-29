'''session - so that user dont need to login again and again

    example imagine you are usng a web and it remembers you till you shut it down this is the use of session'''

from flask import Flask,render_template,url_for,request,redirect,session

''' we can also set how much time the session data has tobe hold'''

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
        return redirect(url_for('user'))
    
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        
        return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f'<h1>{user}</h1>'
    
    else:
        return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    app.run(debug = True)