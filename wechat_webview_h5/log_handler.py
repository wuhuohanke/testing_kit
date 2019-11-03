import logging
import time


# 初始化logger
def get_logger():
    log = logging.getLogger(__name__)
    log.setLevel(level=logging.INFO)
    handler = logging.FileHandler("./logs/exec_log-" + time.strftime("%Y%m%d_%H%M%S") + ".log")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log


logger = get_logger()
