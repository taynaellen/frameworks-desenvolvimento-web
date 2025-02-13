from flask import Blueprint, render_template

aula11_bp = Blueprint('aula11', __name__)

@aula11_bp.route('/aula11')
def aula11():
    return render_template('aula11.html')