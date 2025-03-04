# FastAPI VirusTotal Scanner

Este es un servicio REST API construido con FastAPI que permite a los usuarios subir archivos y escanearlos en busca de malware utilizando la API de VirusTotal. El servicio está containerizado con Docker.

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

abrir en el navegador: 
http://localhost:8000/docs#/default/scan_file_scan_file__post

## Uso de la API

Escanear un archivo y obtener el informe automáticamente
Endpoint: POST /scan-file/

Descripción: Sube un archivo para escanearlo en VirusTotal y obtén el informe completo en una sola solicitud.

Ejemplo de solicitud:

```bash

curl -X POST -F "file=@/path/to/your/file" http://localhost:8000/scan-file/
```
Respuesta:

```json
{
  "scan_result": {
    "scan_id": "id",
    "sha1": "...",
    "sha256": "...",
    "md5": "...",
    "permalink": "https://www.virustotal.com/file/.../analysis/..."
  },
  "report_result": {
    "scan_id": "id",
    "sha1": "...",
    "sha256": "...",
    "md5": "...",
    "permalink": "https://www.virustotal.com/file/.../analysis/...",
    "positives": 3,
    "total": 70,
    "scans": {
      "Antivirus1": {"detected": true, "result": "Malware"},
      "Antivirus2": {"detected": false, "result": null},
      ...
    }
  }
}
```
## Supociciones 

1.Tiempo de espera para el informe:
El servicio espera 15 segundos después de escanear el archivo antes de intentar obtener el informe. 

2.Tamaño máximo de archivo:
FastAPI maneja archivos de hasta 100 MB por defecto.
