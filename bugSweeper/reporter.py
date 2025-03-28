import json

def generate_report(output_file, data=None):
    """Genera un reporte en formato JSON o Markdown y muestra un resumen en la terminal."""
    data = data or {}

    # Mostrar un resumen en la terminal
    print("=== Resumen del Reporte ===")
    for key, value in data.items():
        print(f"- {key}: {value.splitlines()[0]}")  # Muestra solo la primera línea de cada sección
    print("===========================")

    # Generar el reporte detallado
    if output_file.endswith(".json"):
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
    elif output_file.endswith(".md"):
        with open(output_file, "w") as f:
            f.write("# Reporte de Vulnerabilidades\n")
            for key, value in data.items():
                f.write(f"## {key}\n{value}\n")
    else:
        raise ValueError("Formato de archivo no soportado. Use .json o .md")
    