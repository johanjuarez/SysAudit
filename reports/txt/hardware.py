from reports.txt.common import write_section, write_field


def write_hardware(file, hardware):

    write_section(file, "Hardware")
    write_cpu(file, hardware["cpu"])
    write_bios(file,hardware["bios"])
    write_memory(file, hardware["memory"])
    write_motherboard(file, hardware["motherboard"])
    write_gpu(file,hardware["gpu"])
    write_battery(file,hardware["battery"])
    write_storage(file,hardware["storage"])
    write_partitions(file,hardware["partitions"])


def write_cpu(file, cpu):

    file.write("\nProcesador\n")
    write_field(file,"Modelo",cpu.model)
    write_field(file,"Fabricante",cpu.manufacturer)
    write_field(file,"Nucleos",cpu.cores)
    write_field(file,"Hilos",cpu.threads)
    write_field(
        file,
        "Frecuencia maxima",
        f"{cpu.max_frequency} MHz"
    )

def write_bios(file,bios):
    file.write("\nBIOS\n")

    write_field(file,"Version",bios["version"])
    write_field(file,"Fabricante",bios["manufacturer"])
    write_field(file,"Serial",bios["serial"])


def write_memory(file, memory):

    file.write("\nMEMORIA\n")

    write_field(file,"Total",f"{memory.total} GB")
    write_field(file,"Disponible",f"{memory.available} GB")
    write_field(file,"Uso",f"{memory.used_percent} %")
    file.write("\nMódulos instalados\n")

    for index, module in enumerate(memory.modules, start=1):

        file.write(f"\nSlot {index}\n")

        write_field(file,"Fabricante",module.manufacturer)
        write_field(file,"Capacidad",f"{module.capacity} GB")
        write_field(file,"Velocidad",f"{module.speed} MHz")
        write_field(file,"Ubicación",module.location)
        write_field(file,"Serial",module.serial)

        
def write_motherboard(file,motherboard):
    file.write("\nPLACA MADRE\n")

    write_field(file,"Modelo",motherboard["model"])
    write_field(file,"Fabricante",motherboard["manufacturer"])
    write_field(file,"Serial",motherboard["serial"])


def write_gpu(file,gpu):
    file.write("\nGPU/Tarjeta grafica\n")
    for value in (gpu):
        write_field(file, "Fabricante", value["manufacturer"])
        write_field(file, "Nombre", value['name'])
        write_field(file, "VRAM//Memoria de video", value['vram'])
        write_field(file, "Version del controlador", value["driver_version"])
        write_field(file, "Resolucion", value["resolution"])

def write_battery(file, battery):

    file.write("\nBATERIA\n")

    write_field(file, "Disponible", "Sí" if battery["available"] else "No")
    write_field(file,"Porcentaje",battery["percentage"])
    write_field(file, "Cargando", "Sí" if battery["charging"] else "No")


def write_storage(file, storage):

    file.write("\nALMACENAMIENTO\n")

    for index, disk in enumerate(storage, start=1):

        file.write(f"\nDisco {index}\n")

        write_field(file,"Modelo",disk["model"])
        write_field(file,"Fabricante",disk["manufacturer"])
        write_field(file,"Interfaz",disk["interface"])
        write_field(file,"Número de serie",disk["serial"])
        write_field(file,"Capacidad",f"{disk['size']} GB")


def write_partitions(file, partitions):

    file.write("\nPARTICIONES\n")

    for index, partition in enumerate(partitions, start=1):

        file.write(f"\nPartición {index}\n")

        write_field(file, "Unidad", partition["device"])
        write_field(file, "Sistema de archivos", partition["filesystem"])
        write_field(file, "Capacidad total", partition["total"])
        write_field(file, "Espacio libre", partition["free"])
        write_field(file, "Uso", partition["used_percent"])


    

