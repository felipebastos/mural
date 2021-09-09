from sqlalchemy.orm import backref
from app import db

'''
CREATE TABLE usuario (
    id INTEGER auto_increment,
    nome VARCHAR(100) UNIQUE NOT NULL,
    sobrenome VARCHAR(200) NOT NULL,
    idade INTEGER,
    CONSTRAINT PK_USU PRIMARY KEY (id)
)
'''

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    sobrenome = db.Column(db.String(200), nullable=False)
    idade = db.Column(db.Integer, default=0)

    recados = db.relationship('Recado', backref='usuario', lazy=True)

# Entidades do projeto
#lista_usuarios = [
#    {'id': 1, 'nome': 'Reperquilson', 'sobrenome': 'Bastos', 'idade': 19},
#    {'id': 2, 'nome': 'Reperqueli', 'sobrenome': 'Bastos', 'idade': 18},
#    {'id': 3, 'nome': 'Mundico', 'sobrenome': 'Bastos', 'idade': 17},
#]

class Recado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dest = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    remetente = db.Column(db.String(100), default="anônimo")
    conteudo = db.Column(db.String(1000), nullable=False)

base_de_recados = [
    {'dest': 1, 'remetente': 'Reperqueli', 'conteudo': 'E aí maninho!'},
    {'dest': 1, 'remetente': 'Mundico', 'conteudo': 'Cadê minha cueca?'},
    {'dest': 2, 'remetente': 'Mundico', 'conteudo': 'Tou com fome, traz coxinha?'},
    {'dest': 3, 'remetente': 'Reperqueli',
        'conteudo': 'Um real a entrega. Fora valor da coxinha.'},
    {'dest': 1, 'remetente': 'Mundico', 'conteudo': 'Já achei.'},
    {'dest': 2, 'remetente': 'Reperqueli', 'conteudo': 'Você é linda!'},
]
