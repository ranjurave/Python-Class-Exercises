from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    username = request.form['nm']
    age = request.form['age']
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('username', username)
    resp.set_cookie('age', age)
    return resp

@app.route('/getcookie')
def getcookie():
    username = request.cookies.get('username')
    age = request.cookies.get('age')
    return f'User {username} is {age} years old'

if __name__=="__main__":
    app.run(debug=True)