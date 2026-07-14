from models.inventory import Inventory

from collector.system import get_system_info
from collector.hardware import get_hardware_info
from collector.network import get_network_info
from collector.software import get_software_info
from collector.security import get_security_info
from app.utils import safe_execute


def collect_inventory():

    inventory = Inventory()

    inventory.system = safe_execute(
        get_system_info,
        {}
    )

    inventory.hardware = safe_execute(
        get_hardware_info,
        {}
    )

    inventory.network = safe_execute(
        get_network_info,
        {}
    )

    inventory.software = safe_execute(
        get_software_info,
        {}
    )

    inventory.security = safe_execute(
        get_security_info,
        {}
    )


    return inventory