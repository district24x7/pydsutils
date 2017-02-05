from pdb import set_trace as debug
import os
import sys
from .generic import create_logger
logger = create_logger(__name__, level="info")


def ensure_dir_exists(dir_name):
    """Makes sure the folder exists on disk, similar to "$ mkdir -p"
    Args:
        dir_name: Path string to the folder we want to create.
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return


def set_pythonpath(path, level=0, verbose=1):
    """
    Args:
        path: File path
        level: How many levels to go up. default = 0 means the current directory
        verbose: Verbosity levels
    :return:
    """
    dir = os.path.dirname(os.path.realpath(path))
    while level >=1:
        dir = os.path.dirname(dir)
        level -= 1

    if dir in sys.path:
        if verbose >= 1: logger.info("%s is already on pythonpath. No need to do anything" %dir)
    else:
        sys.path.insert(0, dir)
        if verbose >= 1: logger.info("Successfully added %s to pythonpath" %dir)
    return dir
