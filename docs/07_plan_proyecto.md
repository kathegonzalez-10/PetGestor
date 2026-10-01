# 7. Plan de proyecto

## 7.1 Descripción

El desarrollo de PetGestor se organizará mediante actividades relacionadas con el análisis de requisitos, diseño, programación, pruebas, documentación y preparación de la entrega.

El proyecto será desarrollado utilizando Python, archivos planos y una estructura modular organizada en las carpetas establecidas para el proyecto.

## 7.2 Actividades del proyecto

| No. | Actividad | Descripción |
|---|---|---|
| 1 | Análisis del problema | Identificación de las necesidades y requisitos establecidos para el sistema PQRS. |
| 2 | Definición de requisitos | Organización de los requisitos funcionales y no funcionales. |
| 3 | Diseño de la estructura | Creación de las carpetas, archivos y estructura general del proyecto. |
| 4 | Módulo de autenticación | Desarrollo del Login, validación de usuarios y control de intentos. |
| 5 | Gestión de archivos | Desarrollo de las funciones para lectura y escritura de archivos planos. |
| 6 | Registro de PQRS | Desarrollo del registro de peticiones, quejas, reclamos y sugerencias. |
| 7 | Validación de datos | Implementación de las validaciones de nombres, correos, teléfonos y fechas. |
| 8 | Gestión de estados | Implementación de los estados Registrada, En proceso y Solucionada. |
| 9 | Consulta y radicado | Desarrollo de las funciones de consulta y visualización de los registros. |
| 10 | Estadísticas | Desarrollo de los cálculos y reportes requeridos. |
| 11 | Pruebas | Verificación del funcionamiento del sistema y corrección de errores. |
| 12 | Documentación | Elaboración de la documentación y manual de usuario. |
| 13 | Organización del repositorio | Organización de código, documentación, imágenes y archivos de datos en GitHub. |
| 14 | Preparación de entrega | Revisión final del proyecto y preparación de los entregables. |

## 7.3 Cronograma

El siguiente cronograma representa la planificación propuesta para el desarrollo del proyecto.

| Actividad | Sep. 1-7 | Sep. 8-14 | Sep. 15-21 | Sep. 22-30 | Oct. 1-15 | Oct. 16-31 | Nov. 1-10 | Nov. 11-18 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Análisis del problema | X | | | | | | | |
| Definición de requisitos | X | X | | | | | | |
| Diseño de estructura | | X | X | | | | | |
| Módulo de autenticación | | | X | X | | | | |
| Gestión de archivos | | | | X | X | | | |
| Registro de PQRS | | | | X | X | X | | |
| Validación de datos | | | | | X | X | | |
| Gestión de estados | | | | | X | X | | |
| Consulta y radicado | | | | | | X | X | |
| Estadísticas | | | | | | X | X | |
| Pruebas | | | | | | X | X | X |
| Documentación | | | X | X | X | X | X | X |
| Organización del repositorio | | X | X | X | X | X | X | X |
| Preparación de entrega | | | | X | | | X | X |

## 7.4 Diagrama de Gantt

```mermaid
gantt
    title Plan de proyecto PetGestor
    dateFormat  YYYY-MM-DD
    axisFormat  %d/%m

    section Análisis
    Análisis del problema       :2026-09-01, 7d
    Definición de requisitos    :2026-09-08, 7d

    section Diseño y desarrollo
    Diseño de estructura        :2026-09-15, 7d
    Módulo de autenticación     :2026-09-22, 9d
    Gestión de archivos         :2026-10-01, 7d
    Registro de PQRS            :2026-10-08, 14d
    Validación de datos         :2026-10-16, 10d
    Gestión de estados          :2026-10-20, 10d
    Consulta y radicado         :2026-10-26, 8d
    Estadísticas                :2026-11-01, 7d

    section Pruebas y documentación
    Pruebas                     :2026-11-05, 8d
    Documentación               :2026-09-15, 60d
    Organización del repositorio :2026-09-15, 60d
    Preparación de entrega      :2026-11-13, 6d

