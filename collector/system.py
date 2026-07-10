import os
import platform
from datetime import datetime, timedelta


import psutil
import wmi


def get_system_info():

    c = wmi.WMI()

    computer = c.Win32_ComputerSystem()[0]
    bios = c.Win32_BIOS()[0]
    os_info = c.Win32_OperatingSystem()[0]

    boot_time = datetime.fromtimestamp(
        psutil.boot_time()
    )
    
    uptime = datetime.now() - boot_time

    return {

        "computer_name": platform.node(),
        "user": os.getlogin(),
        "manufacturer": computer.Manufacturer,
        "model": computer.Model,
        "serial_number": bios.SerialNumber,
        "operating_system": os_info.Caption,
        "version": os_info.Version,
        "build": os_info.BuildNumber,
        "architecture": platform.machine(),
        "last_boot": str(boot_time),

        "uptime": str(
            timedelta(
                seconds=int(
                    uptime.total_seconds()
                )
            )
        )

    }