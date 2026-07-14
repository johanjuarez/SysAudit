from dataclasses import dataclass, field

from models.system import SystemInfo


@dataclass
class Inventory:

    system: SystemInfo = field(default_factory=SystemInfo)

    hardware: dict = field(default_factory=dict)

    network: dict = field(default_factory=dict)

    software: dict = field(default_factory=dict)

    security: dict = field(default_factory=dict)