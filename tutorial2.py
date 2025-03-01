''' adding templates '''

from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

'''@app.route("/")
def home():
    return render_template('index.html')'''


@app.route('/<name>')
def home(name):
    return render_template('index.html',content = name)

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for better error tracking
