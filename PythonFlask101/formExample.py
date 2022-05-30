from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = "random_text"

@app.route('/contact', methods = ['POST' , 'GET'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('Data required in all fields.')
            flash('All fields must be filled')
            flash('Please try again')
            return render_template('contact.html', form=form)
        else:
            return render_template('success.html')
    if request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
