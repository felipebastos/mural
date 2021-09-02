from flask import Blueprint, request, render_template, redirect, url_for

from app import base_de_recados

bp = Blueprint('mural', __name__, template_folder='templates', url_prefix='/mural')

@bp.post('/novorecado')
def novorecado():
    recado = {
        'dest': int(request.form['dest']),
        'remetente': request.form['remetente'],
        'conteudo': request.form['conteudo'],
    }
    base_de_recados.append(recado)
    return redirect(url_for('usuarios.perfil', id=request.form["dest"]))

# Rota que tem a ver só com mural
@bp.get('/recado/<int:id>')
def recado(id):
    return render_template('postarecado.html', id=id)