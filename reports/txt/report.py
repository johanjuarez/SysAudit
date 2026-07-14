from pathlib import Path
from datetime import datetime
from config import (APP_NAME, APP_DESCRIPTION, AUTHOR, VERSION)

from reports.txt.common import write_separator
from reports.txt.hardware import write_hardware
from reports.txt.network import write_network
from reports.txt.software import write_software
from reports.txt.system import write_system


OUTPUT_FOLDER = Path("output/txt/")


def generate_txt_report(inventory):

    OUTPUT_FOLDER.mkdir(exist_ok=True)

    filename = (
        f"Inventory_{datetime.now():%Y%m%d_%H%M%S}.txt"
    )

    report_path = OUTPUT_FOLDER / filename

    with open(report_path, "w", encoding="utf-8") as file:

        write_header(file)
        write_system(file, inventory.system)
        write_hardware(file, inventory.hardware)
        write_network(file, inventory.network)
        write_software(file, inventory.software)

        write_footer(file)

    return report_path


def write_header(file):

    write_separator(file)

    file.write(f"{APP_NAME.upper()} - REPORTE DE EQUIPOS\n")

    write_separator(file)

    file.write(f"Version: {VERSION}\n")
    file.write(f"Descripcion: {APP_DESCRIPTION}\n")
    file.write(f"Autor: {AUTHOR}\n")
    file.write(f"Fecha de generacion: {datetime.now():%Y-%m-%d %H:%M:%S}\n")


def write_footer(file):

    file.write("\n")

    write_separator(file)

    file.write("Fin del reporte\n")