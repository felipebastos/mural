from sqlalchemy import log
from usuarios.entidades import Usuario
from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required, login_user, logout_user

from app import db, bcrypt

bp = Blueprint('auth', __name__, url_prefix='/auth',
               template_folder='templates')


@bp.route('/login', methods=['GET', 'POST'])
def form_login():
    if request.method == 'POST':
        nick_tentativa = request.form['nick']
        senha_tentativa = request.form['senha']

        usuario = Usuario.query.filter_by(nick=nick_tentativa).first()
        if usuario:
            if bcrypt.check_password_hash(usuario.senha, senha_tentativa):
                login_user(usuario)
                flash('Parabéns! Você sabe a sua senha, e logou!')
                return redirect('/')
            else:
                flash('Errou a senha.')
                return redirect('/auth/login')
        else:
            flash('Usuário não existe.')
            return redirect('/auth/login')

    return render_template('auth/login.html')

@bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        print('É post')
        if Usuario.query.filter_by(nick=request.form['nick']).first() is not None:
            print('já tinha')
            flash('O nick já está em uso, escolha outro.')
            return redirect('/auth/cadastro')
        novo = Usuario()
        novo.nick = request.form['nick']
        novo.nome = request.form['nome']
        novo.sobrenome = request.form['sobrenome']
        novo.senha = bcrypt.generate_password_hash(request.form['senha'])

        db.session.add(novo)
        db.session.commit()

        flash('Usuário cadastro dom sucesso!')
        return redirect('/')

    return render_template('auth/cadastro.html')

@bp.get('/logout')
@login_required
def sair():
    logout_user()
    flash('Saiu com sucesso!')
    return redirect('/')
