import logging

def safe_execute(function, default=None):

    try:

        return function()

    except Exception as error:

        logging.error(
            f"{function.__name__}: {error}"
        )

        return default