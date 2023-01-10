import csv
from datetime import datetime
import sqlite3


con = sqlite3.connect('walmart.db')

def extract_name_from_email(row):
    """
        A function that extracts a manager's name from his email
        if the cell//name column is empty and email is provided
    """
    name = row.split('@')
    return name[0].split('.')[0] + ' ' + name[0].split('.')[1]

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
                        cursor.execute("INSERT into store(id, store_type) VALUES(?, ?)", (row[0] , row[1]))
                    else:
                        cursor.execute("INSERT into store(id, store_type, size) VALUES(?, ?, ?)", (row[0] , row[1], int(row[2])))
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
                    cursor.execute("INSERT into sales(store, department, date, weekly_sales, is_holiday) VALUES(?, ?, ?, ?, ?)", (row[0], int(row[1]), sales_date, float(row[3]), is_holiday))
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
                    cursor.execute("INSERT into feature(store, date, temperature, fuel_price, mark_down_1, mark_down_2, mark_down_3, mark_down_4, mark_down_5, cpi, unemployment, is_holiday) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row[0], feature_date, float(row[2]), float(row[3]), row[4], row[5], row[6], row[7], row[8], row[9], row[10], is_holiday))
                    con.commit()
                    cursor.close() 
        print("features data set loaded successfully")
    except Exception as e:
        print("There was an issue loading the features data set")
        print(e)

def load_store_info():
    """
        A function that loads the store info csv data
        into a mysql database

        CLEANING:
                Noticing that some shops had repeated address, there was need to make the address
                of each shop unique, and also maintain same shop_id.

                python dictionary "all_adress" was used to store the addresses after being inserted to know when 
                a shop address already exists and also get the last or max store id, for consistency and uniqness
                of store id.

                multiple queries was needed when manager cell or email values are missing.
    """
    path = 'datasets/store_info.csv'
    all_adress = {}
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
                    #   conditions if name and email are given or not
                    if row[1] == '' and row[3] == '':
                        name = 'NULL'
                        email = 'NULL'
                    else:
                        name = extract_name_from_email(row[3])
                        email = row[3]

                    address = row[4].split(';')
                    if str(row[4]) in all_adress:
                        cursor.execute("INSERT into store_info(store, manager, year_as_manager, email, address, city, state, zip_code) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (all_adress[str(row[4])] , name, row[2], email, address[0], address[1], address[2], address[3]))
                    else:   
                        #   condition to clean duplicate store
                        store_id = 1
                        #   get last or highest store id and add 1 to increment the id of the next unique store address
                        if len(all_adress) > 0:
                            store_id = int(max(all_adress.values())) + 1

                        cursor.execute("INSERT into store_info(store, manager, year_as_manager, email, address, city, state, zip_code) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (store_id , name, row[2], email, address[0], address[1], address[2], address[3]))

                    con.commit()
                    cursor.close() 
                    all_adress[str(row[4])] = store_id
        print("store info loaded successfully")
    except Exception as e:
        print("There was an issue loading the store info")
        print(e)

load_stores_data_set()

load_sales_data_set()

load_features_data_set()

load_store_info()