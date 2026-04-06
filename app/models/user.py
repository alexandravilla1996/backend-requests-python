from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.config.database import Base

# Definimos la tabla de usuarios
class User(Base):
    __tablename__ = "users"

    # ID único del usuario
    id = Column(Integer, primary_key=True, index=True)

    # Nombre del usuario
    name = Column(String(100))

    # Email único
    email = Column(String(150), unique=True, index=True)

    # Fecha automática
    created_at = Column(DateTime, default=datetime.utcnow)