import os
from datetime import datetime

from c_usuarios import GestorUsuarios, RUTA_USUARIOS
from c_pqrs import c_pqrs
from archivos import c_archivos
from reportes import c_reportes

from validaciones import (
    validar_nombre,
    validar_documento,
    validar_correo,
    validar_telefono,
    calcular_fecha_maxima
)


# ============================================================
# RUTAS
# ============================================================

RUTA_DATA = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data"
)


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def pedir_dato(mensaje, funcion_validacion=None):
    """
    Solicita un dato al usuario y lo valida.
    """

    while True:

        dato = input(mensaje).strip()

        if funcion_validacion is None:
            return dato

        if funcion_validacion(dato):
            return dato

        print("Dato inválido. Intente nuevamente.")


def seleccionar_opcion(mensaje, opciones):
    """
    Muestra una lista de opciones y permite seleccionar una.
    """

    while True:

        print("\n" + mensaje)

        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")

        try:
            seleccion = int(
                input("Seleccione una opción: ")
            )

            if 1 <= seleccion <= len(opciones):
                return opciones[seleccion - 1]

            print("Seleccione una opción válida.")

        except ValueError:
            print("Debe ingresar un número.")


# ============================================================
# REGISTRAR PQRS
# ============================================================

def registrar_pqrs(usuario):
    """
    Registra una nueva PQRS.
    """

    archivos = c_archivos(RUTA_DATA)

    print("\n" + "=" * 60)
    print("                  REGISTRAR PQRS")
    print("=" * 60)

    tipo_solicitud = seleccionar_opcion(
        "Tipo de solicitud:",
        [
            "Petición",
            "Queja",
            "Reclamo",
            "Sugerencia"
        ]
    )

    print("\n--- DATOS DEL SOLICITANTE ---")

    nombre = pedir_dato(
        "Nombre completo: ",
        validar_nombre
    )

    tipo_documento = seleccionar_opcion(
        "Tipo de documento:",
        [
            "CC",
            "TI",
            "CE",
            "PP",
            "NIT"
        ]
    )

    numero_documento = pedir_dato(
        "Número de documento: ",
        validar_documento
    )

    tipo_telefono = seleccionar_opcion(
        "Tipo de teléfono:",
        [
            "Celular",
            "Fijo",
            "Corporativo",
            "Otro"
        ]
    )

    telefono = pedir_dato(
        "Teléfono de contacto: ",
        validar_telefono
    )

    correo = pedir_dato(
        "Correo electrónico: ",
        validar_correo
    )

    direccion = input(
        "Dirección: "
    ).strip()

    if direccion == "":
        direccion = "N/A"

    print("\n--- INFORMACIÓN DE LA PQRS ---")

    canal = seleccionar_opcion(
        "Canal de recepción:",
        [
            "Página web",
            "Correo electrónico",
            "Presencial",
            "Teléfono",
            "Redes sociales",
            "Otro"
        ]
    )

    asunto = pedir_dato(
        "Asunto o título: "
    )

    descripcion = pedir_dato(
        "Descripción detallada: "
    )

    tipo_mascota = seleccionar_opcion(
        "Tipo de mascota:",
        [
            "Perro",
            "Gato",
            "Otro"
        ]
    )

    campus = seleccionar_opcion(
        "Campus relacionado:",
        [
            "Campus Medellín - Ciudad Universitaria",
            "Campus Medellín - Ciudadela Robledo",
            "Campus en el Área de la salud",
            "Campus Medellín - Sede de Posgrado",
            "Campus Medellín - Edificio San Ignacio",
            "Campus Medellín - Antigua Escuela de Derecho",
            "Campus Medellín - Edificio Antioquia",
            "Campus Medellín - Casas Patrimoniales",
            "Campus Medellín - Edificio de Extensión",
            "Campus Medellín - Casas Patrimoniales"
        ]
    )

    # --------------------------------------------------------
    # FECHAS
    # --------------------------------------------------------

    fecha_actual = datetime.now()

    fecha_radicacion = fecha_actual.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    fecha_solo_dia = fecha_actual.strftime(
        "%d/%m/%Y"
    )

    fecha_maxima = calcular_fecha_maxima(
        fecha_solo_dia
    )

    # --------------------------------------------------------
    # ID CONSECUTIVO
    # --------------------------------------------------------

    identificador = archivos.obtener_siguiente_id(
        tipo_solicitud
    )

    # --------------------------------------------------------
    # CREAR OBJETO PQRS
    # --------------------------------------------------------

    nueva_pqrs = c_pqrs(
        identificador,
        nombre,
        tipo_documento,
        numero_documento,
        tipo_telefono,
        telefono,
        correo,
        direccion,
        tipo_solicitud,
        fecha_radicacion,
        canal,
        asunto,
        descripcion,
        tipo_mascota,
        campus,
        fecha_maxima,
        "Registrada",
        usuario.usuario
    )

    # --------------------------------------------------------
    # GUARDAR
    # --------------------------------------------------------

    archivos.guardar_registro(
        tipo_solicitud,
        nueva_pqrs.convertir_a_diccionario()
    )

    print("\n" + "=" * 60)
    print("          PQRS REGISTRADA EXITOSAMENTE")
    print("=" * 60)
    print(f"Tipo de solicitud: {tipo_solicitud}")
    print(f"ID asignado: {identificador}")
    print(f"Estado: Registrada")
    print(f"Fecha de radicación: {fecha_radicacion}")
    print(f"Fecha máxima de respuesta: {fecha_maxima}")
    print(f"Usuario registrador: {usuario.usuario}")
    print("=" * 60)


# ============================================================
# CONSULTAR PQRS
# ============================================================

def consultar_pqrs():
    """
    Permite consultar todas las PQRS de un tipo determinado.
    """

    archivos = c_archivos(RUTA_DATA)

    print("\n" + "=" * 60)
    print("                  CONSULTAR PQRS")
    print("=" * 60)

    tipo_solicitud = seleccionar_opcion(
        "Seleccione el tipo de PQRS:",
        [
            "Petición",
            "Queja",
            "Reclamo",
            "Sugerencia"
        ]
    )

    registros = archivos.leer_archivo(
        tipo_solicitud
    )

    if not registros:

        print("\nNo existen registros para este tipo de PQRS.")
        return

    print("\n" + "=" * 60)
    print(
        f"        REGISTROS DE {tipo_solicitud.upper()}"
    )
    print("=" * 60)

    for registro in registros:

        print(
            f"\nID: {registro.get('id', '')}"
        )

        print(
            f"Nombre: "
            f"{registro.get('nombre_completo', '')}"
        )

        print(
            f"Documento: "
            f"{registro.get('tipo_documento', '')} "
            f"{registro.get('numero_documento', '')}"
        )

        print(
            f"Tipo de solicitud: "
            f"{registro.get('tipo_solicitud', '')}"
        )

        print(
            f"Fecha de radicación: "
            f"{registro.get('fecha_radicacion', '')}"
        )

        print(
            f"Estado: "
            f"{registro.get('estado_peticion', '')}"
        )

        print(
            f"Fecha máxima de respuesta: "
            f"{registro.get('fecha_maxima_respuesta', '')}"
        )

        print("-" * 60)


# ============================================================
# CONSULTAR PQRS POR ID
# ============================================================

def consultar_pqrs_por_id():
    """
    Consulta una PQRS específica mediante su ID.
    """

    archivos = c_archivos(RUTA_DATA)

    print("\n" + "=" * 60)
    print("             CONSULTAR PQRS POR ID")
    print("=" * 60)

    tipo_solicitud = seleccionar_opcion(
        "Seleccione el tipo de PQRS:",
        [
            "Petición",
            "Queja",
            "Reclamo",
            "Sugerencia"
        ]
    )

    identificador = input(
        "Ingrese el ID de la PQRS: "
    ).strip()

    registro = archivos.buscar_por_id(
        tipo_solicitud,
        identificador
    )

    if registro is None:

        print("\nNo se encontró una PQRS con ese ID.")
        return

    print("\n" + "=" * 60)
    print("                 PQRS ENCONTRADA")
    print("=" * 60)

    print(
        f"ID: {registro.get('id', '')}"
    )

    print(
        f"Nombre completo: "
        f"{registro.get('nombre_completo', '')}"
    )

    print(
        f"Tipo de documento: "
        f"{registro.get('tipo_documento', '')}"
    )

    print(
        f"Número de documento: "
        f"{registro.get('numero_documento', '')}"
    )

    print(
        f"Tipo de teléfono: "
        f"{registro.get('tipo_telefono', '')}"
    )

    print(
        f"Teléfono: "
        f"{registro.get('telefono_contacto', '')}"
    )

    print(
        f"Correo: "
        f"{registro.get('correo_electronico', '')}"
    )

    print(
        f"Dirección: "
        f"{registro.get('direccion', '')}"
    )

    print(
        f"Tipo de solicitud: "
        f"{registro.get('tipo_solicitud', '')}"
    )

    print(
        f"Fecha de radicación: "
        f"{registro.get('fecha_radicacion', '')}"
    )

    print(
        f"Canal: "
        f"{registro.get('canal_recepcion', '')}"
    )

    print(
        f"Asunto: "
        f"{registro.get('asunto_titulo', '')}"
    )

    print(
        f"Descripción: "
        f"{registro.get('descripcion_detallada', '')}"
    )

    print(
        f"Tipo de mascota: "
        f"{registro.get('tipo_mascota', '')}"
    )

    print(
        f"Campus: "
        f"{registro.get('campus_relacionado', '')}"
    )

    print(
        f"Fecha máxima de respuesta: "
        f"{registro.get('fecha_maxima_respuesta', '')}"
    )

    print(
        f"Estado: "
        f"{registro.get('estado_peticion', '')}"
    )

    print(
        f"Usuario registrador: "
        f"{registro.get('usuario_registro', '')}"
    )

    print("=" * 60)


# ============================================================
# CAMBIAR ESTADO
# ============================================================

def cambiar_estado_pqrs():
    """
    Permite cambiar el estado de una PQRS.

    Flujo permitido:
    Registrada -> En proceso -> Solucionada
    """

    archivos = c_archivos(RUTA_DATA)

    print("\n" + "=" * 60)
    print("              CAMBIAR ESTADO DE PQRS")
    print("=" * 60)

    tipo_solicitud = seleccionar_opcion(
        "Seleccione el tipo de PQRS:",
        [
            "Petición",
            "Queja",
            "Reclamo",
            "Sugerencia"
        ]
    )

    identificador = input(
        "Ingrese el ID de la PQRS: "
    ).strip()

    registro = archivos.buscar_por_id(
        tipo_solicitud,
        identificador
    )

    if registro is None:

        print("\nNo se encontró la PQRS.")
        return

    estado_actual = registro.get(
        "estado_peticion",
        "Registrada"
    )

    print(
        f"\nEstado actual: {estado_actual}"
    )

    if estado_actual == "Registrada":

        nuevo_estado = "En proceso"

    elif estado_actual == "En proceso":

        nuevo_estado = "Solucionada"

    else:

        print(
            "\nLa PQRS ya está solucionada."
        )
        return

    print(
        f"Nuevo estado: {nuevo_estado}"
    )

    confirmar = input(
        "¿Desea realizar el cambio? (S/N): "
    ).strip().upper()

    if confirmar != "S":

        print("\nOperación cancelada.")
        return

    ruta = archivos.obtener_ruta(
        tipo_solicitud
    )

    with open(
        ruta,
        "r",
        encoding="utf-8"
    ) as archivo:

        lineas = archivo.readlines()

    encabezado = lineas[0]

    nuevas_lineas = [encabezado]

    for linea in lineas[1:]:

        campos = linea.rstrip("\n").split("|")

        if len(campos) > 16 and campos[0] == identificador:

            campos[16] = nuevo_estado

            linea = "|".join(campos) + "\n"

        nuevas_lineas.append(linea)

    with open(
        ruta,
        "w",
        encoding="utf-8"
    ) as archivo:

        archivo.writelines(nuevas_lineas)

    print("\nEstado actualizado correctamente.")
    print(
        f"Estado anterior: {estado_actual}"
    )
    print(
        f"Nuevo estado: {nuevo_estado}"
    )


# ============================================================
# GENERAR RADICADO
# ============================================================

def generar_radicado():
    """
    Genera e imprime un radicado con ancho fijo de 120 caracteres.
    """

    archivos = c_archivos(RUTA_DATA)

    ANCHO = 120

    print("\n" + "=" * ANCHO)
    print(
        "                    GENERAR RADICADO"
    )
    print("=" * ANCHO)

    tipo_solicitud = seleccionar_opcion(
        "Seleccione el tipo de PQRS:",
        [
            "Petición",
            "Queja",
            "Reclamo",
            "Sugerencia"
        ]
    )

    identificador = input(
        "Ingrese el ID de la PQRS: "
    ).strip()

    registro = archivos.buscar_por_id(
        tipo_solicitud,
        identificador
    )

    if registro is None:

        print("\nNo se encontró la PQRS.")
        return

    def linea(texto=""):

        texto = str(texto)

        espacio = ANCHO - 4

        if len(texto) > espacio:
            texto = texto[:espacio]

        return (
            "| "
            + texto.center(espacio)
            + " |"
        )

    print("+" + "-" * (ANCHO - 2) + "+")

    print(
        linea("PETGESTOR - SISTEMA DE PQRS")
    )

    print(
        linea("RADICADO")
    )

    print(
        linea("")
    )

    print(
        linea(
            f"Tipo de solicitud: "
            f"{registro.get('tipo_solicitud', '')}"
        )
    )

    print(
        linea(
            f"ID: {registro.get('id', '')}"
        )
    )

    print(
        linea(
            "Fecha y hora de generación: "
            + datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
    )

    print(
        linea(
            f"Fecha de radicación: "
            f"{registro.get('fecha_radicacion', '')}"
        )
    )

    print(
        linea(
            f"Estado inicial: "
            f"{registro.get('estado_peticion', '')}"
        )
    )

    print(
        linea(
            f"Fecha máxima de respuesta: "
            f"{registro.get('fecha_maxima_respuesta', '')}"
        )
    )

    print(
        linea("")
    )

    print(
        linea("DATOS DEL SOLICITANTE")
    )

    print(
        linea(
            f"Nombre: "
            f"{registro.get('nombre_completo', '')}"
        )
    )

    print(
        linea(
            f"Documento: "
            f"{registro.get('tipo_documento', '')} "
            f"{registro.get('numero_documento', '')}"
        )
    )

    print(
        linea(
            f"Teléfono: "
            f"{registro.get('telefono_contacto', '')}"
        )
    )

    print(
        linea(
            f"Correo: "
            f"{registro.get('correo_electronico', '')}"
        )
    )

    print(
        linea(
            f"Dirección: "
            f"{registro.get('direccion', 'N/A')}"
        )
    )

    print(
        linea("")
    )

    print(
        linea("CLASIFICACIÓN")
    )

    print(
        linea(
            f"Tipo de mascota: "
            f"{registro.get('tipo_mascota', '')}"
        )
    )

    print(
        linea(
            f"Campus: "
            f"{registro.get('campus_relacionado', '')}"
        )
    )

    print(
        linea(
            f"Canal: "
            f"{registro.get('canal_recepcion', '')}"
        )
    )

    print(
        linea(
            f"Asunto: "
            f"{registro.get('asunto_titulo', '')}"
        )
    )

    print(
        linea("")
    )

    print(
        linea(
            "Documento generado por PetGestor"
        )
    )

    print(
        "+" + "-" * (ANCHO - 2) + "+"
    )


# ============================================================
# MOSTRAR MENÚ
# ============================================================

def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """

    print("\n" + "=" * 60)
    print("                    PETGESTOR")
    print("              SISTEMA DE GESTIÓN PQRS")
    print("=" * 60)

    print("1. Registrar PQRS")
    print("2. Consultar PQRS")
    print("3. Consultar PQRS por radicado")
    print("4. Cambiar estado de PQRS")
    print("5. Generar radicado")
    print("6. Generar estadísticas")
    print("7. Ver información del usuario")
    print("8. Salir")

    print("=" * 60)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    """
    Función principal de PetGestor.
    """

    gestor_usuarios = GestorUsuarios(
        RUTA_USUARIOS
    )

    usuario = gestor_usuarios.iniciar_sesion()

    if usuario is None:

        print(
            "\nNo fue posible iniciar sesión."
        )

        return

    archivos = c_archivos(
        RUTA_DATA
    )

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "1":

            registrar_pqrs(
                usuario
            )

        elif opcion == "2":

            consultar_pqrs()

        elif opcion == "3":

            consultar_pqrs_por_id()

        elif opcion == "4":

            cambiar_estado_pqrs()

        elif opcion == "5":

            generar_radicado()

        elif opcion == "6":

            reportes = c_reportes(
                RUTA_DATA
            )

            reportes.mostrar_reportes()

        elif opcion == "7":

            usuario.mostrar_datos()

        elif opcion == "8":

            print(
                "\nGracias por utilizar PetGestor."
            )

            print(
                "Sesión finalizada correctamente."
            )

            break

        else:

            print(
                "\nOpción inválida."
            )

        input(
            "\nPresione ENTER para continuar..."
        )


# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":

    main()