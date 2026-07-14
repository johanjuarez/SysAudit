"""
Obtiene información del software instalado.
"""

import platform
import winreg


def get_software_info():

    return {

        "operating_system": get_operating_system(),

        "installed_programs": get_installed_programs()

    }


def get_operating_system():

    return {

        "name": platform.system(),

        "release": platform.release(),

        "version": platform.version(),

        "architecture": platform.machine()

    }


def get_installed_programs():

    programs = []

    registry_paths = [

        (
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        ),

        (
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        ),

        (
            winreg.HKEY_CURRENT_USER,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        )

    ]


    for hive, path in registry_paths:

        programs.extend(
            read_registry(hive, path)
        )


    programs = clean_programs(programs)

    return categorize_programs(programs) 

def clean_programs(programs):

    programs = remove_duplicates(programs)

    programs = sort_programs(programs)

    return programs


def read_registry(hive, path):

    programs = []

    try:

        with winreg.OpenKey(hive, path) as registry:

            total = winreg.QueryInfoKey(registry)[0]

            for index in range(total):

                try:

                    subkey_name = winreg.EnumKey(
                        registry,
                        index
                    )

                    with winreg.OpenKey(registry, subkey_name) as subkey:

                        program = {

                            "name": get_registry_value(
                                subkey,
                                "DisplayName"
                            ),

                            "version": get_registry_value(
                                subkey,
                                "DisplayVersion"
                            ),

                            "publisher": get_registry_value(
                                subkey,
                                "Publisher"
                            ),

                            "install_date": get_registry_value(
                                subkey,
                                "InstallDate"
                            )

                        }

                        if is_valid_program(program):

                            programs.append(program)

                except OSError:

                    continue

    except FileNotFoundError:

        pass

    return programs

def get_registry_value(key, value_name):

    try:

        value, _ = winreg.QueryValueEx(
            key,
            value_name
        )

        return value

    except OSError:

        return ""


def sort_programs(programs):

    return sorted(

        programs,

        key=lambda program: program["name"].lower()

    )


def remove_duplicates(programs):

    unique_programs = []

    unique_keys = set()

    for program in programs:

        name = program.get("name", "").strip().lower()

        version = program.get("version", "").strip().lower()

        program_key = (name, version)

        if program_key in unique_keys:

            continue

        unique_keys.add(program_key)

        unique_programs.append(program)

    return unique_programs


def is_valid_program(program):

    name = program.get("name", "").strip()

    if not name:
        return False

    IGNORED_KEYWORDS = [

        "Update for",

        "Security Update",

        "Hotfix",

        "Language Pack",

        "Service Pack",

        "Windows Driver Package",

        "Microsoft Edge Update",

        "Microsoft Visual C++",

        "Microsoft OneDrive Setup",

        "WebView2 Runtime"

    ]

    for keyword in IGNORED_KEYWORDS:

        if keyword.lower() in name.lower():

            return False

    return True



def categorize_programs(programs):

    categories = {

        "Applications": [],

        "Browsers": [],

        "Development": [],

        "Frameworks": [],

        "Virtualization": [],

        "Security": [],

        "Updates": [],

        "Other": []

    }

    for program in programs:

        category = classify_program(program)

        categories[category].append(program)

    return categories



def classify_program(program):

    name = program.get("name", "").lower()


    # Navegadores

    if any(browser in name for browser in [

        "chrome",

        "edge",

        "firefox",

        "opera",

        "brave"

    ]):

        return "Browsers"


    # Desarrollo

    if any(dev in name for dev in [

        "python",

        "git",

        "visual studio",

        "visual studio code",

        "node",

        "jdk",

        "java",

        "intellij",

        "pycharm",

        "android studio"

    ]):

        return "Development"


    # Frameworks

    if any(framework in name for framework in [

        ".net",

        "runtime",

        "redistributable",

        "visual c++",

        "asp.net"

    ]):

        return "Frameworks"


    # Virtualización

    if any(vm in name for vm in [

        "docker",

        "vmware",

        "virtualbox",

        "hyper-v",

        "wsl"

    ]):

        return "Virtualization"


    # Seguridad

    if any(security in name for security in [

        "defender",

        "eset",

        "mcafee",

        "forticlient",

        "bitdefender",

        "kaspersky"

    ]):

        return "Security"


    # Actualizaciones

    if "kb" in name or "update" in name:

        return "Updates"


    return "Applications"