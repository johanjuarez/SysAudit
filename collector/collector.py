from models.inventory import Inventory

from collector.system import get_system_info
from collector.hardware import get_hardware_info
from collector.network import get_network_info
from collector.software import get_software_info
from collector.security import get_security_info
from app.utils import safe_execute


def collect_inventory():

    return {

        "system": safe_execute(get_system_info,{}),
        "hardware": safe_execute(get_hardware_info,{}),
        "network": safe_execute(get_network_info,{}),
        "software": safe_execute(get_software_info,{})
        
    }