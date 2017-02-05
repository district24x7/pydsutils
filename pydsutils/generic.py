"""Generic utility functions
"""
import logging


def retry(n_try, sleep=1, *exception_types):
    """Retry a function several times

    Args:
        n_try: Number of trials
        sleep: Delay in seconds. Default=1
        exception_types: Types of exeptions
    """

    def try_fn(func, *args, **kwargs):
        for n in range(n_try):
            try:
                return func(*args, **kwargs)
            except exception_types or Exception as e:
                print("Trial {n} failed with exception: {e} .\nTrying again after a {sleep} second sleep".format(n=n,\
                        e=str(e), sleep=sleep))
                time.sleep(sleep)
    return try_fn


def create_logger(name,
                  level="info",
                  fmt="%(asctime)s %(levelname)s %(name)s: %(message)s",
                  datefmt="%Y-%m-%d %H:%M:%S",
                  add_console_handler=True,
                  add_file_handler=False,
                  logfile="/tmp/tmp.log"):
    """Create a formatted logger

    Args:
        fmt: Format of the log message
        datefmt: Datetime format of the log message
    Examples:
        logger = create_logger(__name__, level="info")
        logger.info("Hello world")
    """
    level = {
        "debug": logging.DEBUG, "info": logging.INFO,
        "warn": logging.WARN,   "error": logging.ERROR
        }[level]

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logFmt = logging.Formatter(fmt=fmt, datefmt=datefmt)

    if add_console_handler:  # Print on console
        ch = logging.StreamHandler()
        ch.setFormatter(logFmt)
        logger.addHandler(ch)

    if add_file_handler:  # Print in a log file
        th = logging.RotatingFileHandler(logfile, backupCount=5)
        th.doRollover()
        th.setFormatter(logFmt)
        logger.addHandler(th)

    return logger
