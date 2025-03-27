import requests
import time

def scan_vulnerabilities(url):
    """Escanea una URL en busca de vulnerabilidades comunes."""
    vulnerabilities = {
        "SQL Injection": test_sql_injection(url),
        "XSS": test_xss(url),
        "CSRF": test_csrf(url),
    }
    return vulnerabilities

def test_sql_injection(url):
    """Prueba básica para detectar SQL Injection."""
    payload = "' OR '1'='1"
    try:
        response = requests.get(url, params={"q": payload})
        if "error" in response.text or "syntax" in response.text:
            return True
    except requests.RequestException:
        pass
    return False

def test_xss(url):
    """Prueba básica para detectar XSS."""
    payload = "<script>alert('XSS')</script>"
    try:
        response = requests.get(url, params={"q": payload})
        if payload in response.text:
            return True
    except requests.RequestException:
        pass
    return False

def test_csrf(url):
    """Prueba básica para detectar CSRF."""
    try:
        response = requests.get(url)
        if "csrf" not in response.headers.get("Set-Cookie", "").lower():
            return True
    except requests.RequestException:
        pass
    return False

def analyze_http_headers(url):
    """Analiza las cabeceras HTTP de una URL."""
    try:
        response = requests.get(url)
        headers = response.headers
        issues = {}

        # Verificar cabeceras de seguridad
        if "Content-Security-Policy" not in headers:
            issues["Content-Security-Policy"] = "Falta la cabecera CSP."
        if "X-Frame-Options" not in headers:
            issues["X-Frame-Options"] = "Falta la cabecera X-Frame-Options."
        if "Strict-Transport-Security" not in headers:
            issues["Strict-Transport-Security"] = "Falta la cabecera HSTS."

        return issues
    except requests.RequestException as e:
        return {"Error": str(e)}

def recursive_scan(urls, delay=2):
    """Realiza un escaneo recursivo en una lista de URLs."""
    results = {}
    for url in urls:
        print(f"Escaneando: {url}")
        results[url] = scan_vulnerabilities(url)
        time.sleep(delay)  # Espera entre escaneos para evitar ser bloqueado
    return results