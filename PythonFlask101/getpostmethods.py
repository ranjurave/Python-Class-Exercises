from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome_user(name):
    return f'<p> welcome {name} </p>'

@app.route('/login', methods =['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('welcome_user', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('welcome_user', name=user))

if(__name__=='__main__'):
    app.run(debug=True)