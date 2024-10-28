# Generar Reporte de Evaluación Docente

Este proyecto utiliza Gradio y se conecta a una API en MongoDB para generar reportes de evaluación docente. Solo necesita el ID del curso y de la materia para buscar y generar el documento `.docx`.

## Requisitos

- Python 3.11
- Gradio
- pymongo
- python-docx

## Instalación

1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd generateReport
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:
    ```bash
    python app.py
    ```

2. Abre tu navegador y ve a `http://localhost:7860`.

3. Ingresa el ID del curso y de la materia para generar el reporte.

## Estructura del Proyecto

- `functions`: Carpeta con las funciones necesarias del proyecto.
- `temp`: Carpeta donde se guardan los archivos temporales.
- `utils`: Carpeta con la plantilla del reporte
- `main.py`: Archivo principal de la aplicación.
- `requirements.txt`: Lista de dependencias del proyecto.
- `README.md`: Este archivo.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.