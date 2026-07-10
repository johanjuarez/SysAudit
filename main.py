from collector.collector import collect_inventory

from reports.txt.report import generate_txt_report


def main():

    inventory = collect_inventory()

    report = generate_txt_report(inventory)

    print(f"Reporte generado correctamente:\n{report}")


if __name__ == "__main__":

    main()