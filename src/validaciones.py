import re
from datetime import datetime


def validar_nombre(nombre):
    """
    Valida el nombre completo del solicitante.
    Debe tener entre 3 y 100 caracteres y permitir
    letras, espacios, apóstrofes y guiones.
    """

    nombre = nombre.strip()

    if len(nombre) < 3 or len(nombre) > 100:
        return False

    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü' -]+$"

    return bool(re.fullmatch(patron, nombre))


def validar_documento(numero_documento):
    """
    Valida el número de documento.
    Debe contener solamente números y tener
    entre 3 y 15 dígitos.
    """

    numero_documento = numero_documento.strip()

    return (
        numero_documento.isdigit()
        and 3 <= len(numero_documento) <= 15
    )


def validar_correo(correo):
    """
    Valida el formato básico del correo electrónico.
    """

    correo = correo.strip()

    if len(correo) > 254:
        return False

    patron = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return bool(re.fullmatch(patron, correo))


def validar_telefono(telefono):
    """
    Valida el teléfono de contacto.
    Debe contener exactamente 10 dígitos.
    """

    telefono = telefono.strip()

    return telefono.isdigit() and len(telefono) == 10


def validar_fecha(fecha):
    """
    Valida que la fecha tenga el formato:
    día/mes/año.
    """

    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True

    except ValueError:
        return False


def calcular_fecha_maxima(fecha_radicacion):
    """
    Calcula la fecha máxima de respuesta.
    La fecha corresponde a 25 días calendario
    después de la fecha de radicación.
    """

    from datetime import timedelta

    fecha = datetime.strptime(
        fecha_radicacion,
        "%d/%m/%Y"
    )

    fecha_maxima = fecha + timedelta(days=25)

    return fecha_maxima.strftime("%d/%m/%Y")


def validar_tipo_documento(tipo_documento):
    """
    Valida los tipos de documento permitidos.
    """

    tipos_permitidos = [
        "CC",
        "TI",
        "CE",
        "PP",
        "NIT"
    ]

    return tipo_documento.upper() in tipos_permitidos


def validar_tipo_telefono(tipo_telefono):
    """
    Valida los tipos de teléfono permitidos.
    """

    tipos_permitidos = [
        "Celular",
        "Fijo",
        "Corporativo",
        "Otro"
    ]

    return tipo_telefono.capitalize() in tipos_permitidos


def validar_tipo_mascota(tipo_mascota):
    """
    Valida el tipo de mascota permitido.
    """

    tipos_permitidos = [
        "Perro",
        "Gato",
        "Otro"
    ]

    return tipo_mascota.capitalize() in tipos_permitidos


def validar_estado(estado):
    """
    Valida los estados permitidos para una PQRS.
    """

    estados_permitidos = [
        "Registrada",
        "En proceso",
        "Solucionada"
    ]

    return estado in estados_permitidos