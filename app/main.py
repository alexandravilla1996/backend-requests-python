"""
Archivo: main.py
Descripción:
Este archivo corresponde al punto de inicio de la API Backend de Gestión
de Solicitudes. Desde aquí inicia la aplicación y se configuran los
componentes principales del sistema.

Autor: Alexandra Maireth Villa Guerra
Fecha: Enero 2026
"""
# Importación de librerias
from fastapi import FastAPI

# Creación de instancia principal de la aplicación
app = FastAPI(
    title="Backend de Gestión de Solicitudes",
    description="API backend desarrollada en Python para la gestión de solicitudes.",
    version="1.0.0"
)

@app.get("/")
def root():
    """
    Endpoint raíz del sistema.
    Se utiliza para verificar que la API se encuentra en funcionamiento.
    """
    return {"message": "API Backend de Solicitudes en ejecución"}
