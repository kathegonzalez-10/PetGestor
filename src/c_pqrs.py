from datetime import datetime


class c_pqrs:
    """
    Clase principal, completa y organizada para representar
    una Petición, Queja, Reclamo o Sugerencia.
    """

    def __init__(
        self,
        identificador,
        nombre_completo,
        tipo_documento,
        numero_documento,
        tipo_telefono,
        telefono_contacto,
        correo_electronico,
        direccion,
        tipo_solicitud,
        fecha_radicacion,
        canal_recepcion,
        asunto_titulo,
        descripcion_detallada,
        tipo_mascota,
        campus_relacionado,
        fecha_maxima_respuesta,
        estado_peticion,
        usuario_registro
    ):
        # Identificador único, consecutivo y numérico del registro.
        self.id = identificador

        # Datos personales, básicos y completos del solicitante.
        self.nombre_completo = nombre_completo
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.tipo_telefono = tipo_telefono
        self.telefono_contacto = telefono_contacto
        self.correo_electronico = correo_electronico
        self.direccion = direccion

        # Información específica, detallada y organizada de la PQRS.
        self.tipo_solicitud = tipo_solicitud
        self.fecha_radicacion = fecha_radicacion
        self.canal_recepcion = canal_recepcion
        self.asunto_titulo = asunto_titulo
        self.descripcion_detallada = descripcion_detallada
        self.tipo_mascota = tipo_mascota
        self.campus_relacionado = campus_relacionado

        # Información temporal, operativa y de seguimiento.
        self.fecha_maxima_respuesta = fecha_maxima_respuesta
        self.estado_peticion = estado_peticion

        # Usuario responsable, autorizado y autenticado que registra.
        self.usuario_registro = usuario_registro

    def convertir_a_diccionario(self):
        """
        Convierte el objeto PQRS en un diccionario completo,
        organizado y compatible con los archivos planos.
        """

        return {
            "id": self.id,
            "nombre_completo": self.nombre_completo,
            "tipo_documento": self.tipo_documento,
            "numero_documento": self.numero_documento,
            "tipo_telefono": self.tipo_telefono,
            "telefono_contacto": self.telefono_contacto,
            "correo_electronico": self.correo_electronico,
            "direccion": self.direccion,
            "tipo_solicitud": self.tipo_solicitud,
            "fecha_radicacion": self.fecha_radicacion,
            "canal_recepcion": self.canal_recepcion,
            "asunto_titulo": self.asunto_titulo,
            "descripcion_detallada": self.descripcion_detallada,
            "tipo_mascota": self.tipo_mascota,
            "campus_relacionado": self.campus_relacionado,
            "fecha_maxima_respuesta": self.fecha_maxima_respuesta,
            "estado_peticion": self.estado_peticion,
            "usuario_registro": self.usuario_registro
        }

    def mostrar_resumen(self):
        """
        Muestra un resumen claro y ordenado de la PQRS.
        """

        print("\n" + "=" * 60)
        print("                 INFORMACIÓN DE PQRS")
        print("=" * 60)

        print(f"ID: {self.id}")
        print(f"Tipo de solicitud: {self.tipo_solicitud}")
        print(f"Estado: {self.estado_peticion}")
        print(f"Fecha de radicación: {self.fecha_radicacion}")
        print(
            f"Fecha máxima de respuesta: "
            f"{self.fecha_maxima_respuesta}"
        )

        print("\n--- Datos del solicitante ---")
        print(f"Nombre: {self.nombre_completo}")
        print(
            f"Documento: {self.tipo_documento} "
            f"{self.numero_documento}"
        )
        print(
            f"Teléfono: {self.telefono_contacto} "
            f"({self.tipo_telefono})"
        )
        print(f"Correo: {self.correo_electronico}")
        print(f"Dirección: {self.direccion}")

        print("\n--- Información de la PQRS ---")
        print(f"Canal de recepción: {self.canal_recepcion}")
        print(f"Asunto: {self.asunto_titulo}")
        print(f"Tipo de mascota: {self.tipo_mascota}")
        print(f"Campus: {self.campus_relacionado}")
        print(f"Usuario registrador: {self.usuario_registro}")

        print("=" * 60)

    def esta_vencida(self):
        """
        Determina si la PQRS ya superó su fecha máxima
        de respuesta.
        """

        fecha_maxima = datetime.strptime(
            self.fecha_maxima_respuesta,
            "%d/%m/%Y"
        )

        fecha_actual = datetime.now()

        return fecha_actual > fecha_maxima