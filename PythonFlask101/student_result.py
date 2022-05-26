from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def enter_marks():
    return render_template('entermarks.html')

@app.route('/results', methods = ['POST','GET'])
def display_results():
    if request.method == 'POST':
        result = request.form
        return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
