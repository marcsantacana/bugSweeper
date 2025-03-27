import argparse
from .scanner import scan_vulnerabilities
from .enumerator import enumerate_subdomains, enumerate_directories
from .reporter import generate_report

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
        scan_vulnerabilities(args.url)
    elif args.command == "enum":
        if args.subdomains and args.domain:
            print(enumerate_subdomains(args.domain, ["www", "api", "test"]))
        if args.directories and args.url:
            print(enumerate_directories(args.url, ["admin", "login", "dashboard"]))
    elif args.command == "report":
        generate_report(args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()