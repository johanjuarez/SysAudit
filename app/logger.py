"""
Configuración del sistema de logs de SysAudit.
"""

import logging

from config import LOG_DIR


LOG_FILE = LOG_DIR / "sysaudit.log"


def setup_logger():

    logging.basicConfig(

        filename=LOG_FILE,

        level=logging.INFO,

        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(message)s"
        ),

        datefmt="%Y-%m-%d %H:%M:%S"

    )


    return logging.getLogger("SysAudit")