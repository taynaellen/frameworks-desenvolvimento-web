from flask import Blueprint, render_template

class_list_bp = Blueprint('class_list', __name__)

@class_list_bp.route('/class_list')
def class_list():
    return render_template('class_list.html')