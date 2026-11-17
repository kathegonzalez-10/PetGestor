from datetime import datetime
from archivos import c_archivos


class c_reportes:
    """
    Clase encargada de generar reportes y estadísticas
    de las PQRS de PetGestor.
    """

    def __init__(self, carpeta_data):
        self.archivos = c_archivos(carpeta_data)
        self.registros = []

    # ========================================================
    # CARGAR REGISTROS
    # ========================================================

    def cargar_registros(self):
        """
        Carga los registros de los cuatro archivos planos.
        """

        self.registros = []

        tipos = [
            "Petición",
            "Queja",
            "Reclamo",
            "Sugerencia"
        ]

        for tipo in tipos:

            registros = self.archivos.leer_archivo(tipo)

            self.registros.extend(registros)

        return self.registros

    # ========================================================
    # CONVERTIR FECHAS
    # ========================================================

    def convertir_fecha(self, fecha):
        """
        Convierte una fecha almacenada en los archivos
        a un objeto datetime.

        Se aceptan los formatos utilizados por PetGestor.
        """

        if not fecha:
            return None

        formatos = [
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%d/%m/%Y %H:%M:%S"
        ]

        for formato in formatos:

            try:

                return datetime.strptime(
                    fecha,
                    formato
                )

            except ValueError:
                continue

        return None

    # ========================================================
    # TOTAL DE PQRS
    # ========================================================

    def total_pqrs(self):
        """
        Calcula el número total de PQRS registradas.
        """

        return len(self.registros)

    # ========================================================
    # DISTRIBUCIÓN POR MASCOTA
    # ========================================================

    def distribucion_mascotas(self):
        """
        Calcula la distribución de PQRS
        según el tipo de mascota.
        """

        resultado = {}

        for registro in self.registros:

            mascota = registro.get(
                "tipo_mascota",
                "No registrado"
            )

            resultado[mascota] = (
                resultado.get(mascota, 0) + 1
            )

        return resultado

    # ========================================================
    # DISTRIBUCIÓN POR CANAL
    # ========================================================

    def distribucion_canales(self):
        """
        Calcula la distribución de PQRS
        según el canal de recepción.
        """

        resultado = {}

        for registro in self.registros:

            canal = registro.get(
                "canal_recepcion",
                "No registrado"
            )

            resultado[canal] = (
                resultado.get(canal, 0) + 1
            )

        return resultado

    # ========================================================
    # DISTRIBUCIÓN POR CAMPUS
    # ========================================================

    def distribucion_campus(self):
        """
        Calcula la distribución de PQRS
        según el campus relacionado.
        """

        resultado = {}

        for registro in self.registros:

            campus = registro.get(
                "campus_relacionado",
                "No registrado"
            )

            resultado[campus] = (
                resultado.get(campus, 0) + 1
            )

        return resultado

    # ========================================================
    # DISTRIBUCIÓN POR TIPO DE SOLICITUD
    # ========================================================

    def distribucion_tipo_solicitud(self):
        """
        Calcula la cantidad de PQRS
        según su clasificación.
        """

        resultado = {}

        for registro in self.registros:

            tipo = registro.get(
                "tipo_solicitud",
                "No registrado"
            )

            resultado[tipo] = (
                resultado.get(tipo, 0) + 1
            )

        return resultado

    # ========================================================
    # DISTRIBUCIÓN POR ESTADO
    # ========================================================

    def distribucion_estados(self):
        """
        Calcula la cantidad de PQRS
        según su estado actual.
        """

        resultado = {}

        for registro in self.registros:

            estado = registro.get(
                "estado_peticion",
                "No registrado"
            )

            resultado[estado] = (
                resultado.get(estado, 0) + 1
            )

        return resultado

    # ========================================================
    # PQRS MÁS ANTIGUAS
    # ========================================================

    def pqrs_mas_antiguas(self):
        """
        Identifica las PQRS con las fechas
        de radicación más antiguas.
        """

        fechas_validas = []

        for registro in self.registros:

            fecha = self.convertir_fecha(
                registro.get("fecha_radicacion", "")
            )

            if fecha is not None:

                fechas_validas.append(
                    (fecha, registro)
                )

        if not fechas_validas:
            return []

        fecha_mas_antigua = min(
            fecha
            for fecha, registro in fechas_validas
        )

        resultado = [
            registro
            for fecha, registro in fechas_validas
            if fecha == fecha_mas_antigua
        ]

        return resultado

    # ========================================================
    # PQRS PRÓXIMAS A VENCER
    # ========================================================

    def pqrs_proximas_vencer(self, dias=5):
        """
        Identifica las PQRS cuya fecha máxima de respuesta
        está próxima a vencer.
        """

        fecha_actual = datetime.now()

        resultado = []

        for registro in self.registros:

            estado = registro.get(
                "estado_peticion",
                ""
            )

            if estado == "Solucionada":
                continue

            fecha_maxima = self.convertir_fecha(
                registro.get(
                    "fecha_maxima_respuesta",
                    ""
                )
            )

            if fecha_maxima is None:
                continue

            diferencia = (
                fecha_maxima - fecha_actual
            ).days

            if 0 <= diferencia <= dias:

                resultado.append(
                    {
                        "registro": registro,
                        "dias_restantes": diferencia
                    }
                )

        return resultado

    # ========================================================
    # PQRS VENCIDAS
    # ========================================================

    def pqrs_vencidas(self):
        """
        Identifica las PQRS que ya superaron
        su fecha máxima de respuesta.
        """

        fecha_actual = datetime.now()

        resultado = []

        for registro in self.registros:

            estado = registro.get(
                "estado_peticion",
                ""
            )

            if estado == "Solucionada":
                continue

            fecha_maxima = self.convertir_fecha(
                registro.get(
                    "fecha_maxima_respuesta",
                    ""
                )
            )

            if fecha_maxima is None:
                continue

            if fecha_actual > fecha_maxima:

                resultado.append(
                    registro
                )

        return resultado

    # ========================================================
    # PROMEDIO DE DÍAS DE RESPUESTA
    # ========================================================

    def promedio_dias_respuesta(self):
        """
        Calcula el promedio de días de respuesta
        cuando existe una fecha real de respuesta.
        """

        tiempos = []

        for registro in self.registros:

            fecha_respuesta = registro.get(
                "fecha_respuesta",
                ""
            )

            if not fecha_respuesta:
                continue

            fecha_inicio = self.convertir_fecha(
                registro.get(
                    "fecha_radicacion",
                    ""
                )
            )

            fecha_fin = self.convertir_fecha(
                fecha_respuesta
            )

            if fecha_inicio is None or fecha_fin is None:
                continue

            dias = (
                fecha_fin - fecha_inicio
            ).days

            if dias >= 0:
                tiempos.append(dias)

        if not tiempos:
            return None

        return round(
            sum(tiempos) / len(tiempos)
        )

    # ========================================================
    # MOSTRAR REPORTES
    # ========================================================

    def mostrar_reportes(self):
        """
        Muestra de manera organizada las estadísticas
        disponibles de PetGestor.
        """

        self.cargar_registros()

        print("\n" + "=" * 70)
        print("                    REPORTES PETGESTOR")
        print("=" * 70)

        # ----------------------------------------------------
        # 1. TOTAL
        # ----------------------------------------------------

        print("\n1. TOTAL DE PQRS")
        print("-" * 70)

        print(
            f"Total de PQRS registradas: "
            f"{self.total_pqrs()}"
        )

        # ----------------------------------------------------
        # 2. MASCOTAS
        # ----------------------------------------------------

        print("\n2. DISTRIBUCIÓN POR TIPO DE MASCOTA")
        print("-" * 70)

        mascotas = self.distribucion_mascotas()

        for mascota, cantidad in mascotas.items():

            print(
                f"{mascota}: {cantidad}"
            )

        # ----------------------------------------------------
        # 3. CANALES
        # ----------------------------------------------------

        print("\n3. DISTRIBUCIÓN POR CANAL DE RECEPCIÓN")
        print("-" * 70)

        canales = self.distribucion_canales()

        for canal, cantidad in canales.items():

            print(
                f"{canal}: {cantidad}"
            )

        # ----------------------------------------------------
        # 4. CAMPUS
        # ----------------------------------------------------

        print("\n4. DISTRIBUCIÓN POR CAMPUS")
        print("-" * 70)

        campus = self.distribucion_campus()

        for nombre, cantidad in campus.items():

            print(
                f"{nombre}: {cantidad}"
            )

        # ----------------------------------------------------
        # 5. TIPO DE SOLICITUD
        # ----------------------------------------------------

        print("\n5. DISTRIBUCIÓN POR TIPO DE SOLICITUD")
        print("-" * 70)

        tipos = self.distribucion_tipo_solicitud()

        for tipo, cantidad in tipos.items():

            print(
                f"{tipo}: {cantidad}"
            )

        # ----------------------------------------------------
        # 6. ESTADOS
        # ----------------------------------------------------

        print("\n6. DISTRIBUCIÓN POR ESTADO")
        print("-" * 70)

        estados = self.distribucion_estados()

        for estado, cantidad in estados.items():

            print(
                f"{estado}: {cantidad}"
            )

        # ----------------------------------------------------
        # 7. PQRS MÁS ANTIGUAS
        # ----------------------------------------------------

        print("\n7. PQRS MÁS ANTIGUAS")
        print("-" * 70)

        antiguas = self.pqrs_mas_antiguas()

        if antiguas:

            for registro in antiguas:

                print(
                    f"ID {registro.get('id')} | "
                    f"{registro.get('tipo_solicitud')} | "
                    f"Fecha: "
                    f"{registro.get('fecha_radicacion')} | "
                    f"Estado: "
                    f"{registro.get('estado_peticion')}"
                )

        else:

            print(
                "No existen registros con fecha válida."
            )

        # ----------------------------------------------------
        # 8. PRÓXIMAS A VENCER
        # ----------------------------------------------------

        print("\n8. PQRS PRÓXIMAS A VENCER")
        print("-" * 70)

        proximas = self.pqrs_proximas_vencer()

        if proximas:

            for elemento in proximas:

                registro = elemento["registro"]

                print(
                    f"ID {registro.get('id')} | "
                    f"{registro.get('tipo_solicitud')} | "
                    f"Vence: "
                    f"{registro.get('fecha_maxima_respuesta')} | "
                    f"Días restantes: "
                    f"{elemento['dias_restantes']}"
                )

        else:

            print(
                "No hay PQRS próximas a vencer."
            )

        # ----------------------------------------------------
        # 9. VENCIDAS
        # ----------------------------------------------------

        print("\n9. PQRS VENCIDAS")
        print("-" * 70)

        vencidas = self.pqrs_vencidas()

        print(
            f"Total de PQRS vencidas: "
            f"{len(vencidas)}"
        )

        if vencidas:

            for registro in vencidas[:10]:

                print(
                    f"ID {registro.get('id')} | "
                    f"{registro.get('tipo_solicitud')} | "
                    f"Fecha máxima: "
                    f"{registro.get('fecha_maxima_respuesta')} | "
                    f"Estado: "
                    f"{registro.get('estado_peticion')}"
                )

            if len(vencidas) > 10:

                print(
                    f"... y "
                    f"{len(vencidas) - 10} "
                    f"PQRS vencidas adicionales."
                )

        # ----------------------------------------------------
        # 10. PROMEDIO DE RESPUESTA
        # ----------------------------------------------------

        print("\n10. PROMEDIO DE DÍAS DE RESPUESTA")
        print("-" * 70)

        promedio = self.promedio_dias_respuesta()

        if promedio is None:

            print(
                "No es posible calcular todavía el promedio "
                "real de días de respuesta porque los archivos "
                "actuales no contienen una fecha de respuesta."
            )

        else:

            print(
                f"Promedio de días de respuesta: "
                f"{promedio} días"
            )

        print("\n" + "=" * 70)