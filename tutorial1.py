''' basics of flask with routing'''


from flask import Flask,redirect,url_for



app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello, this is the Home page <h1>Hellooooo</h1>'

@app.route("/<name>")
def user(name):
    return f'Hello {name}'

@app.route('/admin')
def admin():
    return redirect(url_for("user",name = 'Admi!'))

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for better error tracking
