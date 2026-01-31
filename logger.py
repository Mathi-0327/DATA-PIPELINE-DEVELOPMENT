import logging

def setup_logger(log_file="pipeline.log", level=logging.INFO):
    logger = logging.getLogger("DataPipelineLogger")
    logger.setLevel(level)

    # Avoid duplicate logs
    if not logger.handlers:

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
