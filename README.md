# BugSweeper v.01.00

BugSweeper es una herramienta de línea de comandos escrita en Python, diseñada para ayudar a los investigadores de seguridad en la simulación y detección de vulnerabilidades en aplicaciones y sistemas. Está orientada a la práctica del Bug Bounty, proporcionando funcionalidades útiles para identificar y reportar problemas de seguridad.

## Características

- **Escaneo de Vulnerabilidades**:
  - Analiza aplicaciones en busca de vulnerabilidades comunes como SQL Injection, XSS, CSRF, entre otras.
  - Realiza análisis de cabeceras HTTP para identificar configuraciones inseguras.
  - Soporte para escaneo recursivo en múltiples URLs.

- **Enumeración de Recursos**:
  - Permite enumerar directorios, subdominios y endpoints de una aplicación web.
  - Incluye soporte para diccionarios personalizados.
  - Guarda los subdominios encontrados en un archivo `.txt`.

- **Pruebas de Seguridad Automatizadas**:
  - Realiza pruebas básicas de seguridad como detección de cabeceras HTTP inseguras o configuraciones incorrectas.

- **Generación de Reportes**:
  - Crea reportes en formato Markdown o JSON para facilitar el envío a programas de Bug Bounty.

- **Modo Educativo**:
  - Incluye explicaciones sobre las vulnerabilidades detectadas y cómo mitigarlas.

## Requisitos

- **Lenguaje**: Python 3.8 o superior.
- **Entorno**: Compatible únicamente con terminal.
- **Dependencias**: Listadas en el archivo `requirements.txt`.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/marcsantacana/bugSweeper.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd BugSweeper
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta el programa desde la terminal con los siguientes comandos:

- **Escaneo de vulnerabilidades**:
  Escanea una URL en busca de vulnerabilidades comunes:
  ```bash
  python -m bugSweeper.main scan --url https://example.com
  ```
  Realiza un escaneo recursivo en múltiples URLs:
  ```bash
  python -m bugSweeper.main scan --recursive --urls https://example1.com https://example2.com
  ```

- **Enumeración de subdominios**:
  ```bash
  python -m bugSweeper.main enum --subdomains --domain example.com
  ```

- **Enumeración de directorios**:
    
  Los subdominios encontrados se guardarán automáticamente en un archivo subdomains.txt.
  ```bash
  python -m bugSweeper.main enum --directories --url https://example.com
  ```

- **Detección de Broken Authentication**:

  ```python
  from enumerator import detect_broken_authentication

  url = "http://example.com"
  common_credentials = [("admin", "admin"), ("root", "toor"), ("user", "password")]
  detect_broken_authentication(url, common_credentials)
  ```

  Si se detecta un problema, se imprimirá un mensaje como:

  ```
  [!] Broken Authentication detected at http://example.com/login with credentials admin:admin
  ```

- **Detección de Configuraciones Inseguras**:

  ```python
  from enumerator import detect_misconfigurations

  url = "http://example.com"
  sensitive_files = [".env", "config.php", "backup.zip"]
  detect_misconfigurations(url, sensitive_files)
  ```

  Si se detecta una configuración insegura, se imprimirá un mensaje como:

  ```
  [!] Misconfiguration detected: http://example.com/.env is accessible.
  ```

### Generación de reportes

### Generación de Reportes

#### Ejemplo de Resumen en la Terminal y Reporte Detallado

```python
from reporter import generate_report

data = {
    "Subdomains": "3 subdominios encontrados:\n- http://www.example.com\n- http://mail.example.com\n- http://ftp.example.com",
    "Directories": "2 directorios accesibles:\n- http://example.com/admin\n- http://example.com/login",
    "Broken Authentication": "1 vulnerabilidad detectada:\n- Credenciales admin:admin funcionan en http://example.com/login",
    "Misconfigurations": "Archivo .env accesible:\n- http://example.com/.env"
}

generate_report("detailed_report.md", data)
```

#### Salida en la Terminal:
```plaintext
=== Resumen del Reporte ===
- Subdomains: 3 subdominios encontrados:
- Directories: 2 directorios accesibles:
- Broken Authentication: 1 vulnerabilidad detectada:
- Misconfigurations: Archivo .env accesible:
===========================
```

#### Contenido del Archivo `detailed_report.md`:
```markdown
# Reporte de Vulnerabilidades
## Subdomains
3 subdominios encontrados:
- http://www.example.com
- http://mail.example.com
- http://ftp.example.com

## Directories
2 directorios accesibles:
- http://example.com/admin
- http://example.com/login

## Broken Authentication
1 vulnerabilidad detectada:
- Credenciales admin:admin funcionan en http://example.com/login

## Misconfigurations
Archivo .env accesible:
- http://example.com/.env
```

## Estructura del Proyecto

```
BugSweeper/
├── bugSweeper/
│   ├── __init__.py       # Archivo de inicialización del paquete
│   ├── main.py           # Punto de entrada del programa
│   ├── scanner.py        # Lógica para escaneo de vulnerabilidades
│   ├── enumerator.py     # Lógica para enumeración de recursos
│   ├── reporter.py       # Lógica para generación de reportes
│   └── ui.py             # Interfaz gráfica minimalista para la terminal
├── README.md             # Documentación del proyecto
├── requirements.txt      # Dependencias del proyecto
└── setup.py              # Configuración para instalar el programa
```

## Funcionalidades Futuras

- Integración con APIs de herramientas de seguridad como OWASP ZAP.
- Soporte para pruebas de fuerza bruta en formularios de autenticación.
- Escaneo de aplicaciones móviles.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar la herramienta o encuentras un problema, abre un issue o envía un pull request.

## Licencia

Este proyecto está licenciado bajo la MIT License.

## Autor

Marc Santacana
