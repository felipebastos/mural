from flask import Blueprint, request, render_template, redirect, url_for

from app import db
from usuarios.entidades import Recado

bp = Blueprint('mural', __name__, template_folder='templates', url_prefix='/mural')

@bp.post('/novorecado')
def novorecado():
    novo_recado = Recado()
    novo_recado.dest = int(request.form['dest'])
    novo_recado.remetente = request.form['remetente']
    novo_recado.conteudo = request.form['conteudo']
    
    db.session.add(novo_recado)
    db.session.commit()

    return redirect(url_for('usuarios.perfil', id=request.form["dest"]))

# Rota que tem a ver só com mural
@bp.get('/recado/<int:id>')
def recado(id):
    return render_template('mural/postarecado.html', id=id)