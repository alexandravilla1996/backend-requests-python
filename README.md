# backend-requests-python

API backend desarrollada en Python para gestionar solicitudes de usuarios, utilizando PostgreSQL como base de datos.

# Tecnologías utilizadas

- Python
- FastAPI / Flask
- PostgreSQL
- Git y GitHub

---

# Funcionalidades principales

- Creación de solicitudes
- Consulta de solicitudes individuales y listados
- Actualización del estado de una solicitud
- Eliminación de solicitudes
- Validación de datos
- Manejo estandarizado de errores

# Estructura del proyecto

```text
app/
├── main.py            # Punto de entrada de la aplicación
├── routers/           # Endpoints de la API
├── models/            # Modelos de base de datos
├── schemas/           # Esquemas de validación
├── services/          # Lógica de negocio
├── database/          # Conexión a PostgreSQL
└── config/            # Configuración del proyecto

