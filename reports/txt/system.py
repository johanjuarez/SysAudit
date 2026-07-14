from reports.txt.common import write_section, write_field


def write_system(file, system):

    write_section(file, "Sistema")

    write_basic_system(file, system)


def write_basic_system(file, sys):

    file.write("\nSistema del equipo\n")

    write_field(file,"Nombre computador",sys.computer_name)
    write_field(file,"Usuario",sys.user)
    write_field(file,"Fabricante",sys.manufacturer)
    write_field(file,"Modelo",sys.model)
    write_field(file,"Numero serial",sys.serial_number)
    write_field(file,"Sistema operativo",sys.operating_system)
    write_field(file,"Version",sys.version)
    write_field(file,"Build",sys.build)
    write_field(file,"Arquitectura",sys.architecture)
    write_field(file,"Ultimo inicio",sys.last_boot)
    write_field(file,"Tiempo actividad",sys.uptime)