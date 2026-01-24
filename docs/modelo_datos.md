# Modelo de Datos

## Backend API – Sistema de Gestión de Solicitudes

## 1. Introducción

Este documento describe el modelo de datos del proyecto Backend API – Sistema de Gestión de Solicitudes, el cual será implementado utilizando una base de datos relacional PostgreSQL. El diseño del modelo busca garantizar integridad, consistencia y facilidad de mantenimiento.

## 2. Descripción General

El sistema gestiona usuarios y las solicitudes asociadas a estos. Cada usuario puede registrar una o varias solicitudes, y cada solicitud pertenece a un único usuario.

## 3. Entidades y Relaciones

### 3.1 Entidad: Usuario

Representa a las personas que interactúan con el sistema y registran solicitudes.

**Tabla:** users

| Campo      | Tipo de dato | Descripción                     |
| ---------- | ------------ | ------------------------------- |
| id         | SERIAL       | Identificador único del usuario |
| name       | VARCHAR(100) | Nombre completo del usuario     |
| email      | VARCHAR(150) | Correo electrónico del usuario  |
| created_at | TIMESTAMP    | Fecha de creación del usuario   |

**Clave primaria:** id

### 3.2 Entidad: Solicitud

Representa las solicitudes creadas por los usuarios.

**Tabla:** requests

| Campo       | Tipo de dato | Descripción                         |
| ----------- | ------------ | ----------------------------------- |
| id          | SERIAL       | Identificador único de la solicitud |
| description | TEXT         | Descripción de la solicitud         |
| status      | VARCHAR(50)  | Estado de la solicitud              |
| created_at  | TIMESTAMP    | Fecha de creación de la solicitud   |
| user_id     | INTEGER      | Identificador del usuario asociado  |

**Clave primaria:** id

**Clave foránea:** user_id → users(id)

## 4. Relaciones

* Un usuario puede tener una o muchas solicitudes.
* Una solicitud pertenece a un único usuario.

Relación: **Uno a Muchos (1:N)** entre `users` y `requests`.

## 5. Reglas de Integridad

* El campo `email` del usuario debe ser único.
* No se permite crear una solicitud sin un usuario asociado.
* El estado de la solicitud debe pertenecer a un conjunto predefinido (pendiente, en proceso, resuelta).

## 6. Justificación del Diseño

* Se utiliza una base de datos relacional para asegurar consistencia y relaciones claras.
* La separación de entidades facilita la escalabilidad del sistema.
* El modelo permite futuras extensiones sin afectar la estructura actual.

## 7. Estado del Documento

Documento en construcción. Puede ajustarse conforme se implementen nuevas funcionalidades.
