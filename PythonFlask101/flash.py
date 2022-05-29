from flask import Flask, flash, render_template, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'random string'
@app.route('/')
def index():
    return render_template('indexFlash.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != "admin" or request.form['password'] != 'admin':
            error = 'User name or password was wrong.'
        else:
            flash('You have successfully logged in.')
            flash('Log out before log in again.')
            return redirect(url_for('index'))
    return render_template('log_in.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)