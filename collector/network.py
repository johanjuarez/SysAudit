"""
Obtiene información de red.
"""

import psutil
import socket
import wmi


wmi_connection = wmi.WMI()


def get_network_info():

    return {

        "hostname": get_hostname(),
        "interfaces": get_interfaces()

    }


def get_hostname():

    return socket.gethostname()


def get_interfaces():

    interfaces = []

    adapters = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    for name, addresses in adapters.items():

        interface = {

            "name": name

        }

        for address in addresses:

            if address.family == socket.AF_INET:
                interface["ipv4"] = address.address
                interface["mask"] = address.netmask
            elif address.family == psutil.AF_LINK:
                interface["mac"] = address.address

        status = stats.get(name)
        if status:

            interface["status"] = (
                "Conectado"
                if status.isup
                else "Desconectado"
            )

            interface["speed"] = f"{status.speed} Mbps"

        interface["type"] = get_connection_type(name)
        if is_valid_interface(interface):
            interfaces.append(interface)

    return interfaces


def is_valid_interface(interface):

    ip = interface.get("ipv4", "")
    if not ip:
        return False

    if ip.startswith("127."):
        return False

    if ip.startswith("169.254."):
        return False

    return True


def get_connection_type(name):

    name = name.lower()

    if "wi-fi" in name or "wireless" in name or "wlan" in name:
        return "Wi-Fi"

    if "ethernet" in name:
        return "Ethernet"

    return "Otro"