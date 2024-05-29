class Usuario:
    def __init__(self, id, nombre, correo_electronico):
        self.id = id
        self.nombre = nombre
        self.correo_electronico = correo_electronico

    def obtener_id(self):
        return self.id

    def obtener_nombre(self):
        return self.nombre

    def obtener_correo_electronico(self):
        return self.correo_electronico
