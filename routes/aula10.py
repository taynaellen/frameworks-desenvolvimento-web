from flask import Blueprint, render_template

aula10_bp = Blueprint('aula10', __name__)

@aula10_bp.route('/aula10')
def aula10():
    return render_template('aula10.html')