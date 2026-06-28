import logging


def get_logger(name: str, verbosity_level: int = 0) -> logging.Logger:
    """Creates and configures a centralized logger."""
    logger = logging.getLogger(name)
    
    #  Handle multiple calls
    if logger.hasHandlers():
        logger.handlers.clear()
        
    #  Level defining based on verbosity level:
    if verbosity_level == 0:
        log_level = logging.WARNING
    elif verbosity_level == 1:
        log_level = logging.INFO
    else:
        log_level = logging.DEBUG
        
    logger.setLevel(log_level)
    
    #  Visual formatting
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger