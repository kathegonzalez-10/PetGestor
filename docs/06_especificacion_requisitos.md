# 6. Especificación de requisitos

## 6.1 Requisitos funcionales

Los requisitos funcionales describen las acciones, comportamientos y operaciones que debe realizar PetGestor para satisfacer las necesidades del usuario.

### RF01. Autenticación de usuarios

El sistema debe solicitar obligatoriamente el inicio de sesión antes de permitir el acceso al menú principal.

El usuario podrá autenticarse utilizando:

- Nombre de usuario.
- Correo institucional.
- Contraseña.

Las credenciales deberán ser verificadas contra el archivo de usuarios autorizados.

### RF02. Control de intentos de acceso

El sistema debe permitir un máximo de tres intentos fallidos de autenticación.

Al alcanzar los tres intentos fallidos, el sistema deberá bloquear temporalmente la pantalla durante un tiempo definido por el equipo y mostrar el tiempo de bloqueo.

### RF03. Gestión de sesión

Cuando la autenticación sea exitosa, el sistema debe almacenar los datos del usuario autenticado para asociarlo automáticamente con las operaciones realizadas durante la sesión.

### RF04. Registro de PQRS

El sistema debe permitir registrar:

- Peticiones.
- Quejas.
- Reclamos.
- Sugerencias.

Cada tipo de PQRS debe almacenarse en su archivo plano correspondiente.

### RF05. Asignación de identificador consecutivo

Cada PQRS debe recibir un identificador de registro entero, auto-incremental y sin repetirse.

Cada archivo plano debe manejar su propia secuencia independiente de registros.

### RF06. Registro de información del solicitante

El sistema debe permitir registrar la información del solicitante:

- Nombre completo.
- Tipo de documento.
- Número de documento.
- Teléfono de contacto.
- Tipo de teléfono.
- Correo electrónico.
- Dirección.

### RF07. Registro de información de la PQRS

El sistema debe permitir registrar:

- Tipo de solicitud.
- Fecha de radicación.
- Canal de recepción.
- Asunto o título.
- Descripción detallada de la solicitud.
- Tipo de animal atendido.
- Campus o sede correspondiente.
- Estado de la PQRS.

### RF08. Validación de datos

El sistema debe validar los datos ingresados por el usuario antes de almacenarlos.

Se deberán realizar validaciones relacionadas con:

- Nombres.
- Correo electrónico.
- Teléfono.
- Fechas.
- Datos obligatorios.

### RF09. Gestión de fechas

El sistema debe registrar la fecha de radicación de cada PQRS y calcular la fecha máxima de respuesta.

La fecha máxima de respuesta será de 30 días calendario después de la fecha de registro.

### RF10. Gestión de estados

Cada PQRS debe manejar los siguientes estados:

- Registrada.
- En proceso.
- Solucionada.

El sistema debe permitir consultar el estado de las PQRS registradas.

### RF11. Consulta de PQRS

El sistema debe permitir consultar los registros existentes y visualizar la información correspondiente a cada PQRS.

### RF12. Consulta mediante radicado

El sistema debe permitir visualizar la información de una PQRS utilizando la misma funcionalidad de impresión del radicado.

### RF13. Manejo de campos opcionales

Cuando la dirección del solicitante no sea proporcionada, el sistema deberá mostrar el valor:

`N/A`

### RF14. Estadísticas

El sistema debe permitir generar estadísticas sobre la información registrada.

La estadística obligatoria corresponde al promedio de días que toma dar respuesta a una PQRS.

Además, se deberán incluir estadísticas relacionadas con:

- Distribución de solicitudes por tipo de mascota.
- Proporción de PQRS por canal de recepción.
- Distribución de solicitudes por campus UdeA.
- Porcentaje de efectividad y resolución según el estado.
- Alertas de vencimiento y control del plazo de respuesta.
- Análisis de solicitantes y perfilamiento operativo.

### RF15. Manejo de archivos planos

El sistema debe permitir la lectura y escritura de los archivos planos correspondientes a:

- Peticion.txt
- Queja.txt
- Reclamo.txt
- Sugerencia.txt

### RF16. Generación de información para análisis

El sistema deberá permitir utilizar la información consolidada de las PQRS para posteriores procesos de análisis y visualización mediante Power BI.

---

## 6.2 Requisitos no funcionales

Los requisitos no funcionales establecen características de calidad que debe cumplir el sistema.

### RNF01. Seguridad

El sistema debe controlar el acceso mediante autenticación con usuario o correo institucional y contraseña.

Además, deberá limitar los intentos fallidos de acceso y realizar un bloqueo temporal después de tres intentos incorrectos.

### RNF02. Usabilidad

La interfaz debe ser clara, sencilla y visualmente amigable para facilitar el uso del sistema desde la consola.

Los mensajes mostrados al usuario deben ser comprensibles y orientar sobre las acciones que puede realizar.

### RNF03. Rendimiento

El sistema debe procesar las operaciones de lectura, escritura, consulta y actualización de los archivos planos de manera eficiente.

### RNF04. Fiabilidad

La información registrada debe conservarse correctamente en los archivos correspondientes y los identificadores de las PQRS no deben repetirse dentro de cada archivo.

### RNF05. Mantenibilidad

El código debe estar organizado mediante clases, objetos y módulos independientes para facilitar su mantenimiento y modificación.

### RNF06. Modularidad

Las funciones de validación, manipulación de archivos y generación de reportes deben estar separadas en módulos específicos.

Se utilizarán los siguientes archivos:

- `validaciones.py`
- `archivos.py`
- `reportes.py`

### RNF07. Compatibilidad

El sistema debe desarrollarse en Python y ejecutarse desde una interfaz de consola.

### RNF08. Organización

El código fuente, la documentación, las imágenes y los archivos de datos deberán mantenerse organizados en las carpetas correspondientes del repositorio:

- `src/`
- `docs/`
- `images/`
- `data/`



