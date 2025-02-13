from flask import Blueprint, render_template

aula1_bp = Blueprint('aula1', __name__)

@aula1_bp.route('/aula1')
def aula1():
    return render_template('aula1.html')