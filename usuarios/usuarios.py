from flask import Blueprint, render_template, request, flash, redirect

from app import lista_usuarios, base_de_recados

bp_usuarios = Blueprint('usuarios', __name__, static_folder='static_usu', template_folder='templates_usu', url_prefix='/usu')

@bp_usuarios.get('/perfil/<int:id>')
def perfil(id):
    res = None
    for usuario in lista_usuarios:
        if usuario['id'] == id:
            res = usuario

    recados_encontrados = []
    for recado in base_de_recados:
        if recado['dest'] == id:
            recados_encontrados.append(recado)

    return render_template('usuarios/perfil.html', usuario=res, recados=recados_encontrados)

@bp_usuarios.get('/cad')
def cadastro():
    return render_template('usuarios/cadastro.html')

@bp_usuarios.post('/addcadastro')
def cadastrar():
    id_novo = len(lista_usuarios)+1
    nome_novo = request.form['nome']
    sobrenome_novo = request.form['sobrenome']
    idade_novo = int(request.form['idade'])

    novo_usuario = {
        'id': id_novo,
        'nome': nome_novo,
        'sobrenome': sobrenome_novo,
        'idade': idade_novo
        }
    
    lista_usuarios.append(novo_usuario)

    flash(f'Mural de {nome_novo} criado com sucesso!')

    return redirect('/')