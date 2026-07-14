from collector.collector import collect_inventory
from app.logger import setup_logger
from reports.txt.report import generate_txt_report


def main():

    logger = setup_logger()
    logger.info("Starting SysAudit")

    inventory = collect_inventory()

    logger.info("Inventory collection completed")

    generate_txt_report(inventory)

    logger.info("Report generated successfully")


if __name__ == "__main__":

    main()