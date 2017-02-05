"""Date time utility
"""
from pdb import set_trace as debug
import datetime


def to_datetime(input_date, format=""):
    if isinstance(input_date, str):
        return datetime.datetime.strptime(input_date, format)

    if isinstance(input_date, datetime.datetime):
        return input_date
    raise TypeError
    return


def day_diff(start_date, end_date, add_one=False, format="%Y-%m-%d"):
    """
    Args:
        add_one: whether to add back one day
    """
    new_start = to_datetime(start_date, format)
    new_end = to_datetime(end_date, format)
    diff = (new_end - new_start).days
    if add_one:
        diff += 1
    return diff


def _back_to_original(date, input_date, format):
    """Convert back to origin type
    """
    if isinstance(input_date, str):
        return date.strftime(format)
    elif isinstance(input_date, datetime.datetime):
        return date


def start_of_week(date, format="%Y-%m-%d"):
    """Find start of the week (monday)
    
    Args:
        date: datetime or string format
        format: date format
    Returns
        Start of the week in the same format as input date
    """
    newdate = to_datetime(date, format=format)
    newdate = newdate - datetime.timedelta(newdate.weekday())  # Get to start of the week
    return _back_to_original(newdate, date, format=format)


def start_of_month(date, format="%Y-%m-%d"):
    """Get start of the month in the same format as the input date

    """
    newdate = to_datetime(date, format=format)
    newdate = newdate.replace(day=1)  # Get to start of month
    return _back_to_original(newdate, date, format=format)


def end_of_month(date, format="%Y-%m-%d"):
    """Find emd of the month

    """
    newdate = to_datetime(date, format=format)
    next_month = newdate.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    newdate = next_month - datetime.timedelta(days=next_month.day)
    return _back_to_original(newdate, date, format=format)
