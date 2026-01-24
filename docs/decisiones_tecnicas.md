# Decisiones Técnicas
## Backend API – Sistema de Gestión de Solicitudes

## 1. Introducción

Este documento describe y justifica las principales decisiones técnicas adoptadas para el desarrollo del proyecto **backend-requests-python**, correspondiente a una API Backend para la Gestión de Solicitudes.

El objetivo de este documento es evidenciar los criterios técnicos utilizados en la selección de tecnologías, herramientas y en la organización del sistema, alineados con prácticas comunes en entornos profesionales de desarrollo de software.

## 2. Lenguaje de Programación

### Python

Se seleccionó Python como lenguaje de programación principal debido a las siguientes razones:

* Alta demanda en el mercado laboral para desarrollo backend.
* Sintaxis clara y legible, que facilita el mantenimiento del código.
* Amplio ecosistema de frameworks y librerías orientadas al desarrollo de APIs REST.
* Excelente integración con bases de datos relacionales como PostgreSQL.

Esta elección permite desarrollar un sistema backend escalable, mantenible y alineado con estándares actuales de la industria.

## 3. Tipo de Aplicación

### API Backend basada en REST

El sistema se desarrolla como una API REST, lo cual permite:

* Separar la lógica de negocio de cualquier capa de presentación.
* Facilitar la integración futura con aplicaciones web, móviles u otros servicios.
* Utilizar métodos HTTP y códigos de respuesta estandarizados.

Este enfoque es ampliamente utilizado en arquitecturas modernas orientadas a servicios.

## 4. Base de Datos

### PostgreSQL

Se eligió PostgreSQL como sistema gestor de base de datos relacional debido a que:

* Cumple con los estándares SQL.
* Garantiza integridad, consistencia y confiabilidad de los datos.
* Permite manejar relaciones estructuradas entre entidades.
* Es una tecnología robusta y ampliamente utilizada en entornos empresariales.

Aunque la API intercambia información en formato JSON, el modelo relacional resulta adecuado para la naturaleza estructurada de las solicitudes gestionadas por el sistema.

## 5. Control de Versiones

### Git y GitHub

El proyecto es gestionado mediante Git como sistema de control de versiones y GitHub como repositorio remoto, lo que permite:

* Llevar un historial claro de cambios en el código.
* Facilitar el seguimiento de la evolución del proyecto.
* Centralizar el código fuente y la documentación técnica.

## 6. Estructura del Proyecto

Se adoptó una estructura modular basada en responsabilidades, separando claramente:

* Rutas (endpoints de la API)
* Servicios (lógica de negocio)
* Modelos (representación de datos y persistencia)
* Esquemas (validación y transferencia de datos)
* Configuración y conexión a base de datos

Esta organización mejora la legibilidad del código, facilita el mantenimiento y permite la escalabilidad del sistema.

## 7. Documentación

La documentación del proyecto se mantiene en la carpeta `docs/`, utilizando formato Markdown.

La documentación describe los requisitos, la arquitectura, el modelo de datos y las decisiones técnicas del sistema, con el objetivo de facilitar su comprensión tanto para evaluación técnica como para mantenimiento futuro.

## 8. Estado del Documento

Este documento se encuentra en desarrollo y podrá actualizarse conforme el proyecto evolucione y se incorporen nuevas decisiones técnicas.

