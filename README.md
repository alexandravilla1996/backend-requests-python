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

backend-requests-python/
├── app/                     # Contiene el código fuente principal del backend
│   ├── main.py              # Punto de entrada de la aplicación y arranque de la API
│   ├── routers/             # Definición de los endpoints (rutas) de la API REST
│   ├── models/              # Modelos que representan las entidades de la base de datos
│   ├── schemas/             # Esquemas para validación y transferencia de datos (JSON)
│   ├── services/            # Lógica de negocio y reglas del sistema
│   ├── database/            # Configuración y conexión a la base de datos PostgreSQL
│   └── config/              # Configuración general del proyecto
│
├── docs/                    # Documentación técnica del proyecto
│   ├── requisitos.md        # Requisitos funcionales y no funcionales del sistema
│   ├── modelo_datos.md      # Modelo de datos y relaciones entre entidades
│   └── decisiones_tecnicas.md # Justificación de decisiones técnicas
│
├── README.md                # Descripción general del proyecto y guía de uso
├── .gitignore               # Archivos y carpetas excluidos del control de versiones
└── LICENSE                  # Licencia de uso del proyecto


