import logging

logger = logging.getLogger("my_logger")
logging.basicConfig()


logger.error("This is error message")
logger.warning("This is warning messge")
logger.log(logging.CRITICAL, "This is critical messge")