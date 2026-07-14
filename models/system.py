from dataclasses import dataclass


@dataclass
class SystemInfo:
    computer_name: str = ""
    user: str =""
    manufacturer: str = ""
    model: str = ""
    serial_number: str = ""
    operating_system: str = ""
    version: str = ""
    build: str = ""
    architecture: str = ""
    last_boot: str = ""
    uptime: str = ""
