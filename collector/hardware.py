"""
Módulo encargado de recolectar información del hardware del equipo.
"""
from models.hardware import (HardwareInfo, CPUInfo, MemoryInfo, MemoryModule, 
    MotherboardInfo, GPUInfo,BatteryInfo, DiskInfo, PartitionInfo, StorageInfo)


import psutil
import wmi


# Conexión WMI
wmi_connection = wmi.WMI()



# CPU

def get_cpu():

    cpu = wmi_connection.Win32_Processor()[0]

    return CPUInfo(

        model=cpu.Name.strip(),
        manufacturer=cpu.Manufacturer,
        cores=cpu.NumberOfCores,
        threads=cpu.NumberOfLogicalProcessors,
        max_frequency=cpu.MaxClockSpeed

    )


# MEMORIA RAM

def get_memory():

    memory = psutil.virtual_memory()
    modules = []

    for ram in wmi_connection.Win32_PhysicalMemory():

        modules.append({

            "manufacturer": ram.Manufacturer,
            "capacity": round(
                int(ram.Capacity) / (1024 ** 3),
                2
            ),
            "speed": ram.Speed,
            "slot": ram.DeviceLocator,
            "serial": ram.SerialNumber

        })


    return {

        "total": round(
            memory.total / (1024 ** 3),
            2
        ),
        "available": round(
            memory.available / (1024 ** 3),
            2
        ),
        "used_percent": memory.percent,
        "modules": modules

    }


# MOTHERBOARD

def get_motherboard():

    motherboard = wmi_connection.Win32_BaseBoard()[0]

    return {

        "manufacturer": motherboard.Manufacturer,
        "model": motherboard.Product,
        "serial": motherboard.SerialNumber
    }


# BIOS

def get_bios():

    bios = wmi_connection.Win32_BIOS()[0]

    return {
        "manufacturer": bios.Manufacturer,
        "version": bios.Version,
        "serial": bios.SerialNumber
    }


# STORAGE

def get_storage():

    disks = []


    for disk in wmi_connection.Win32_DiskDrive():


        disk_info = {
            "model": disk.Model,
            "manufacturer": disk.Manufacturer,
            "interface": disk.InterfaceType,
            "serial": disk.SerialNumber,
            "size": round(

                int(disk.Size) / (1024 ** 3),
                2
            ) if disk.Size else 0,


        }


        disks.append(disk_info)


    return disks


def get_partitions():

    partitions = []


    for partition in psutil.disk_partitions():

        try:

            usage = psutil.disk_usage(
                partition.mountpoint
            )


            partitions.append({

                "device": partition.device,
                "filesystem": partition.fstype,
                "total": round(
                    usage.total / (1024 ** 3),
                    2
                ),
                "free": round(
                    usage.free / (1024 ** 3),
                    2
                ),
                "used_percent":
                    usage.percent
            })


        except PermissionError:

            continue


    return partitions




def get_gpu():

    gpu_list = []


    for gpu in wmi_connection.Win32_VideoController():

        gpu_list.append({

            "name": gpu.Name,
            "manufacturer": gpu.AdapterCompatibility,
            "vram": round(
                gpu.AdapterRAM / (1024 ** 3),
                2
            ) if gpu.AdapterRAM else 0,

            "driver_version": gpu.DriverVersion,
            "resolution": f"{gpu.CurrentHorizontalResolution}x{gpu.CurrentVerticalResolution}"

        })


    return gpu_list



def get_battery():

    battery = psutil.sensors_battery()


    if battery is None:

        return {
            "available": False,
            "message": "No se detectó batería"
        }


    if battery.secsleft < 0:
        time_left = "No disponible"

    else:
        hours = battery.secsleft // 3600
        minutes = (
            battery.secsleft % 3600
        ) // 60
        time_left = (
            f"{int(hours)}h {int(minutes)}m"
        )


    return {

        "available": True,
        "percentage": f"{battery.percent}%",
        "charging":
            "Sí"
            if battery.power_plugged
            else "No",

        # "time_left": time_left

    }

# HARDWARE PRINCIPAL

def get_hardware_info():

    return {

        "cpu": get_cpu(),
        "memory": get_memory(),
        "motherboard": get_motherboard(),
        "bios": get_bios(),
        "storage": get_storage(),
        "partitions": get_partitions(),  
        "gpu": get_gpu(),
        "battery": get_battery()
    }