import requests

def enumerate_subdomains(domain, wordlist, output_file="subdomains.txt"):
    """Enumera subdominios de un dominio dado y los guarda en un archivo."""
    subdomains = []
    with open(output_file, "w") as file:
        for subdomain in wordlist:
            url = f"http://{subdomain}.{domain}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    subdomains.append(url)
                    file.write(url + "\n")  # Escribe el subdominio en el archivo
            except requests.ConnectionError:
                pass
    return subdomains

def enumerate_directories(url, wordlist):
    """Enumera directorios en una URL dada."""
    directories = []
    for directory in wordlist:
        full_url = f"{url}/{directory}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                directories.append(full_url)
        except requests.ConnectionError:
            pass
    return directories

def detect_broken_authentication(url, common_credentials):
    """
    Detecta problemas de autenticación rota probando credenciales comunes.
    """
    vulnerable = False
    login_url = f"{url}/login"  # Supongamos que la página de login está en /login
    for username, password in common_credentials:
        try:
            response = requests.post(login_url, data={"username": username, "password": password})
            if response.status_code == 200 and "Welcome" in response.text:  # Ajustar según el texto esperado
                print(f"[!] Broken Authentication detected at {login_url} with credentials {username}:{password}")
                vulnerable = True
        except requests.ConnectionError:
            pass
    return vulnerable

def detect_misconfigurations(url, sensitive_files):
    """
    Detecta configuraciones inseguras buscando archivos sensibles.
    """
    misconfigurations = []
    for file in sensitive_files:
        file_url = f"{url}/{file}"
        try:
            response = requests.get(file_url)
            if response.status_code == 200:
                print(f"[!] Misconfiguration detected: {file_url} is accessible.")
                misconfigurations.append(file_url)
        except requests.ConnectionError:
            pass
    return misconfigurations