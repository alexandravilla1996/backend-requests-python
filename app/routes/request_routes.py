# APIRouter que permite crear rutas separadas del main
# Depends permite inyectar dependencias (como la DB)
from fastapi import APIRouter, Depends

# Tipo de conexión a la DB
from sqlalchemy.orm import Session

# Importamos la sesión de base de datos
from app.config.database import SessionLocal

# Importamos los schemas (validación)
from app.schemas.request_schema import RequestCreate, RequestResponse

# Importamos la lógica de negocio
from app.services.request_service import create_request


# Creamos el enrutador
router = APIRouter()


# 🔹 Función para manejar conexión a la DB en cada request
def get_db():

    # Abrimos conexión
    db = SessionLocal()

    try:
        # Entregamos la conexión al endpoint
        yield db

    finally:
        # Cerramos conexión 
        db.close()


# Endpoint para crear solicitud
@router.post("/requests", response_model=RequestResponse)
def create_new_request(

    # Datos que envía el cliente (validados por Pydantic)
    request: RequestCreate,

    # Inyección automática de la base de datos
    db: Session = Depends(get_db)
):

    # Llamamos al servicio (lógica)
    return create_request(db, request)