from flask import Blueprint, render_template

aula4_bp = Blueprint('aula4', __name__)

@aula4_bp.route('/aula4')
def aula4():
    return render_template('aula4.html')

@aula4_bp.route('/aula4_exercicio1')
def aula4_exercicio1():
    return render_template('aula4_exercicio1.html')

@aula4_bp.route('/aula4_exercicio2')
def aula4_exercicio2():
    return render_template('aula4_exercicio2.html')

@aula4_bp.route('/aula4_exercicio3')
def aula4_exercicio3():
    return render_template('aula4_exercicio3.html')

@aula4_bp.route('/aula4_exercicio4')
def aula4_exercicio4():
    return render_template('aula4_exercicio4.html')

@aula4_bp.route('/aula4_exercicio5')
def aula4_exercicio5():
    return render_template('aula4_exercicio5.html')
