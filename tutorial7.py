''' SQL alchamy database'''

from flask import Flask,render_template,url_for,request,redirect,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5) # this keeps the data for 5 minuted and then again theuser has to login we can also set it for days

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self,name,email = None):
        self.name = name
        self.email = email


@app.route('/')
def home():
    return render_template('index_.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user

        found_user = users.query.filter_by(name = user).delete()
        for user in found_user:
            user.delete()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = users(user)
            db.session.add(usr)
            db.session.commit()

        flash("Login successfull!")
        return redirect(url_for('user'))
    
    else:
        if 'user' in session:
            flash("Already Logged in")
            return redirect(url_for('user'))
        
        return render_template('login.html')

@app.route('/user',methods = ['POST','GET'])
def user():
    email = None
    if 'user' in session:
        user = session['user']

        if request.method == "POST":
            email = request.form['email']
            session['email'] = email
            found_user = users.query.filter_by(name = user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")
        else:
            if email in session:
                email = session['email']
        
        return render_template("user.html",email = email)

    
    else:
        flash("You are not Logged in!")
        return redirect(url_for('login'))
    

@app.route('/logout')
def logout():

    flash("You have been logged out!")
    session.pop('user',None)
    session.pop('email',None)
    return redirect(url_for('login'))

@app.route('/view')
def view():
    return render_template('view.html',values = users.query.all())
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates the database tables
    app.run(debug=True)
