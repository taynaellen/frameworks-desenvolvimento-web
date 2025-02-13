from flask import Blueprint, render_template

aula14_bp = Blueprint('aula14', __name__)

@aula14_bp.route('/aula14')
def aula14():
    return render_template('aula14.html')