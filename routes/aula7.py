from flask import Blueprint, render_template

aula7_bp = Blueprint('aula7', __name__)

@aula7_bp.route('/aula7')
def aula7():
    return render_template('aula7.html')