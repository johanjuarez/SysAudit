"""
CONFIGURACION BASE DE LA APLICACION
"""

from pathlib import Path


### informacion de la aplicacion ###

APP_NAME = "SysAudit"
APP_DESCRIPTION = "Profesional system Inventory & Diagnostics"
AUTHOR = "Johan Gonzalez"
VERSION = "1.0.0"


### DIRECTORIOS ###

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "output"
PDF_DIR = OUTPUT_DIR / "pdf"
TXT_DIR = OUTPUT_DIR / "txt"
LOG_DIR = OUTPUT_DIR / "logs"

# Crear carpetas automáticamente

for directory in (OUTPUT_DIR, PDF_DIR, TXT_DIR, LOG_DIR):
    directory.mkdir(parents=True, exist_ok=True)


### Formatos disponibles ###

SUPPORTED_FORMATS = [
    "pdf",
    "txt"
]


### MODULOS DISPONIBLES ###

AVAILABLE_MODULES = {

    "system": True,
    "hardware": True,
    "network": True,

    "software": False,
    "security": False,
    "services": False,
    "processes": False,
    "printers": False,
    "usb": False

}
