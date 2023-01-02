import csv
import  os
from datetime import datetime


def format_date(date_string):
    """
        A function to convert csv date
        to python date format
    """

    full_month_format = "%d %B %Y"

    return datetime.strptime(date_string, full_month_format)


def load_stores_data_set():
    pass

def load_store_info():
    pass

def load_sales_data_set():
    pass

def load_Features_data_set():
    pass