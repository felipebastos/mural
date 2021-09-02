from flask import Flask, render_template

# Configurações do app
app = Flask(__name__)
app.secret_key = '123456'

# Entidades do projeto
lista_usuarios = [
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

# Rotas ou Views
@app.route('/')
def principal():
    return render_template('index.html', lista_usuarios=lista_usuarios)

# Rotas que tem a ver só com usuários


from usuarios import usuarios
app.register_blueprint(usuarios.bp_usuarios)

from mural import mural
app.register_blueprint(mural.bp)

# Rota que tem a ver só com usuários
