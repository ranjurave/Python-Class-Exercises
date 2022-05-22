from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hi Ranju Raveendran </h1>"

@app.route('/hello/<name>')
def hello_user(name):
    return f"<h1>Hello {name} </h1>"

if __name__=='__main__':
    app.run(debug=True)