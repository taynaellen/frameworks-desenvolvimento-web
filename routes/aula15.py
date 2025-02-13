from flask import Blueprint, render_template

aula15_bp = Blueprint('aula15', __name__)

@aula15_bp.route('/aula15')
def aula15():
    return render_template('aula15.html')