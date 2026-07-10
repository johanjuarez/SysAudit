from .common import write_section, write_field


def write_software(file, software):

    write_section(file, "Software")
    write_operating_system(file, software["operating_system"])



def write_operating_system(file, operating_system):

    file.write("\nSistema Operativo\n")

    write_field(file, "Nombre", operating_system["name"])
    write_field(file, "Versión", operating_system["release"])
    write_field(file, "Build", operating_system["version"])
    write_field(file, "Arquitectura", operating_system["architecture"])

    