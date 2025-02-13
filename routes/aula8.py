from flask import Blueprint, render_template

aula8_bp = Blueprint('aula8', __name__)

@aula8_bp.route('/aula8')
def aula8():
    return render_template('aula8.html')