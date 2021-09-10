from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

# Carregando variáveis de ambiente.
from dotenv import load_dotenv

import os

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()


# Configurações do app
def create_app():
    load_dotenv('.env')

    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from routes import principal
        app.add_url_rule('/', view_func=principal)

        from usuarios import usuarios
        app.register_blueprint(usuarios.bp_usuarios)

        from mural import mural
        app.register_blueprint(mural.bp)

        from sobre import sobre
        app.register_blueprint(sobre.bp)

    return app
