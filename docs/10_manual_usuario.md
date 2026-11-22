# Manual de usuario – PetGestor

## 1. Descripción general del sistema

PetGestor es un sistema desarrollado en Python para la gestión de Peticiones, Quejas, Reclamos y Sugerencias (PQRS) relacionadas con la atención de perros y gatos.

El programa permite a los usuarios registrar solicitudes, consultar la información de las PQRS, buscar solicitudes mediante su número de radicado, actualizar sus estados y generar estadísticas sobre los registros del sistema.

PetGestor cuenta con un módulo de autenticación para controlar el acceso al programa y un menú principal desde el cual se pueden ejecutar las diferentes funcionalidades.

## 2. Requisitos para ejecutar el programa

Para utilizar PetGestor se requiere:

- Tener Python 3 instalado en el equipo.
- Contar con los archivos del proyecto PetGestor.
- Disponer de una terminal o entorno de desarrollo que permita ejecutar programas en Python.
- Mantener la estructura de carpetas y los archivos necesarios para el funcionamiento del sistema, especialmente las carpetas `src` y `data`.

### 2.1. Ubicación del programa

El código fuente del sistema se encuentra en la carpeta `src`, donde están los módulos encargados de la autenticación, validaciones, registro y consulta de PQRS, manejo de archivos y generación de reportes.

La carpeta `data` contiene los archivos de texto utilizados para almacenar la información del sistema.

### 2.2. Ejecución del programa

Para iniciar PetGestor, se debe abrir una terminal en la carpeta principal del proyecto y ejecutar el siguiente comando:

```bash
python src/main.py

## 3. Inicio de sesión

Al ejecutar PetGestor, el sistema muestra la pantalla de autenticación, en la cual el usuario debe ingresar sus credenciales para acceder a las funcionalidades del programa.

### 3.1. Ingreso de credenciales

Para iniciar sesión se deben seguir estos pasos:

1. Ejecutar el programa desde la terminal.
2. Ingresar el nombre de usuario o el correo institucional cuando el sistema lo solicite.
3. Introducir la contraseña correspondiente.
4. Esperar la validación de las credenciales.

Si los datos ingresados son correctos y la cuenta se encuentra habilitada, el sistema permite el acceso y muestra el menú principal.

### 3.2. Intentos fallidos de inicio de sesión

El sistema cuenta con un mecanismo de seguridad para controlar los intentos de acceso incorrectos:

- Se permiten hasta tres intentos fallidos.
- Al alcanzar el límite de intentos, el acceso se bloquea temporalmente durante 30 segundos.

Una vez finalizado el tiempo de bloqueo, el usuario puede intentar iniciar sesión nuevamente.

## 4. Menú principal

Después de iniciar sesión correctamente, el sistema muestra el menú principal de PetGestor, desde el cual se puede acceder a las diferentes funcionalidades.

El menú presenta las siguientes opciones:

| Opción | Funcionalidad |
|--------|---------------|
| 1 | Registrar PQRS |
| 2 | Consultar PQRS |
| 3 | Consultar PQRS por radicado |
| 4 | Cambiar estado de PQRS |
| 5 | Generar radicado |
| 6 | Generar estadísticas |
| 7 | Ver información del usuario |
| 8 | Salir |

Para utilizar una funcionalidad, el usuario debe ingresar el número correspondiente a la opción deseada y seguir las instrucciones que aparecen en pantalla.

Cada opción permite realizar una operación específica dentro del sistema.

## 5. Registro de PQRS

Esta opción permite registrar una nueva Petición, Queja, Reclamo o Sugerencia en el sistema.

Para realizar el registro, se deben seguir estos pasos:

1. Seleccionar la opción **1. Registrar PQRS** en el menú principal.
2. Seleccionar el tipo de solicitud que se desea registrar:
   - Petición.
   - Queja.
   - Reclamo.
   - Sugerencia.
3. Ingresar la información del usuario que presenta la solicitud.
4. Seleccionar el tipo de documento e ingresar el número correspondiente.
5. Registrar los datos de contacto solicitados por el sistema, incluyendo el tipo de teléfono y el número.
6. Seleccionar el canal por el cual se recibe la solicitud.
7. Ingresar el asunto y la descripción de la PQRS.
8. Proporcionar la información relacionada con la mascota y los demás datos que solicite el programa.
9. Verificar la información ingresada y completar el registro siguiendo las indicaciones del sistema.

Una vez finalizado el procedimiento, PetGestor confirma el registro y presenta la información de la solicitud, incluyendo su identificador, estado, fecha de radicación y fecha máxima de respuesta.

**Importante:** Se debe proporcionar información válida y completa para que el registro pueda realizarse correctamente.

## 6. Consulta general de PQRS

Esta opción permite consultar las PQRS que se encuentran almacenadas en el sistema y visualizar la información de las solicitudes registradas.

Para realizar la consulta, se deben seguir estos pasos:

1. Seleccionar la opción **2. Consultar PQRS** en el menú principal.
2. Esperar a que el sistema consulte los registros almacenados.
3. Revisar la información de las PQRS que muestra el programa.
4. Una vez finalizada la consulta, regresar al menú principal siguiendo las indicaciones del sistema.

La información presentada permite conocer los registros existentes y revisar los datos asociados a cada solicitud.

## 7. Consulta de PQRS por número de radicado

Esta opción permite localizar una solicitud específica mediante su número de radicado.

Para realizar la consulta, se deben seguir estos pasos:

1. Seleccionar la opción **3. Consultar PQRS por radicado** en el menú principal.
2. Ingresar el número de radicado de la solicitud que se desea consultar.
3. Esperar a que el sistema realice la búsqueda.
4. Revisar la información de la PQRS encontrada.

Si el número de radicado corresponde a una solicitud registrada, el sistema muestra la información asociada a ella.

Si no se encuentra una solicitud con ese número, el programa informa que no existen resultados para la búsqueda.

## 8. Cambio de estado de una PQRS

Esta opción permite actualizar el estado de una solicitud previamente registrada en PetGestor.

Para realizar el procedimiento, se deben seguir estos pasos:

1. Seleccionar la opción **4. Cambiar estado de PQRS** en el menú principal.
2. Ingresar el número de radicado o el identificador de la solicitud que se desea actualizar, según lo solicite el sistema.
3. Verificar que la PQRS encontrada corresponda a la solicitud que se desea modificar.
4. Seleccionar el nuevo estado entre las opciones disponibles.
5. Confirmar la actualización siguiendo las indicaciones del programa.

Una vez realizado el procedimiento, el sistema informa si el cambio de estado se efectuó correctamente.

## 9. Generación de radicados

Esta opción permite generar el número de radicado asociado a una solicitud registrada en PetGestor.

Para utilizar esta funcionalidad, se deben seguir estos pasos:

1. Seleccionar la opción **5. Generar radicado** en el menú principal.
2. Seguir las instrucciones que muestra el sistema para identificar la solicitud correspondiente.
3. Proporcionar la información solicitada por el programa.
4. Esperar a que el sistema realice el procedimiento de generación del radicado.
5. Verificar el resultado que presenta el programa.

El número de radicado permite identificar y realizar el seguimiento de una PQRS dentro del sistema.

## 10. Consulta de estadísticas

Esta opción permite consultar estadísticas relacionadas con las PQRS registradas en PetGestor.

Para acceder a esta funcionalidad, se deben seguir estos pasos:

1. Seleccionar la opción **6. Generar estadísticas** en el menú principal.
2. Esperar a que el sistema procese la información almacenada.
3. Revisar los resultados estadísticos que presenta el programa.
4. Analizar la información mostrada para conocer el comportamiento de las solicitudes registradas.
5. Regresar al menú principal siguiendo las indicaciones del sistema.

Las estadísticas permiten obtener un resumen de los registros y facilitar el análisis de la información almacenada en el sistema.

## 11. Información del usuario

Esta opción permite consultar la información correspondiente al usuario que ha iniciado sesión en PetGestor.

Para acceder a esta funcionalidad, se deben seguir estos pasos:

1. Seleccionar la opción **7. Ver información del usuario** en el menú principal.
2. Esperar a que el sistema consulte los datos del usuario autenticado.
3. Revisar la información presentada en pantalla.
4. Regresar al menú principal siguiendo las indicaciones del programa.

Esta funcionalidad permite visualizar los datos asociados a la cuenta con la que se está utilizando el sistema.

## 11. Información del usuario

Esta opción permite consultar la información correspondiente al usuario que ha iniciado sesión en PetGestor.

Para acceder a esta funcionalidad, se deben seguir estos pasos:

1. Seleccionar la opción **7. Ver información del usuario** en el menú principal.
2. Esperar a que el sistema consulte los datos del usuario autenticado.
3. Revisar la información presentada en pantalla.
4. Regresar al menú principal siguiendo las indicaciones del programa.

Esta funcionalidad permite visualizar los datos asociados a la cuenta con la que se está utilizando el sistema.
