class DaoUsuario:
    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, usuario):
        self.usuarios[usuario.obtener_id()] = usuario

    def obtener_usuario(self, id):
        return self.usuarios.get(id)

    def obtener_todos_usuarios(self):
        return list(self.usuarios.values())
