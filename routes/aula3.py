from flask import Blueprint, render_template

aula3_bp = Blueprint('aula3', __name__)

@aula3_bp.route('/aula3')
def aula3():
    return render_template('aula3.html')