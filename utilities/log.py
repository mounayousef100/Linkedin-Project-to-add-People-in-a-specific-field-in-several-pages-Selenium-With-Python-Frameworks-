import logging


def generate_log():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create a file handler for logging to a file
    file_handler = logging.FileHandler('log.log')
    file_handler.setLevel(logging.INFO)

    # Create a formatter and add it to the file handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger