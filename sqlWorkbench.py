#sql workbench
import sqlite3

#connection to db
conn = sqlite3.connect('demo.db')
#cursor creates location of db
cursor = conn.cursor()
#contents of new db intitialy null
sql = {}
#
sql['DropCustomerTable'] = \
    """
        DROP TABLE IF EXISTS Customers;
    """
sql['createCustomerTable'] = \
    """
    CREATE TABLE Customers (
        Customer_Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Customer_Name TEXT NOT NULL,
        Credit_Rating INTEGER NOT NULL,
        Birthdate DATE NULL
        );
    """

cursor.execute(sql['DropCustomerTable'])
cursor.execute(sql['createCustomerTable'])
conn.commit() 