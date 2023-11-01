from flask import Flask, request, jsonify
from sqlalchemy.orm import sessionmaker
from main import Session
from models.aeroclub import Usuarios, engine
from sqlalchemy import false
from app import app

# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    session = Session()
    usuarios = session.query(Usuarios).all()
    usuarios_lista = [{"id": usuario.id_usuarios, "nombre": usuario.nombre, "apellido": usuario.apellido} for usuario in usuarios]
    session.close()
    return jsonify(usuarios_lista)

# Obtener usuario por ID
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
       
# ¿Crear usuario es necesario?
''' @app.route('/usuarios', methods=['POST'])
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
        return "Datos de usuario no proporcionados", 400'''

# Ver detalles de usuario
@app.route('/usuarios/<int:id>/detalles', methods=['GET'])
def obtener_detalles_usuario(id):
    session = Session()
    usuario = session.query(Usuarios).filter(Usuarios.id_usuarios == id).first()
    if usuario:
        detalles_usuario = {
            "id": usuario.id_usuarios,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "email": usuario.email,
            "telefono": usuario.telefono,
            "dni": usuario.dni,
            "fecha_alta": usuario.fecha_alta,
            "fecha_baja": usuario.fecha_baja,
            "dirección": usuario.dirección,
            "foto_perfil": usuario.foto_perfil,
            "estados_id": usuario.estados_id
        }
        session.close()
        return jsonify(detalles_usuario)
    else:
        return "Usuario no encontrado", 404

# Modificar usuario 
@app.route('/usuarios/<int:id>/modificar', methods=['PUT'])
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

# Modificar ROL de usuario 
@app.route('/usuarios/<int:id>/modificar-rol', methods=['PUT'])
def modificar_rol_usuario(id):
    data = request.get_json()
    if data:
        session = Session()
        usuario = session.query(Usuarios).filter(Usuarios.id_usuarios == id).first()
        if usuario:
            # Modificar el rol del usuario según los datos proporcionados en JSON (por ejemplo, asumiendo que el rol es un campo "rol" en el JSON).
            if 'rol' in data:
                usuario.rol = data['rol']
            session.commit()
            session.close()
            return "Rol del usuario modificado satisfactoriamente"
        else:
            return "Usuario no encontrado", 404
    else:
        return "Datos de usuario no proporcionados", 400
   

# Eliminar usuario 
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    session = Session()
    usuario = session.query(Usuarios).filter(Usuarios.id_usuarios == id).first()
    if usuario:
        session.delete(usuario) # por el momento eliminamos, a futuro habría que ver deshabilitarlo en su lugar.
        session.commit()
        session.close()
        return "Usuario eliminado satisfactoriamente"
    else:
        return "Usuario no encontrado", 404
