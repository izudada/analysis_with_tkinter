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

    full_month_format = "%d/%m/%Y"

    return datetime.strptime(date_string, full_month_format)


def load_stores_data_set():
    """
        A function to load stores data set 
        into a mysql database

        CLEANING:
                the "size" column has empty cells in the csv file.
                this automatically translates to a null value.

                Size column has to be an int type before database insertion.
                Thus a condition was used to determine when to add size column
                to the columns of insertion and when not to. 
                This is to accommodate the null or empty cells.
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
    """
        A function that loads sales
        data set into mysql database

        CLEANING:
                    Date field had to be formatted to python date object before inserting
                    into the table.

                    MYSQL doesnt accommodate booleans but tinyint field types.
                    "is_holiday" column had to be converted from boolean to tinyint
                    before inserting into the table
    """

    path = 'datasets/sales_data-set.csv'

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
                    #   formate date
                    sales_date = format_date(row[2])
                    #   convert is_holiday value from boolean string to tinyint for mysql field
                    is_holiday = 0
                    if row[4] != 'FALSE':
                        is_holiday = 1
                    
                    #   insert record into db
                    cursor.execute("INSERT into sales(store, department, date, weekly_sales, is_holiday) VALUES(%s, %s, %s, %s, %s)", (row[0], int(row[1]), sales_date, float(row[3]), is_holiday))
                    con.commit()
                    cursor.close() 
        print("sales data set loaded successfully")
    except Exception as e:
        print("There was an issue loading the sales data set")
        print(e)

def load_features_data_set():
    """
        A function that loads the feature
        data set into mysql db.

        CLEANING: columns that needed cleaning were MarkDown 1 - 5, CPI and unemployment columns
                    Reason for cleaning is because most of their values/cells are NA (not available).
                    To modell a consistent, complete and valid data, the default values in the mysql 
                    database for these fields are NA. 

                    To accommodate the char "NA" and the valid data of floating numbers, a VARCHAR
                    field type was used for the aforementioned fileds.

                    MYSQL doesnt accommodate booleans but tinyint field types.
                    "is_holiday" column had to be converted from boolean to tinyint
                    before inserting into the table
    """
    path = 'datasets/Features_data_set.csv'

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
                    #   formate date
                    feature_date = format_date(row[1])

                    #   convert is_holiday boolean value to tinyint for mysql table
                    is_holiday = 0
                    if row[11] != 'FALSE':
                        is_holiday = 1
                    
                    #   insert record into db
                    cursor.execute("INSERT into feature(store, date, temperature, fuel_price, mar_down_1, mar_down_2, mar_down_3, mar_down_4, mar_down_5, cpi, unemployment, is_holiday) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (row[0], feature_date, float(row[2]), float(row[3]), row[4], row[5], row[6], row[7], row[8], row[9], row[10], is_holiday))
                    con.commit()
                    cursor.close() 
        print("features data set loaded successfully")
    except Exception as e:
        print("There was an issue loading the features data set")
        print(e)

def load_store_info():
    path = 'datasets/store_info.csv'

# load_stores_data_set()

# load_sales_data_set()

load_features_data_set()