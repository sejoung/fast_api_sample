import logging


def create_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    log_formatter = logging.Formatter(
        "%(asctime)s %(module)s %(levelname)s %(message)s"
    )
    handler.setFormatter(log_formatter)
    logger.addHandler(handler)
    return logger
