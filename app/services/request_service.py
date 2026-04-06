# Importamos Session que representa una conexión activa con la base de datos
from sqlalchemy.orm import Session

# Importamos el modelo (tabla)
from app.models.request import Request


# Función que contiene la lógica de negocio
def create_request(db: Session, request_data):

    # Creamos un objeto tipo Request (esto NO guarda aún en la DB)
    new_request = Request(
        description=request_data.description,  # asignamos descripción
        user_id=request_data.user_id          # asignamos usuario
    )

    # Agregamos el objeto a la sesión (preparado para guardarse)
    db.add(new_request)

    # Confirmamos cambios, aquí SI se guarda en PostgreSQL
    db.commit()

    # Refrescamos el objeto y trae datos actualizados (ej: ID generado)
    db.refresh(new_request)

    # Retornamos el objeto ya guardado
    return new_request