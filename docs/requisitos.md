# Documento de Requisitos
## Backend API – Sistema de Gestión de Solicitudes

## 1. Introducción

Este documento describe los requisitos del proyecto Backend API – Sistema de Gestión de Solicitudes, consiste en el desarrollo de una API backend utilizando Python y PostgreSQL. El documento tiene como propósito definir de manera clara el alcance, las funcionalidades y las restricciones del sistema.

## 2. Objetivo

Desarrollar una API backend que permita gestionar solicitudes de usuarios, aplicando buenas prácticas de ingeniería de software, control de versiones y documentación técnica, con el fin de fortalecer el perfil profesional y el portafolio de desarrollo.

## 3. Alcance del Proyecto

El sistema permitirá:

- Registrar usuarios.
- Crear solicitudes asociadas a un usuario.
- Consultar solicitudes registradas.
- Actualizar el estado de una solicitud.

El sistema no incluye interfaz gráfica (frontend) ni autenticación avanzada en esta fase inicial.

## 4. Requisitos Funcionales

**RF-01 Registro de usuarios**

El sistema debe permitir registrar usuarios con información básica como nombre, correo electrónico y fecha de registro.

**RF-02 Creación de solicitudes**

El sistema debe permitir que un usuario registre una solicitud indicando una descripción y una fecha de creación.

**RF-03 Consulta de solicitudes**

El sistema debe permitir consultar todas las solicitudes registradas y filtrar por usuario.

**RF-04 Actualización de estado**

El sistema debe permitir actualizar el estado de una solicitud (por ejemplo: pendiente, en proceso, resuelta).

## 5. Requisitos No Funcionales

**RNF-01 Usabilidad**

La API debe seguir convenciones REST y retornar respuestas claras en formato JSON.

**RNF-02 Rendimiento**

El sistema debe responder a las solicitudes en un tiempo razonable bajo carga normal.

**RNF-03 Mantenibilidad**

El código debe estar organizado en capas (rutas, servicios, modelos) para facilitar su mantenimiento.

**RNF-04 Portabilidad**

El sistema debe poder ejecutarse en diferentes entornos locales sin cambios significativos.

## 6. Restricciones

- El desarrollo se realizará utilizando Python.
- La base de datos será PostgreSQL.
- El proyecto será gestionado mediante Git y GitHub.
- La documentación se redactará en español.

## 7. Supuestos

El sistema será utilizado como proyecto de portafolio profesional, orientado a la demostración de competencias técnicas en desarrollo backend.

## 8. Estado del Documento

El proyecto se encuentra actualmente en desarrollo.