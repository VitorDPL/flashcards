from projeto import app, db
from flask import request, jsonify
from projeto.models import *
import random

def todas_as_questoes_erradas():
    try:
        data = request.json
        pergunta = data.get('pergunta')
        resposta = data.get('resposta')

        questao_errada = QuestoesErradas(
            questao = pergunta,
            resposta = resposta
        )

        db.session.add(questao_errada)
        db.session.commit()

        return jsonify({'message' : 'Questão enviada ao banco de erros.'})
    
    except Exception as e:
        return jsonify({'error' : str(e)}), 500
    
def deletar_questao(BancoDeDados):
    try:
        data = request.json
        id = data.get('id')
        
        if id is not None:
            questao_errada = BancoDeDados.query.filter_by(id=id).first()

            if questao_errada:
                db.session.delete(questao_errada)
                db.session.commit()

                return jsonify({'message': 'Questão errada deletada com sucesso.'}), 200
            else:
                return jsonify({'error': 'Questão errada não encontrada.'}), 404
        else:
            return jsonify({'error': 'ID da questão não fornecido.'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


def cadastrar_pergunta(BancoDeDados):
    try:
        data = request.json

        nova_questao = BancoDeDados(
            questao=data.get('pergunta'),
            resposta=data.get('resposta'),
        )

        db.session.add(nova_questao)
        db.session.commit()

        return jsonify({'message': 'Questão cadastrada com sucesso.'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def buscar_perguntas(BancoDeDados):
    try:
        questoes = BancoDeDados.query.all()

        # embaralhando a lista
        random.shuffle(questoes)

        # convertendo as questões embaralhadas para o formato JSON
        questoes_json = [{'id': questao.id, 'questao': questao.questao, 'resposta': questao.resposta} for questao in questoes]

        return jsonify(questoes_json)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ----------------rotas

# questoes erradas
@app.route('/questoes_erradas', methods=["POST"])
def questoes_erradas():
    if request.method == "POST":
        return todas_as_questoes_erradas()
    
@app.route('/deletar_questoes_erradas', methods=["POST"])
def deletar_questoes_erradas():
    return deletar_questao(QuestoesErradas)

@app.route('/get_questoes_erradas', methods=["GET"])
def get_questoes_erradas():
    return buscar_perguntas(QuestoesErradas)


# fundamentos de programação
@app.route('/fundamentos_de_programacao', methods=["POST"])
def fundamentos_de_programacao():
    return cadastrar_pergunta(MateriaFundamentosDeProgramacao)

@app.route('/questoes_fundamentos_de_programacao', methods=["GET"])
def get_questoes_fundamentos():
    return buscar_perguntas(MateriaFundamentosDeProgramacao)

@app.route('/deletar_questao_fp', methods =["POST"])
def deletar_questao_route():
    return deletar_questao(MateriaFundamentosDeProgramacao)


# fundamentos de banco de dados
@app.route('/fundamentos_de_banco_de_dados', methods=["POST"])
def fundamentos_de_banco_de_dados():
    return cadastrar_pergunta(MateriaFundamentosDeBancoDeDados)

@app.route('/questoes_fundamentos_de_banco_de_dados', methods=["GET"])
def get_questoes_fbd():
    return buscar_perguntas(MateriaFundamentosDeBancoDeDados)

@app.route('/deletar_questao_fbd', methods=["POST"])
def deletar_questao_fbd():
    return deletar_questao(MateriaFundamentosDeBancoDeDados)

# engenharia de software
@app.route('/engenharia_de_software', methods=["POST"])
def engenharia_de_software():
    return cadastrar_pergunta(MateriaEngenhariaDeSoftware)

@app.route('/questoes_engenharia_de_software', methods=["GET"])
def get_questoes_eng_soft():
    return buscar_perguntas(MateriaEngenhariaDeSoftware)

@app.route('/deletar_questao_engsoftw', methods=["POST"])
def deletar_questa_eng_softw():
    return deletar_questao(MateriaEngenhariaDeSoftware)

# redes
@app.route('/redes', methods=["POST"])
def redes():
    return cadastrar_pergunta(MateriaRedes)

@app.route('/questoes_redes', methods=["GET"])
def get_questoes_redes():
    return buscar_perguntas(MateriaRedes)

@app.route('/deletar_questao_redes', methods=["POST"])
def deletar_questao_redes():
    return deletar_questao(MateriaRedes)

# sistemas operacionais
@app.route('/sistemas_operacionais', methods=["POST"])
def sistemas_operacionais():
    return cadastrar_pergunta(MateriaSistemasOperacionais)

@app.route('/questoes_sistemas_operacionais')
def get_questoes_so():
    return buscar_perguntas(MateriaSistemasOperacionais)

@app.route('/deletar_questao_so', methods=["POST"])
def deletar_questao_so():
    return deletar_questao(MateriaSistemasOperacionais)