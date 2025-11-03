from flask import Blueprint, request 
from controllers.serie_controllers import (
    get_series,
    get_serie_by_id,
    get_serie_by_titulo,
    create_serie,
    update_serie,
    delete_serie
)

serie_routes = Blueprint('serie_routes', __name__)  

# Rota para listar todos as series (GET)
@serie_routes.route('/Serie', methods=['GET'])
def series_get():
    return get_series()

# Rota para buscar um funcionário pelo ID (GET)
@serie_routes.route('/Serie/<int:serie_id>', methods=['GET'])
def serie_get_by_id(serie_id):
    return get_serie_by_id(serie_id)

@serie_routes.route('/Serie/<string:serie_titulo>', methods=['GET'])  # Alterado para consulta por nome
def serie_get_by_titulo(serie_titulo):  # Alterado para buscar por nome
    return get_serie_by_titulo(serie_titulo)  # Alterado para chamar a função que usa o nome


# Rota para criar um novo funcionário (POST)
@serie_routes.route('/Serie', methods=['POST'])
def series_post():
    return create_serie(request.json)

# Rota para atualizar um funcionário pelo ID (PUT)
@serie_routes.route('/Serie/<int:serie_id>', methods=['PUT'])
def series_put(serie_id):
    return update_serie(serie_id, request.json)

# Rota para excluir um funcionário pelo ID (DELETE)
@serie_routes.route('/Serie/<int:serie_id>', methods=['DELETE'])
def serie_delete(serie_id):
    return delete_serie(serie_id)
