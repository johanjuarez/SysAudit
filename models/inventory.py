from dataclasses import dataclass, field


@dataclass
class Inventory:

    system: dict = field(default_factory=dict)
    hardware: dict = field(default_factory=dict)
    network: dict = field(default_factory=dict)
    software: dict = field(default_factory=dict)
    security: dict = field(default_factory=dict)