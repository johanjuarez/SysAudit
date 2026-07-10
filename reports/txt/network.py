from .common import write_section, write_field


def write_network(file, network):

    write_section(file, "Red")

    write_field(file, "Nombre del equipo", network["hostname"])

    for interface in network["interfaces"]:

        file.write("\n")

        write_field(file, "Adaptador", interface["name"])
        write_field(file, "MAC", interface["mac"])
        write_field(file, "Direccion IPv4", interface["ipv4"])
        write_field(file, "Mascara de red", interface["mask"])
        write_field(file, "Estado", interface["status"])
        write_field(file, "Velocidad", interface["speed"])
        write_field(file, "Tipo", interface["type"])


            








    #         def write_gpu(file,gpu):
    # file.write("\nGPU\n")
    # for index, value in enumerate(gpu, start=1):
    #     write_field(file, "Fabricante", value["manufacturer"])
    #     write_field(file, "Nombre", value['name'])
    #     write_field(file, "VRAM", value['vram'])
    #     write_field(file, "Version driver", value["driver_version"])
    #     write_field(file, "Resolucion", value["resolution"])