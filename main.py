from gestion_usuarios.capa_presentacion.controlador_usuario import ControladorUsuario

def main():
    controlador_usuario = ControladorUsuario()
    controlador_usuario.agregar_usuario("1", "Mairon", "mairon@example.com")
    controlador_usuario.ver_todos_usuarios()

if __name__ == "__main__":
    main()
