from flask import Blueprint, render_template


bp = Blueprint('sobre', __name__, template_folder='templates', url_prefix='/sobre')

@bp.get('/')
def sobre():
    return render_template('sobre/index.html')