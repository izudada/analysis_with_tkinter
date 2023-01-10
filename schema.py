import sqlite3


conn = sqlite3.connect('walmart.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE store_info
         (  id integer(11) PRIMARY KEY,
            store int(3) NOT NULL,
            manager varchar(50) NULL,
            year_as_manager	int(3) NOT NULL,
            email varchar(100) NULL,
            address varchar(100) NOT NULL,
            city varchar(20) NOT NULL,
            state varchar(5) NOT NULL,
            zip_code int(5) NOT NULL);''')
print("Table store_info created successfully")

conn.execute('''CREATE TABLE  store
         (  id integer(3) PRIMARY KEY,
            store_type varchar(1) NOT NULL,
            size varchar(50) NULL);''')
print("Table store created successfully")


conn.execute('''CREATE TABLE  sales
         (  id integer(20)	 PRIMARY KEY,
            store int(3) NOT NULL,
            department	int(3) NOT NULL,
            date date NOT NULL,
            weekly_sales double NOT NULL,
            is_holiday	tinyint(1) NOT NULL);''')
print("Table sales created successfully")


conn.execute('''CREATE TABLE  feature
         (  id integer(4) PRIMARY KEY,
            store int(3) NOT NULL,
            date date NOT NULL,
            temperature	float NOT NULL,
            fuel_price float NOT NULL,
            mark_down_1	varchar(50) DEFAULT "NA" NOT NULL,
            mark_down_2	varchar(50) DEFAULT "NA" NOT NULL,
            mark_down_3	varchar(50) DEFAULT "NA" NOT NULL,
            mark_down_4	varchar(50) DEFAULT "NA" NOT NULL,
            mark_down_5	varchar(50) DEFAULT "NA" NOT NULL,
            cpi	varchar(50) DEFAULT "NA" NOT NULL,
            unemployment varchar(50) DEFAULT "NA" NOT NULL,
            is_holiday	tinyint(1) NOT NULL);''')
print("Table feature created successfully")

conn.close()
