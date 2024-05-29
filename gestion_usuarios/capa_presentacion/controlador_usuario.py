from gestion_usuarios.capa_negocio.servicio_usuario import ServicioUsuario

class ControladorUsuario:
    def __init__(self):
        self.servicio_usuario = ServicioUsuario()

    def agregar_usuario(self, id, nombre, correo_electronico):
        self.servicio_usuario.agregar_usuario(id, nombre, correo_electronico)

    def ver_usuario(self, id):
        usuario = self.servicio_usuario.obtener_usuario(id)
        if usuario:
            print("ID:", usuario.obtener_id())
            print("Nombre:", usuario.obtener_nombre())
            print("Correo electrónico:", usuario.obtener_correo_electronico())
        else:
            print("Usuario no encontrado.")

    def ver_todos_usuarios(self):
        todos_usuarios = self.servicio_usuario.obtener_todos_usuarios()
        for usuario in todos_usuarios:
            print("ID:", usuario.obtener_id())
            print("Nombre:", usuario.obtener_nombre())
            print("Correo electrónico:", usuario.obtener_correo_electronico())
            print("-----------------------------")
