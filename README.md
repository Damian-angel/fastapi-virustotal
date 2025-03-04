# FastAPI VirusTotal Scanner

Este es un servicio REST API construido con FastAPI que permite a los usuarios subir archivos y escanearlos en busca de malware utilizando la API de VirusTotal. El servicio está containerizado con Docker para facilitar su implementación.

---

## Requisitos

- Docker instalado.
- Una API key de VirusTotal.

---

## Configuración

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Damian-angel/fastapi-virustotal.git
   cd fastapi-virustotal
    ```

2. Crea un archivo .env en la raíz del proyecto y agrega tu clave API de VirusTotal:
    ```bash
    VIRUSTOTAL_API_KEY=virustotal_api_key_here
    ```
## Ejecutar con Docker

Ejecuta el siguiente comando para construir la imagen de Docker:
```bash
    docker build -t fastapi-virustotal .
```

Ejecuta el contenedor con:
```bash
docker run -p 8000:8000 --env-file .env fastapi-virustotal
```
opcion 2 usar docker Compose, ejecuta:
```bash
docker-compose up
```

## Supociciones 

1.Tiempo de espera para el informe:
El servicio espera 15 segundos después de escanear el archivo antes de intentar obtener el informe. 

2.Tamaño máximo de archivo:
FastAPI maneja archivos de hasta 100 MB por defecto.