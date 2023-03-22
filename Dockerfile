# Usa una imagen de Python como base
FROM python:3.8-slim-buster

# Establece el directorio de trabajo en /app
WORKDIR /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir certifi

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

RUN export app=flask
# Copia el resto del código de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto 5000 para que podamos acceder a la aplicación Flask
EXPOSE 5000

# Ejecuta la aplicación cuando se inicia el contenedor
CMD ["python", "src/app.py"]

