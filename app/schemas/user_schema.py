# Importamos BaseModel para definir estructuras de datos (JSON)
from pydantic import BaseModel, EmailStr

# Importamos datetime para manejar fechas
from datetime import datetime

# Este schema se usa cuando el cliente ENVÍA datos (POST)
class UserCreate(BaseModel):

    # Campo obligatorio tipo texto
    name: str

    # Campo email validado automáticamente (formato correo)
    email: EmailStr


# Este schema se usa cuando la API RESPONDE datos
class UserResponse(BaseModel):

    # ID del usuario (lo genera la base de datos)
    id: int

    # Nombre del usuario
    name: str

    # Email del usuario
    email: str

    # Fecha en que fue creado
    created_at: datetime

    # Configuración especial
    class Config:
        # Permite convertir objetos de SQLAlchemy a JSON automáticamente
        orm_mode = True