from flask import Blueprint, render_template

aula12_bp = Blueprint('aula12', __name__)

@aula12_bp.route('/aula12')
def aula12():
    return render_template('aula12.html')