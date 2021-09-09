from flask import Blueprint, render_template, request, flash, redirect

from app import db
from usuarios.entidades import Usuario

bp_usuarios = Blueprint('usuarios', __name__, static_folder='static_usu', template_folder='templates_usu', url_prefix='/usu')

@bp_usuarios.get('/perfil/<int:id>')
def perfil(id):
    usu = Usuario.query.get(id)

    return render_template('usuarios/perfil.html', usuario=usu)

@bp_usuarios.get('/cad')
def cadastro():
    return render_template('usuarios/cadastro.html')

@bp_usuarios.post('/addcadastro')
def cadastrar():
    usuario = Usuario()
    usuario.nome = request.form['nome']
    usuario.sobrenome = request.form['sobrenome']
    usuario.idade = int(request.form['idade'])

    db.session.add(usuario)
    db.session.commit()

    flash(f'Mural de {usuario.nome} criado com sucesso!')

    return redirect('/')

@bp_usuarios.get('/salva/<nome>/<sobrenome>')
def salva(nome, sobrenome):
    # db
    # Usuario
    novo = Usuario()
    novo.nome = nome
    novo.sobrenome = sobrenome

    db.session.add(novo)
    db.session.commit()

    return('Salvei')

@bp_usuarios.get('/lista')
def lista():
    # select * from usuario;
    usuarios = Usuario.query.all()

    res = ''
    for usuario in usuarios:
        res = res + f'ID: {usuario.id} - Nome completo: {usuario.nome} {usuario.sobrenome} - Idade: {usuario.idade} <br>'

    return res

@bp_usuarios.get('/por_nome/<nome_busca>')
def busca_nome(nome_busca):
    # select * from usuarios where nome=nome;
    usuario = Usuario.query.filter_by(nome=nome_busca).first()

    return f'ID: {usuario.id} - Nome completo: {usuario.nome} {usuario.sobrenome} - Idade: {usuario.idade} <br>'


@bp_usuarios.get('/por_sn/<sn_busca>')
def busca_sn(sn_busca):
    # select * from usuarios where nome=nome;
    usuarios = Usuario.query.filter_by(sobrenome=sn_busca)

    res = ''
    for usuario in usuarios:
        res = res + f'ID: {usuario.id} - Nome completo: {usuario.nome} {usuario.sobrenome} - Idade: {usuario.idade} <br>'

    return res

@bp_usuarios.get('/atu/<id>/<sobrenome_novo>')
def atu_sobre(id, sobrenome_novo):
    usuario = Usuario.query.get(id)
    usuario.sobrenome = sobrenome_novo

    db.session.add(usuario)
    db.session.commit()

    return redirect('/usu/lista')

@bp_usuarios.get('/remove/<id>')
def remove_usu(id):
    usuario = Usuario.query.get(id)

    db.session.delete(usuario)
    db.session.commit()

    return redirect('/usu/lista')