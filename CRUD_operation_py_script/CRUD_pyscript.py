import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

con= mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )
cursor = con.cursor()

def create_employee_table():
    """
    Description: Creates the 'employee' table and inserts sample data. 
    Parameters: None    
    Returns: None
    """
    cursor.execute("create table employee(name varchar(20), id int,city varchar(10))")
    cursor.execute("insert into employee values('Ram',1,'pune'),('madhura',2,'thane'),('chandan',3,'kharghar'),('lakhan',4,'mumbai')")

def show_student_table():
    """
    Description: Fetches and prints all records from the employee table
    Parameters: None    
    Returns: None
    """
    cursor.execute("select * from students")
    records = cursor.fetchall()
    for i in records:
        print(i)
   
def update_table():
    """
    Description: Updates the employee table by adding a salary column    and updating values
    Parameters: None    
    Returns: None
    """
    cursor.execute("alter table employee add column salary int")
    cursor.execute("update employee set salary=30000 where id=1")
    cursor.execute("update employee set salary=34000 where id=2")
    cursor.execute("update employee set salary=33000 where id=3")
    cursor.execute("update employee set salary=32000 where id=4")

def drop_table():
    """
    Description: Drops the employee table from the database    Parameters: None    
    Returns: None
    """
    cursor.execute("drop table employee")   

def main():
    """
    Description: Main function to execute database operations.  Parameters: None    
    Returns: None
    """
    create_employee_table()
    show_student_table()
    show_employee_table()
    update_table()
    drop_table() 


if __name__=="__main__":
    main()

cursor.close()
con.close()
