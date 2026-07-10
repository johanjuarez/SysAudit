"""
Funciones comunes para los reportes TXT.
"""

LINE_LENGTH = 70


def write_separator(file):

    file.write("=" * LINE_LENGTH + "\n")


def write_section(file, title):

    file.write("\n")

    write_separator(file)

    file.write(f"{title.upper()}\n")

    write_separator(file)


def write_field(file, key, value):

    value = value if value not in (None, "") else "N/A"

    file.write(f"{key:<25}: {value}\n")