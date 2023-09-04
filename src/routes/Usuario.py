from flask import Blueprint, jsonify, request

import uuid

# Entities
from models.entities.Usuario import Usuario

# Modelos
from models.UsuarioModel import UsuarioModel

main = Blueprint('usuario_blueprint', __name__)


@main.route('/')
def get_usuarios():
    try:
        usuarios = UsuarioModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# Obtener
@main.route('/<id>')
def get_usuario(id):
    try:
        usuario = UsuarioModel.get_usuario(id)
        if usuario != None:
            return jsonify(usuario)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# Agregar 
@main.route('/add', methods=['POST'])
def add_usuario():
    try:
        ci = request.json['ci']
        nombre = request.json['nombre']
        primer_ap = request.json['primer_ap']
        segundo_ap = request.json['segundo_ap']
        fecha_nac = request.json['fecha_nac']
        id = uuid.uuid4()
        usuario = Usuario(str(id), ci, nombre, primer_ap, segundo_ap, fecha_nac)
        affected_rows = UsuarioModel.add_usuario(usuario)
        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({"message": "Error al insertar"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# Eliminar    
@main.route('/delete/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuario(id)
        affected_rows = UsuarioModel.delete_usuario(usuario)
        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "Error al eliminar / O es que el usario no existe"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@main.route('/update/<id>', methods=['PUT'])
def update_usuario(id):
    try:
        ci = request.json['ci']
        nombre = request.json['nombre']
        primer_ap = request.json['primer_ap']
        segundo_ap = request.json['segundo_ap']
        fecha_nac = request.json['fecha_nac']
        usuario = Usuario(id, ci, nombre, primer_ap, segundo_ap, fecha_nac)

        affected_rows = UsuarioModel.update_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({"message": "Error al actualizar datos"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500