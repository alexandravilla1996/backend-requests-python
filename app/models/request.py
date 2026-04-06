from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.config.database import Base

# Tabla solicitudes
class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)

    description = Column(String)

    # Estado por defecto
    status = Column(String(50), default="pendiente")

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relación con usuario
    user_id = Column(Integer, ForeignKey("users.id"))