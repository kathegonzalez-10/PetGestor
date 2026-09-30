# 6. Especificación de Requisitos - PetGestor

## Requisitos Funcionales

**RF1 - Registro del Solicitante:**
El sistema debe validar y registrar la información personal del solicitante que realiza la PQRS.
- Nombre completo: campo obligatorio, entre 3 y 100 caracteres. Solo permite letras, espacios, tildes, ñ, apóstrofe (') y guión (-). No permite números ni caracteres especiales.
- Tipo de documento: obligatorio, valores permitidos CC, TI, CE, PP, NIT.
- Número de documento: obligatorio, entre 3 y 15 dígitos, solo números.
- Tipo de teléfono: obligatorio, Celular, Fijo, Corporativo, Otro.
- Teléfono de contacto: obligatorio, 10 dígitos, solo números.
- Correo electrónico: obligatorio, máximo 254 caracteres, debe cumplir estructura correo@dominio.com con un único @ y dominio válido.
- Dirección: campo opcional, entre 5 y 200 caracteres. Si el usuario no la ingresa, el sistema debe mostrar "N/A" en el comprobante de radicado.

**RF2 - Registro de la Información de la PQRS:**
- Tipo de solicitud: obligatorio, Petición, Queja, Reclamo o Sugerencia.
- Fecha de radicación: obligatoria, formato datetime de Python, no puede ser una fecha futura.
- Canal de recepción: obligatorio, Presencial, Correo electrónico, Página web, Teléfono, Redes sociales, Otro.
- Asunto o título: obligatorio, entre 5 y 150 caracteres, permite letras, números y signos de puntuación básicos.
- Descripción detallada: obligatoria, entre 20 y 2000 caracteres, texto libre que no puede estar vacío ni contener solo espacios.
- Tipo de mascota: obligatorio, Perro, Gato, Otro.
- Campus relacionado: obligatorio, campus de la UdeA donde se solicita el servicio.

**RF3 - Gestión de Tiempos y Estado de la PQRS:**
- Fecha máxima de respuesta: se calcula automáticamente como Fecha de radicación + 25 días calendario.
- Estado de la petición: obligatorio, valores permitidos Registrada, En proceso, Solucionada. Valor inicial al registrar es Registrada. Los cambios deben seguir el flujo Registrada -> En proceso -> Solucionada.

**RF4 - Gestión de Documentos y Radicado:**
- El sistema debe gestionar la información en cuatro archivos planos independientes: Peticion.txt, Queja.txt, Reclamo.txt y Sugerencia.txt.
- Cada archivo debe manejar un ID auto-incremental propio comenzando en 1, independiente de los otros archivos.
- El sistema debe permitir generar un comprobante o radicado en formato TXT de 120 caracteres de ancho fijo, con marco ASCII (+, -, |), que incluya datos del radicado, datos del solicitante y datos de la solicitud, sin incluir la descripción detallada para optimización del espacio.
- El sistema debe permitir consultar el estado general de las PQRS registradas.

**RF5 - Estadísticas del Sistema:**
- El sistema debe calcular el promedio de días que toma dar respuesta a una PQRS.
- Debe permitir generar estadísticas sobre la cantidad de registros por tipo de mascota, por tipo de documento, por campus, documentos más antiguos y registros próximos a vencer.

## Requisitos No Funcionales

**RNF1 - Usabilidad:** El sistema debe tener un menú amigable en consola, visualmente organizado, centrado y de fácil uso para el administrador.

**RNF2 - Rendimiento:** El sistema debe manejar la lectura y escritura de archivos planos de forma eficiente, sin demoras al registrar o consultar PQRS.

**RNF3 - Compatibilidad:** El sistema debe ser desarrollado en Python y funcionar en cualquier sistema operativo que soporte Python 3.

**RNF4 - Seguridad de Datos:** El sistema debe validar que no se guarden registros con campos obligatorios vacíos y debe garantizar que los ID sean únicos y consecutivos.

**RNF5 - Mantenibilidad:** El código debe estar modularizado en archivos separados para validaciones, manejo de archivos y reportes, facilitando su actualización.
