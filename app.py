from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return 'hello world'

@app.route('/contact')
def contact():
    return render_template('contact.html')

#Exercicios dia 30/10/24
@app.route('/exercicio1')
def exercicio1():
    return render_template('exercicio1.html')

@app.route('/exercicio2')
def exercicio2():
    return render_template('exercicio2.html')

@app.route('/exercicio3')
def exercicio3():
    return render_template('exercicio3.html')

@app.route('/exercicio4')
def exercicio4():
    return render_template('exercicio4.html')

@app.route('/exercicio5')
def exercicio5():
    return render_template('exercicio5.html')


#Exercícios dia 06/11/24




















if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0')


