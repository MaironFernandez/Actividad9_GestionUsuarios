from gestion_usuarios.capa_datos.dao_usuario import DaoUsuario
from gestion_usuarios.modelos.usuario import Usuario

class ServicioUsuario:
    def __init__(self):
        self.dao_usuario = DaoUsuario()

    def agregar_usuario(self, id, nombre, correo_electronico):
        nuevo_usuario = Usuario(id, nombre, correo_electronico)
        self.dao_usuario.agregar_usuario(nuevo_usuario)

    def obtener_usuario(self, id):
        return self.dao_usuario.obtener_usuario(id)

    def obtener_todos_usuarios(self):
        return self.dao_usuario.obtener_todos_usuarios()
