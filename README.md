#   Project Todo & Description
Walmart operates a large number of retail stores in the USA. They want to predict sales
in different departments from various factors: the temperature, whether there is a
holiday in a specific week, the unemployment rate, and markdown on the prices. This
small project will focus on database design and some coding in python.
Walmart has run a successful trial of their machine learning for some of their stores in
California. Because only a trial was run the data was collected using CSV files

The following files on the DLE come from the pilot study
- Features_data_set.csv
- sales_data-set.csv
- stores_data-set.csv
- store_info.csv

The data set contains information organized by week. The file Features_data_set.csv
contains information such as Date, temperature, CPI (Consumer Price Index), and
Unemployment (% of the workforce who are unemployed.)

Information about the sales from each department in each store is in the file:
sales_dataset.csv. The file store_info.csv contains information about the store, such
as the name of the manager and the address. The file stores_data-set.csv also contains
information about the stores.

There is more information about the data sets including how the holidays are defined.
Only use the csv data files I have provided.

Design a database to store the data in the csv files. The database design should include
an entity relation diagram, using the crowsfoot notation. You can either use MySQL
workbench or https://app.diagrams.net/, or another graphical package. The database
design should follow the third normal form (3NF). A SQL schema for all the tables
should be produced.

Write a python script to read in the csv files and populate a relational database such as
SQLlite. The data in the csv files may have missing or incorrect values. Discuss how
you cleaned up the data in your code as comments

Write a GUI interface, using for example Tkinter, to update the manager of a specific
store to the database. The code should check that the email is in the correct format:
xxx.yyy@Walmart.org where xxx and yyy are strings of letters.
Demonstrate that the information about the new manager has been correctly added to
the database by including a screenshot.

Develop an additional GUI that has buttons to do the following analysis after the data
has been extracted from the database using SQL.

- Calculate the mean store size for each of the types of stores “A”, “B”, and “C” and print them
out.

- Draw a series of sales versus date for a specific store and department. The GUI should input
the store number and department number and draw the appropriate time series.
Provide screenshots to show the statistical analysis part of the GUI working.


## Set UP
Install and activate a virtual environment before instaling dependencies. Python has virtual envs like 
[virtualen](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3#:~:text=Virtualenv%20is%20a%20tool%20used,the%20globally%20installed%20libraries%20either). There are others like PIPenv and venv. ANy can serve

### Requirements
Once a virtual env is active install dependencies using the command:
```
    pip install -r requirements.txt
```
If you are running a linux OS you will need to install python2-tk manaully to be able to build uisng tkinter. Refer to this [resource](https://www.pythonguis.com/installation/install-tkinter-linux/)

- for Linux the simplest step in installing Tkinter is by running:
```
    sudo apt-get install python3-tk
```
- for indows Tkinter comes pre-installed when installing python software but thos stackoverflow page might help if any isue arises. [Here](https://stackoverflow.com/questions/20044559/how-to-pip-or-easy-install-tkinter-on-windows)

### Schema and Database
The Entity Relationaship Diagram for the MYSQL data base can be found [here](walmart_erd.pdf) 

The sql database has already been exported [here](walmart.sql). But running the csv_loader will populate the database with the record in the csv files within the "datasets" directory.
To populate the database wit the csv files run:
```
    python csv_loader.py
```

Note: some of the csv files are with thousands of records. Depending on the processor speed of your machine this will take hours to conclude. 
Thus it is time efficient to import the sql file into XAMPP or into a MYSQL db.

##  Screenhots or Usage
The required screenshots and usage are compiled [here](Series_sales_versus_date.pdf)

Comments for cleaning data are within respective csv_loader functions