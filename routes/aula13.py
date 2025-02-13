from flask import Blueprint, render_template

aula13_bp = Blueprint('aula13', __name__)

@aula13_bp.route('/aula13')
def aula13():
    return render_template('aula13.html')