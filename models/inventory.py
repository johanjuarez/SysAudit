from dataclasses import dataclass, field

from models.system import SystemInfo
from models.hardware import HardwareInfo


@dataclass
class Inventory:

    system: SystemInfo = field(default_factory=SystemInfo)

    hardware: HardwareInfo = field(default_factory=HardwareInfo)

    network: dict = field(default_factory=dict)

    software: dict = field(default_factory=dict)

    security: dict = field(default_factory=dict)