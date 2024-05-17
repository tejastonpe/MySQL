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

def self_join():
    cursor.execute("SELECT E1.EMAIL, E2.PHONE_NUMBER FROM EMPLOYEES E1 JOIN EMPLOYEES E2 ON E1.EMPLOYEE_ID = E2.EMPLOYEE_ID;")
    result=cursor.fetchall()
    for i in result:
        print(i)
    
def inner_join():
    cursor.execute("select department_name, count(*) as TotalEmployee from  employees e inner join departments d on e.department_id=d.department_id group by d.department_id, d.department_name order by department_name;")
    result=cursor.fetchall()
    for i in result:
        print(i)

def left_join():
    cursor.execute("select e1.first_name,e1.last_name ,e1.hire_date from employees e1 left join employees e2 on e1.hire_date > e2.hire_date where  e2.last_name='jones';")
    result=cursor.fetchall()
    for i in result:
        print(i)

def right_join():
    cursor.execute("select e1.employee_id, e1.last_name, e1.manager_id,e1.last_name from employees e1 right join employees e2 on e1.manager_id=e2.manager_id;")
    result=cursor.fetchall()
    for i in result:
        print(i)

def cross_join():
    cursor.execute("SELECT EMPLOYEES.FIRST_NAME, DEPARTMENTS.DEPARTMENT_NAME FROM EMPLOYEES CROSS JOIN DEPARTMENTS;")
    result=cursor.fetchall()
    for i in result:
        print(i)
    
def outer_join():
    cursor.execute("select department_name, count(*) as TotalEmployee from  employees e inner join departments d on e.department_id=d.department_id group by d.department_id, d.department_name order by department_name;")
    result=cursor.fetchall()
    for i in result:
        print(i)

def main():
    try:
        db=int(input("\n1-Show tables 2-show table details  3-left join  4-right join  5-self join  6-cross join  7-outer join \n"))
        match db:
            case 1:
                cursor.execute("show tables")
                table=cursor.fetchall()
                for i in table:
                    print(i[0]) 
                main()                                   
            case 2:
                table_name=input("Enter table name: ")
                cursor.execute(f"select * from {table_name}")
                columns = cursor.column_names
                rows = cursor.fetchall()
                print(f"Table: {table_name}")
                print(f"Columns: {', '.join(columns)}")
                for row in rows:
                    print(row)
            case 3:
                left_join()
            case 4:
                right_join()
            case 5:
                self_join()
            case 6:
                cross_join()
            case 7:
                outer_join()
    except Exception as e:
        print(e)        

    cursor.close()
    con.close()

if __name__=="__main__":
    main()