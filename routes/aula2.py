from flask import Blueprint, render_template

aula2_bp = Blueprint('aula2', __name__)

@aula2_bp.route('/aula2')
def aula2():
    return render_template('aula2.html')