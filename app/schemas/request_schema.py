# Base para definir estructura de datos
from pydantic import BaseModel

# Para manejar fechas
from datetime import datetime


# Datos que el cliente envía para crear una solicitud
class RequestCreate(BaseModel):

    # Descripción de la solicitud
    description: str

    # ID del usuario (relación)
    user_id: int


# Datos que la API devuelve
class RequestResponse(BaseModel):

    # ID generado por la base de datos
    id: int

    # Descripción de la solicitud
    description: str

    # Estado de la solicitud (pendiente, en proceso, etc.)
    status: str

    # Fecha de creación
    created_at: datetime

    # Usuario asociado
    user_id: int

    class Config:
        # Permite convertir modelo DB a JSON
        orm_mode = True