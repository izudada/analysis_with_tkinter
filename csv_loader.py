import csv
import  os
from datetime import datetime
import mysql.connector as mysql


#   database connection
con = mysql.connect(
        host="localhost", 
        user="root", 
        password="",
        database="walmart"
    )

def format_date(date_string):
    """
        A function to convert csv date
        to python date format
    """

    full_month_format = "%d %B %Y"

    return datetime.strptime(date_string, full_month_format)


def load_stores_data_set():
    """
        A function to load stores data set 
        into a mysql database
    """

    #   csv path
    path = 'datasets/stores_data-set.csv'
    try:
        #   Open and read csv file
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                #   create db connection
                cursor = con.cursor()
                #   skip csv headers
                if row[0] == 'Store':
                    continue
                else:
                    #   insert into store table
                    size = 0
                    if row[2] == '':
                        cursor.execute("INSERT into store(id, store_type) VALUES(%s, %s)", (row[0] , row[1]))
                    else:
                        cursor.execute("INSERT into store(id, store_type, size) VALUES(%s, %s, %s)", (row[0] , row[1], int(row[2])))
                    con.commit()
                    cursor.close() 
        print("stores data set loaded successfully")
    except Exception as e:
        print("There was an issue loading the stores data set")
        print(e)


def load_sales_data_set():
    path = 'datasets/sales_data-set.csv'

def load_store_info():
    path = 'datasets/store_info.csv'

def load_features_data_set():
    path = 'datasets/Features_data_set.csv'

load_stores_data_set()