from flask import Flask 
from controller.controle import *
from controller.controle2 import url2
from controller.etx import db
import os
from dotenv import load_dotenv
from config import db
from flask_restx import Api
from controller.manifesto_carga_controller import manifesto_cargas_blueprint


load_dotenv()

url_bd = os.getenv("DB_URL")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url_bd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(manifesto_cargas_blueprint)


db.init_app(app)  # necessário
app.register_blueprint(url)
app.register_blueprint(url2)

if __name__ == "__main__":
    app.run(
        debug=True,
    )
    