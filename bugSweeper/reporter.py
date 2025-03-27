import json

def generate_report(output_file, data=None):
    """Genera un reporte en formato JSON o Markdown."""
    if output_file.endswith(".json"):
        with open(output_file, "w") as f:
            json.dump(data or {}, f, indent=4)
    elif output_file.endswith(".md"):
        with open(output_file, "w") as f:
            f.write("# Reporte de Vulnerabilidades\n")
            for key, value in (data or {}).items():
                f.write(f"## {key}\n{value}\n")
    else:
        raise ValueError("Formato de archivo no soportado. Use .json o .md")