from models.serie_models import Serie
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request


def get_series():
    series = Serie.query.all()
    
    if not series:  
        response = make_response(
            json.dumps({
                'mensagem': 'Nenhuma serie encontrada.',
                'dados': []  
            }, ensure_ascii=False, sort_keys=False)
        )
    else:
        response = make_response(
            json.dumps({
                'mensagem': 'Lista de séries.',
                'dados': [serie.json() for serie in series]
            }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
        )
    
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response

def get_serie_by_id(serie_id):
    serie = Serie.query.get(serie_id) 

    if serie: 
        response = make_response(
            json.dumps({
                'mensagem': 'Série encontrada.',
                'dados': serie.json() 
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que o tipo da resposta seja JSON
        return response
    else:
       
        response = make_response(
            json.dumps({'mensagem': 'Série não encontrada.', 'dados': {}}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response
    
def get_serie_by_titulo(serie_titulo):
    serie = Serie.query.filter_by(titulo=serie_titulo).first()  # Busca o Serie pelo nome

    if serie:
        response = make_response(
            json.dumps({
                'mensagem': 'Série encontrada.',
                'dados': serie.json()
            }, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps({
                'mensagem': 'Série não encontrada.',
                'dados': {}
            }, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response, 404



def create_serie(serie_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in serie_data for key in ['titulo', 'elenco', 'lancamento', 'genero']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Titulo, elenco, lancamento e genero são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    
    nova_serie = Serie(
        titulo=serie_data['titulo'],
        elenco=serie_data['elenco'],
        lancamento=serie_data['lancamento'],
        genero=serie_data['genero']
        )
    
    db.session.add(nova_serie) 
    db.session.commit()  # Confirma a transação no banco

    response = make_response(
        json.dumps({
            'mensagem': 'Série cadastrada com sucesso.',
            'serie': nova_serie.json() 
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response

def update_serie(serie_id, serie_data):
    serie = Serie.query.get(serie_id) 

    if not serie: 
        response = make_response(
            json.dumps({'mensagem': 'Série não encontrada.'}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response

    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in serie_data for key in ['titulo', 'elenco', 'lancamento', 'genero']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Titulo, elenco, lancamento e genero são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

    # Atualiza os dados do funcionário
    serie.titulo = serie_data['titulo']
    serie.elenco = serie_data['elenco']
    serie.lancamento = serie_data['lancamento']
    serie.genero = serie_data['genero']

    db.session.commit()  # Confirma a atualização no banco de dados

    response = make_response(
        json.dumps({
            'mensagem': 'Série atualizada com sucesso.',
            'serie': serie.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response

# Função para excluir um funcionário por ID com confirmação via parâmetro

def delete_serie(serie_id):
    confirmacao = request.args.get('confirmacao')  # Obtém o parâmetro de confirmação da URL

    if confirmacao != 'true':  # Se a confirmação não for enviada corretamente
        response = make_response(
            json.dumps({'mensagem': 'Confirmação necessária para excluir a série.'}, ensure_ascii=False),
            400  # Código HTTP 400 para "Requisição inválida"
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    serie = Serie.query.get(serie_id)  # Busca o funcionário pelo ID
    if not serie:  # Se o funcionário não for encontrado, retorna erro
        response = make_response(
            json.dumps({'mensagem': 'Série não encontrada.'}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    db.session.delete(serie)  # Remove o funcionário do banco de dados
    db.session.commit()  # Confirma a exclusão

    # Retorna a resposta com a mensagem de sucesso
    response = make_response(
        json.dumps({'mensagem': 'Série excluída com sucesso.'}, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response
