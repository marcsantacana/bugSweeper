def scan_vulnerabilities(url):
    """Escanea una URL en busca de vulnerabilidades comunes."""
    print(f"Escaneando {url} en busca de vulnerabilidades...")
    # Aquí iría la lógica para detectar vulnerabilidades como SQLi, XSS, etc.
    vulnerabilities = {
        "SQL Injection": False,
        "XSS": True,
        "CSRF": False,
    }
    for vuln, found in vulnerabilities.items():
        print(f"{vuln}: {'Encontrado' if found else 'No encontrado'}")
    return vulnerabilities
