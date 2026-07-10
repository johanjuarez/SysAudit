from models.inventory import Inventory

from collector.system import get_system_info
from collector.hardware import get_hardware_info
from collector.network import get_network_info
from collector.software import get_software_info
from collector.security import get_security_info


def collect_inventory():

    inventory = Inventory()

    inventory.system = get_system_info()

    inventory.hardware = get_hardware_info()

    inventory.network = get_network_info()

    inventory.software = get_software_info()

    inventory.security = get_security_info()

    return inventory