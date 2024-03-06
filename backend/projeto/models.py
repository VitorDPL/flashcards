from flask_sqlalchemy import SQLAlchemy
from projeto import db

class QuestoesErradas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questao = db.Column(db.Text)
    resposta = db.Column(db.Text)

class MateriaFundamentosDeProgramacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questao = db.Column(db.Text)
    resposta = db.Column(db.Text)
    acertou = db.Column(db.Boolean, default=False)

class MateriaFundamentosDeBancoDeDados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questao = db.Column(db.Text)
    resposta = db.Column(db.Text)
    acertou = db.Column(db.Boolean, default=False)

class MateriaEngenhariaDeSoftware(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questao = db.Column(db.Text)
    resposta = db.Column(db.Text)
    acertou = db.Column(db.Boolean, default=False)

class MateriaRedes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questao = db.Column(db.Text)
    resposta = db.Column(db.Text)
    acertou = db.Column(db.Boolean, default=False)

class MateriaSistemasOperacionais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questao = db.Column(db.Text)
    resposta = db.Column(db.Text)
    acertou = db.Column(db.Boolean, default=False)