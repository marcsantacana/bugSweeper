# bugSweeper

BugSweeper es una herramienta de línea de comandos escrita en Python, diseñada para ayudar a los investigadores de seguridad en la simulación y detección de vulnerabilidades en aplicaciones y sistemas. Está orientada a la práctica del Bug Bounty, proporcionando funcionalidades útiles para identificar y reportar problemas de seguridad.

## Características

- **Escaneo de Vulnerabilidades**:
  - Analiza aplicaciones en busca de vulnerabilidades comunes como SQL Injection, XSS, CSRF, entre otras.
  - Genera reportes detallados con información sobre las vulnerabilidades encontradas.

- **Enumeración de Recursos**:
  - Permite enumerar directorios, subdominios y endpoints de una aplicación web.
  - Incluye soporte para diccionarios personalizados.

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
  ```bash
  bugSweeper scan --url https://example.com
  ```

- **Enumeración de subdominios**:
  ```bash
  bugSweeper enum --subdomains --domain example.com
  ```

  - **Enumeración de directorios**:
  ```bash
  bugSweeper enum --directories --url https://example.com
  ```

- **Generación de reportes**:
Formato JSON
  ```bash
  bugSweeper report --output report.json
  ```
Formato Markdown
  ```markdown
  bugSweeper report --output report.md
  ```

## Estructura del Proyecto

```
BugSweeper/
├── bugsweeper/
│   ├── __init__.py       # Archivo de inicialización del paquete
│   ├── main.py           # Punto de entrada del programa
│   ├── scanner.py        # Lógica para escaneo de vulnerabilidades
│   ├── enumerator.py     # Lógica para enumeración de recursos
│   └── reporter.py       # Lógica para generación de reportes
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
