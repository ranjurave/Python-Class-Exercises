from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/success')
def success():
    return 'Logged In Successfully'

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['username'] == 'admin':
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))

if __name__ =='__main__':
    app.run(debug=True)