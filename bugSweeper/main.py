import argparse
from .scanner import scan_vulnerabilities
from .enumerator import enumerate_subdomains, enumerate_directories
from .reporter import generate_report
from .ui import show_menu, show_scan_progress, show_results
from rich.console import Console

console = Console()

def main():
    parser = argparse.ArgumentParser(description="BugSweeper CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Comando para escanear vulnerabilidades
    scan_parser = subparsers.add_parser("scan")
    scan_parser.add_argument("--url", required=True, help="URL a escanear")

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
        urls = [args.url]
        show_scan_progress(urls)
        results = scan_vulnerabilities(args.url)
        show_results(results)
    elif args.command == "enum":
        if args.subdomains and args.domain:
            console.print("[bold cyan]Enumerando subdominios...[/bold cyan]")
            subdomains = enumerate_subdomains(args.domain, ["www", "api", "test"])
            console.print(f"Subdominios encontrados: {subdomains}")
        if args.directories and args.url:
            console.print("[bold cyan]Enumerando directorios...[/bold cyan]")
            directories = enumerate_directories(args.url, ["admin", "login", "dashboard"])
            console.print(f"Directorios encontrados: {directories}")
    elif args.command == "report":
        console.print("[bold cyan]Generando reporte...[/bold cyan]")
        generate_report(args.output)
        console.print(f"Reporte generado en: {args.output}")
    else:
        show_menu()

if __name__ == "__main__":
    main()