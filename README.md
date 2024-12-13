# Gestor de Recetas Peruanas con MongoDB Atlas

## Descripción
Aplicación Python desarrollada por Farley Viveros que demuestra operaciones CRUD en MongoDB Atlas usando una colección de recetas peruanas.

## Características
- Conexión a MongoDB Atlas
- Operaciones CRUD con recetas peruanas
- Uso de PyMongo para interactuar con la base de datos

## Requisitos
- Python 3.x
- PyMongo
- Cuenta de MongoDB Atlas

## Instalación
1. Clonar el repositorio
2. Instalar dependencias: `pip install pymongo`

## Configuración
Reemplazar `<Tu Cadena de Conexión de Atlas>` en el código con tu cadena de conexión real de MongoDB Atlas.

## Uso
Ejecutar: `python recetas_peruanas.py`

## Estructura de Datos
```json
{
  "nombre": "nombre de la receta",
  "ingredientes": ["ingrediente1", "ingrediente2", ...],
  "tiempo_prep": tiempo en minutos
}
