from flask import render_template
from usuarios.entidades import Usuario

def principal():
    usuarios = Usuario.query.all()
    return render_template('index.html', lista_usuarios=usuarios)

def erro(error):
    return render_template('erro.html', mensagem_erro=error.description)