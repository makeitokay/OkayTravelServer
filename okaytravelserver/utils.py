import datetime as dt

from okaytravelserver.config import DATETIME_FORMAT, DATE_FORMAT


def get_current_datetime():
    return dt.datetime.now()


def get_current_date():
    return dt.datetime.today()


def parse_date_string(date):
    return dt.datetime.strptime(date, DATE_FORMAT)


def parse_datetime_string(datetime):
    return dt.datetime.strptime(datetime, DATETIME_FORMAT)
