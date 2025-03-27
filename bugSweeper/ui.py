from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()

def show_menu():
    """Muestra el menú principal."""
    console.print("[bold cyan]Bienvenido a BugSweeper[/bold cyan]")
    console.print("Selecciona una opción:")
    console.print("[1] Escanear vulnerabilidades")
    console.print("[2] Enumerar recursos")
    console.print("[3] Generar reporte")
    console.print("[4] Salir")

def show_scan_progress(urls):
    """Muestra una barra de progreso para el escaneo."""
    with Progress() as progress:
        task = progress.add_task("[cyan]Escaneando vulnerabilidades...", total=len(urls))
        for url in urls:
            # Simula el escaneo de una URL
            progress.console.print(f"Escaneando: {url}")
            progress.advance(task)

def show_results(results):
    """Muestra los resultados en una tabla."""
    table = Table(title="Resultados del Escaneo")
    table.add_column("Vulnerabilidad", style="red", justify="left")
    table.add_column("Estado", style="green", justify="left")

    for vuln, status in results.items():
        table.add_row(vuln, "Encontrado" if status else "No encontrado")

    console.print(table)