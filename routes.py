from flask import Flask, request, jsonify
from sqlalchemy.orm import sessionmaker
from main import Session
from modela.aeroclub import Usuarios, engine
from sqlalchemy import false
from app import app

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    session = Session()
    usuarios = session.query(Usuarios).all()
    usuarios_lista = [{"id": usuario.id_usuarios, "nombre": usuario.nombre, "apellido": usuario.apellido} for usuario in usuarios]
    session.close()
    return jsonify(usuarios_lista)

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    session = Session()
    usuario = session.query(Usuarios).filter(Usuarios.id_usuarios == id).first()
    if usuario:
        usuario_dict = {
            "id": usuario.id_usuarios,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "email": usuario.email
        }
        session.close()
        return jsonify(usuario_dict)
    else:
        return "Usuario no encontrado", 404

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    if data:
        nuevo_usuario = Usuarios(
            nombre=data['nombre'],
            apellido=data['apellido'],
            email=data['email'],
            telefono=data['telefono'],
            dni=data['dni'],
            fecha_alta=data['fecha_alta'],
            fecha_baja=data['fecha_baja'],
            dirección=data['dirección'],
            foto_perfil=data['foto_perfil'],
            estados_id=data['estados_id']
        )
        session = Session()
        session.add(nuevo_usuario)
        session.commit()
        session.close()
        return "Usuario creado satisfactoriamente", 201
    else:
        return "Datos de usuario no proporcionados", 400

@app.route('/usuarios/<int:id>', methods=['PUT'])
def modificar_usuario(id):
    data = request.get_json()
    if data:
        session = Session()
        usuario = session.query(Usuarios).filter(Usuarios.id_usuarios == id).first()
        if usuario:
            usuario.nombre = data['nombre']
            usuario.apellido = data['apellido']
            usuario.email = data['email']
            usuario.telefono = data['telefono']
            usuario.dni = data['dni']
            usuario.fecha_alta = data['fecha_alta']
            usuario.fecha_baja = data['fecha_baja']
            usuario.dirección = data['dirección']
            usuario.foto_perfil = data['foto_perfil']
            usuario.estados_id = data['estados_id']
            session.commit()
            session.close()
            return "Usuario modificado satisfactoriamente"
        else:
            return "Usuario no encontrado", 404
    else:
        return "Datos de usuario no proporcionados", 400

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    session = Session()
    usuario = session.query(Usuarios).filter(Usuarios.id_usuarios == id).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        session.close()
        return "Usuario eliminado satisfactoriamente"
    else:
        return "Usuario no encontrado", 404
