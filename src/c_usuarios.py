import os
import time

RUTA_USUARIOS = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "Usuarios.txt"
)

class c_usuarios:
    """
    Clase encargada de representar y gestionar los usuarios
    autorizados para ingresar al sistema PetGestor.
    """

    def __init__(self, usuario, nombre_completo, correo_institucional,
                 contrasena, rol, estado):
        # Datos básicos, completos y organizados del usuario.
        self.usuario = usuario
        self.nombre_completo = nombre_completo
        self.correo_institucional = correo_institucional
        self.contrasena = contrasena
        self.rol = rol
        self.estado = estado

    def mostrar_datos(self):
        """
        Método sencillo que permite consultar los datos
        principales del usuario autenticado.
        """
        print("\n" + "=" * 50)
        print("              USUARIO AUTENTICADO")
        print("=" * 50)
        print(f"Usuario: {self.usuario}")
        print(f"Nombre: {self.nombre_completo}")
        print(f"Correo: {self.correo_institucional}")
        print(f"Rol: {self.rol}")
        print(f"Estado: {self.estado}")
        print("=" * 50)


class GestorUsuarios:
    """
    Clase administradora, funcional y centralizada para leer
    los usuarios y realizar el proceso de autenticación.
    """

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.usuarios = []

    def cargar_usuarios(self):
        """
        Lee el archivo Usuarios.txt y convierte cada registro
        en un objeto de la clase c_usuarios.
        """

        self.usuarios = []

        if not os.path.exists(self.ruta_archivo):
            print("ERROR: No se encontró el archivo Usuarios.txt.")
            return False

        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        # Comprensión de listas: elimina líneas vacías y espacios.
        lineas = [linea.strip() for linea in lineas if linea.strip()]

        # La primera línea corresponde a los encabezados.
        datos = lineas[1:]

        for linea in datos:
            campos = linea.split("|")

            if len(campos) == 6:
                usuario = c_usuarios(
                    campos[0],
                    campos[1],
                    campos[2],
                    campos[3],
                    campos[4],
                    campos[5])

                self.usuarios.append(usuario)

        return True

    def buscar_usuario(self, identificador, contrasena):
        """
        Busca un usuario utilizando su nombre de usuario
        o su correo institucional y verifica la contraseña.
        """

        for usuario in self.usuarios:

            # Permite ingresar con usuario O correo institucional.
          
                identificador_correcto = (
                usuario.usuario == identificador
                or usuario.correo_institucional == identificador
            )

            contrasena_correcta = usuario.contrasena == contrasena

            if identificador_correcto and contrasena_correcta:

                # Solo se permite ingresar si el usuario está activo.
                if usuario.estado.lower() == "activo":
                    return usuario

                print("\nEl usuario existe, pero está inactivo.")
                return None

        return None

    def iniciar_sesion(self):
        """
        Ejecuta el proceso completo de autenticación.
        Se permiten máximo tres intentos incorrectos.
        """

        if not self.cargar_usuarios():
            return None

        maximo_intentos = 3
        intentos = 0
        tiempo_bloqueo = 30

        print("\n" + "=" * 60)
        print("                  PETGESTOR")
        print("              SISTEMA DE PQRS")
        print("=" * 60)

        while intentos < maximo_intentos:

            identificador = input(
                "\nUsuario o correo institucional: "
            ).strip()

            contrasena = input("Contraseña: ")

            usuario_autenticado = self.buscar_usuario(
                identificador,
                contrasena
            )

            if usuario_autenticado is not None:

                print("\n¡Inicio de sesión exitoso!")
                print(f"Bienvenido/a, {usuario_autenticado.nombre_completo}.")
                print(f"Rol: {usuario_autenticado.rol}")

                return usuario_autenticado

            intentos += 1
            intentos_restantes = maximo_intentos - intentos

            if intentos < maximo_intentos:
                print("\nCredenciales incorrectas.")
                print(
                    f"Intentos restantes: {intentos_restantes}"
                )

            else:
                print("\nSe alcanzó el máximo de 3 intentos fallidos.")
                print(
                    f"El sistema se bloqueará durante "
                    f"{tiempo_bloqueo} segundos."
                )

                for segundos in range(
                    tiempo_bloqueo, 0, -1
                ):
                    print(
                        f"\rPantalla bloqueada. "
                        f"Espere {segundos} segundos...",
                        end=""
                    )
                    time.sleep(1)

                print("\n\nBloqueo finalizado.")
                print("Debe iniciar nuevamente el proceso de Login.")

                return None

        return None

   if __name__ == "__main__":

    gestor = GestorUsuarios(RUTA_USUARIOS)

    usuario = gestor.iniciar_sesion()

    if usuario is not None:
        usuario.mostrar_datos()
