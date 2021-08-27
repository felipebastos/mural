from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = '123456'

usuarios = [
    {'id': 1, 'nome': 'Reperquilson', 'sobrenome': 'Bastos', 'idade': 19},
    {'id': 2, 'nome': 'Reperqueli', 'sobrenome': 'Bastos', 'idade': 18},
    {'id': 3, 'nome': 'Mundico', 'sobrenome': 'Bastos', 'idade': 17},
]

base_de_recados = [
    {'dest': 1, 'remetente': 'Reperqueli', 'conteudo': 'E aí maninho!'},
    {'dest': 1, 'remetente': 'Mundico', 'conteudo': 'Cadê minha cueca?'},
    {'dest': 2, 'remetente': 'Mundico', 'conteudo': 'Tou com fome, traz coxinha?'},
    {'dest': 3, 'remetente': 'Reperqueli',
        'conteudo': 'Um real a entrega. Fora valor da coxinha.'},
    {'dest': 1, 'remetente': 'Mundico', 'conteudo': 'Já achei.'},
    {'dest': 2, 'remetente': 'Reperqueli', 'conteudo': 'Você é linda!'},
]


@app.route('/')
def principal():
    return render_template('index.html', usuarios=usuarios)


@app.get('/perfil/<int:id>')
def perfil(id):
    res = None
    for usuario in usuarios:
        if usuario['id'] == id:
            res = usuario

    recados_encontrados = []
    for recado in base_de_recados:
        if recado['dest'] == id:
            recados_encontrados.append(recado)

    return render_template('perfil.html', usuario=res, recados=recados_encontrados)


@app.post('/novorecado')
def novorecado():
    recado = {
        'dest': int(request.form['dest']),
        'remetente': request.form['remetente'],
        'conteudo': request.form['conteudo'],
    }
    base_de_recados.append(recado)
    return redirect(f'/perfil/{request.form["dest"]}')


@app.get('/recado/<int:id>')
def recado(id):
    return render_template('postarecado.html', id=id)


@app.get('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.post('/addcadastro')
def cadastrar():
    id_novo = len(usuarios)+1
    nome_novo = request.form['nome']
    sobrenome_novo = request.form['sobrenome']
    idade_novo = int(request.form['idade'])

    novo_usuario = {
        'id': id_novo,
        'nome': nome_novo,
        'sobrenome': sobrenome_novo,
        'idade': idade_novo
        }
    
    usuarios.append(novo_usuario)

    flash(f'Mural de {nome_novo} criado com sucesso!')

    return redirect('/')