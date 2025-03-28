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
