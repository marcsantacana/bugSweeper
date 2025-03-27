import argparse
from .scanner import scan_vulnerabilities, analyze_http_headers, recursive_scan
from .enumerator import enumerate_subdomains, enumerate_directories, save_subdomains_to_file
from .reporter import generate_report
from rich.console import Console

console = Console()

def main():
    parser = argparse.ArgumentParser(description="BugSweeper CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Comando para escanear vulnerabilidades
    scan_parser = subparsers.add_parser("scan")
    scan_parser.add_argument("--url", required=True, help="URL a escanear")
    scan_parser.add_argument("--recursive", action="store_true", help="Habilitar escaneo recursivo")
    scan_parser.add_argument("--urls", nargs="+", help="Lista de URLs para escaneo recursivo")

    # Comando para enumerar recursos
    enum_parser = subparsers.add_parser("enum")
    enum_parser.add_argument("--subdomains", action="store_true", help="Enumerar subdominios")
    enum_parser.add_argument("--directories", action="store_true", help="Enumerar directorios")
    enum_parser.add_argument("--domain", help="Dominio para enumerar subdominios")
    enum_parser.add_argument("--url", help="URL para enumerar directorios")

    # Comando para generar reportes
    report_parser = subparsers.add_parser("report")
    report_parser.add_argument("--output", required=True, help="Archivo de salida para el reporte")

    args = parser.parse_args()

    if args.command == "scan":
        console.print("[bold cyan]Iniciando escaneo de vulnerabilidades...[/bold cyan]")
        if args.recursive and args.urls:
            results = recursive_scan(args.urls)
            console.print(f"Resultados del escaneo recursivo: {results}")
        else:
            results = scan_vulnerabilities(args.url)
            headers_issues = analyze_http_headers(args.url)
            console.print(f"Resultados del escaneo: {results}")
            console.print(f"Problemas de cabeceras HTTP: {headers_issues}")

    elif args.command == "enum":
        if args.subdomains and args.domain:
            console.print("[bold cyan]Enumerando subdominios...[/bold cyan]")
            subdomains = enumerate_subdomains(args.domain, ["www", "api", "test"])
            console.print(f"Subdominios encontrados: {subdomains}")
            save_subdomains_to_file(subdomains, output_file="subdomains.txt")
        if args.directories and args.url:
            console.print("[bold cyan]Enumerando directorios...[/bold cyan]")
            directories = enumerate_directories(args.url, ["admin", "login", "dashboard"])
            console.print(f"Directorios encontrados: {directories}")

    elif args.command == "report":
        console.print("[bold cyan]Generando reporte...[/bold cyan]")
        generate_report(args.output)
        console.print(f"Reporte generado en: {args.output}")

    else:
        console.print("[bold red]Comando no reconocido. Usa --help para más información.[/bold red]")

if __name__ == "__main__":
    main()