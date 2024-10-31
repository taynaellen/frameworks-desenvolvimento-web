from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return 'hello world'

@app.route('/contact')
def contact():
    return render_template('contact.html')




if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0')


