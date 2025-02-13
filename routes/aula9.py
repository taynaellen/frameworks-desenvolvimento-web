from flask import Blueprint, render_template

aula9_bp = Blueprint('aula9', __name__)

@aula9_bp.route('/aula9')
def aula9():
    return render_template('aula9.html')