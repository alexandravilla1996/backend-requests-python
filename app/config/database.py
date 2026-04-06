# Importamos el motor de conexión
from sqlalchemy import create_engine

# Base para crear modelos (tablas)
from sqlalchemy.ext.declarative import declarative_base

# Permite crear sesiones para interactuar con la DB
from sqlalchemy.orm import sessionmaker

# Conexión a PostgreSQL
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/solicitudes_db"

# Motor de conexión
engine = create_engine(DATABASE_URL)

# Creamos una fábrica de sesiones
SessionLocal = sessionmaker(
    autocommit=False,  # No guarda cambios automáticamente
    autoflush=False,   # No envía cambios automáticamente
    bind=engine        # Conecta con PostgreSQL
)

# Base para que los modelos hereden
Base = declarative_base()