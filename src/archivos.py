import os


class c_archivos:
    """
    Clase encargada de gestionar de manera organizada,
    centralizada y segura los archivos planos de PetGestor.
    """

    ENCABEZADO = (
        "id|nombre_completo|tipo_documento|numero_documento|"
        "tipo_telefono|telefono_contacto|correo_electronico|direccion|"
        "tipo_solicitud|fecha_radicacion|canal_recepcion|asunto_titulo|"
        "descripcion_detallada|tipo_mascota|campus_relacionado|"
        "fecha_maxima_respuesta|estado_peticion|usuario_registro|""fecha_respuesta"
    )

    def __init__(self, carpeta_data):
        """
        Inicializa la clase con la ruta de la carpeta data.
        """

        self.carpeta_data = carpeta_data
        self.actualizar_estructura()

    def actualizar_estructura(self):
        """
        Agrega el campo fecha_respuesta a los archivos existentes
        sin eliminar la información registrada.
        """

        nombres_archivos = [
            "Peticion.txt",
            "Queja.txt",
            "Reclamo.txt",
            "Sugerencia.txt"
        ]

        for nombre in nombres_archivos:

            ruta = os.path.join(
                self.carpeta_data,
                nombre
            )

            if not os.path.exists(ruta):
                continue

            with open(ruta, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()

            if not lineas:
                continue

            encabezados = lineas[0].strip().split("|")

            if "fecha_respuesta" in encabezados:
                continue

            encabezados.append("fecha_respuesta")

            nuevas_lineas = [
                "|".join(encabezados) + "\n"
            ]

            for linea in lineas[1:]:

                if not linea.strip():
                    continue

                campos = linea.rstrip("\n").split("|")

                while len(campos) < len(encabezados):
                    campos.append("")

                nuevas_lineas.append(
                    "|".join(campos) + "\n"
                )

            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.writelines(nuevas_lineas)    

    def obtener_ruta(self, tipo_solicitud):
        """
        Obtiene de manera automática el archivo correspondiente
        al tipo de PQRS seleccionado.
        """

        archivos = {
            "Petición": "Peticion.txt",
            "Queja": "Queja.txt",
            "Reclamo": "Reclamo.txt",
            "Sugerencia": "Sugerencia.txt"
        }

        return os.path.join(
            self.carpeta_data,
            archivos[tipo_solicitud]
        )

    def leer_archivo(self, tipo_solicitud):
        """
        Lee todos los registros del archivo correspondiente
        y los convierte en una lista de diccionarios.
        """

        ruta = self.obtener_ruta(tipo_solicitud)

        if not os.path.exists(ruta):
            return []

        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        lineas = [
            linea.strip()
            for linea in lineas
            if linea.strip()
        ]

        if len(lineas) <= 1:
            return []

        encabezados = lineas[0].split("|")

        registros = [
            dict(zip(encabezados, linea.split("|")))
            for linea in lineas[1:]
        ]

        return registros

    def obtener_siguiente_id(self, tipo_solicitud):
        """
        Obtiene el siguiente identificador disponible.
        Cada archivo mantiene su propia secuencia independiente.
        """

        registros = self.leer_archivo(tipo_solicitud)

        if not registros:
            return 1

        ids = [
            int(registro["id"])
            for registro in registros
            if registro.get("id", "").isdigit()
        ]

        if not ids:
            return 1

        return max(ids) + 1

    def guardar_registro(self, tipo_solicitud, registro):
        """
        Guarda un nuevo registro en el archivo correspondiente.
        """

        ruta = self.obtener_ruta(tipo_solicitud)

        archivo_existe = os.path.exists(ruta)

        with open(ruta, "a", encoding="utf-8") as archivo:

            if not archivo_existe or os.path.getsize(ruta) == 0:
                archivo.write(self.ENCABEZADO + "\n")

            valores = [
                str(registro.get("id", "")),
                str(registro.get("nombre_completo", "")),
                str(registro.get("tipo_documento", "")),
                str(registro.get("numero_documento", "")),
                str(registro.get("tipo_telefono", "")),
                str(registro.get("telefono_contacto", "")),
                str(registro.get("correo_electronico", "")),
                str(registro.get("direccion", "N/A")),
                str(registro.get("tipo_solicitud", "")),
                str(registro.get("fecha_radicacion", "")),
                str(registro.get("canal_recepcion", "")),
                str(registro.get("asunto_titulo", "")),
                str(registro.get("descripcion_detallada", "")),
                str(registro.get("tipo_mascota", "")),
                str(registro.get("campus_relacionado", "")),
                str(registro.get("fecha_maxima_respuesta", "")),
                str(registro.get("estado_peticion", "Registrada")),
                str(registro.get("usuario_registro", "")),
                str(registro.get("fecha_respuesta",""))
            ]

            archivo.write("|".join(valores) + "\n")

    def buscar_por_id(self, tipo_solicitud, identificador):
        """
        Busca una PQRS específica mediante su identificador.
        """

        registros = self.leer_archivo(tipo_solicitud)

        for registro in registros:

            if registro.get("id") == str(identificador):
                return registro

        return None

    def contar_registros(self, tipo_solicitud):
        """
        Cuenta la cantidad de registros existentes
        en un archivo específico.
        """

        return len(self.leer_archivo(tipo_solicitud))