"""System level util functions
"""
import sys
import resource


def get_memory_usage():
    """Get memory usage in Mb

    Returns:
        Memory usage in Mb
    """
    rusage_denom = 1024.0
    if sys.platform == 'darwin':  # if Mac
        rusage_denom = rusage_denom * rusage_denom
    
    # in Mb
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem
