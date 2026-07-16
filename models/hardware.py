from dataclasses import dataclass, field
from typing import List


@dataclass
class CPUInfo:

    model: str = ""
    manufacturer: str = ""
    cores: int = 0
    threads: int = 0
    max_frequency: float = 0.0


@dataclass
class MemoryModule:

    manufacturer: str = ""
    capacity: float = 0.0
    speed: int = 0
    location: str = ""
    serial: str = ""


@dataclass
class MemoryInfo:

    total: float = 0.0
    available: float = 0.0
    used_percent: float = 0.0

    modules: List[MemoryModule] = field(default_factory=list)


@dataclass
class MotherboardInfo:

    model: str = ""
    manufacturer: str = ""
    serial: str = ""


@dataclass
class GPUInfo:

    manufacturer: str = ""
    name: str = ""
    vram: float = 0.0
    driver_version: str = ""
    resolution: str = ""


@dataclass
class BatteryInfo:

    available: bool = False
    percentage: int = 0
    charging: bool = False


@dataclass
class DiskInfo:

    model: str = ""
    manufacturer: str = ""
    interface: str = ""
    serial: str = ""
    size: float = 0.0


@dataclass
class PartitionInfo:

    device: str = ""
    filesystem: str = ""
    total: float = 0.0
    free: float = 0.0
    used_percent: float = 0.0


@dataclass
class StorageInfo:

    disks: List[DiskInfo] = field(default_factory=list)
    partitions: List[PartitionInfo] = field(default_factory=list)


@dataclass
class HardwareInfo:

    cpu: CPUInfo = field(default_factory=CPUInfo)
    memory: MemoryInfo = field(default_factory=MemoryInfo)
    motherboard: MotherboardInfo = field(default_factory=MotherboardInfo)
    gpu: GPUInfo = field(default_factory=GPUInfo)
    battery: BatteryInfo = field(default_factory=BatteryInfo)
    storage: StorageInfo = field(default_factory=StorageInfo)