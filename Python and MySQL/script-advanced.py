# Importing required packages
import pymysql
import csv

# Creating database connection to MySQL

# Credentials
HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
DATABASE_NAME = 'hrdata'

try:
    conn = pymysql.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = DATABASE_NAME
    )

    print(f'Successfully connected to database- {DATABASE_NAME} on host- {HOST}')

    cursor = conn.cursor()

except Exception as e:
    print(e)

def create_tables():
    """
        Desc : Creating random tables for the database using DDL (Data Definition Languages) majorly - CREATE, DROP
    """
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS employees (emp_id VARCHAR(255) PRIMARY KEY NOT NULL, firstname VARCHAR(255) NOT NULL, lastname VARCHAR(255) NOT NULL, sex TEXT, region VARCHAR(255), dept_id INT NOT NULL, salary BIGINT NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS departments (emp_id_dep VARCHAR(255) NOT NULL, dep_name VARCHAR(255) NOT NULL, start_date TIMESTAMP, FOREIGN KEY (emp_id_dep) REFERENCES hrdata.employees(emp_id))")

        print("Successfully Created Tables - employees and departments.")
    
    except Exception as e:
        print(f"An Error occurred :- {e}")

# create_tables()

def insert_from_csv():
    """
        Desc : Populating the tables with data from .csv files.
    """
    try:
        employees_data = csv.reader(open('./data/employees.csv'))
        departments_data = csv.reader(open('./data/departments.csv'))
        next(employees_data)
        next(departments_data)
        for row in employees_data:
            cursor.execute('INSERT INTO employees (emp_id, firstname, lastname, sex, region, dept_id, salary) VALUES(%s, %s, %s, %s, %s, %s, %s)',row)

        for row in departments_data:
            cursor.execute('INSERT INTO departments (emp_id_dep, dep_name, start_date) VALUES(%s, %s, %s)', row)

        conn.commit()
        print("Successfully populated !")
    
    except Exception as e:
        print(f"An Error occurred :- {e}")

# insert_from_csv()

def run(query):
    cursor.execute(query)
    rows = cursor.fetchall()
    return [row for row in rows]

# String patterns using LIKE
print(run("SELECT * FROM employees WHERE firstname like 'wa%' ")) # OUTPUT - [('E0004', 'Wale', 'Davies', 'M', 'Abuja', 2, 35000)]
# WHERE clause, AND clause, sorting using ORDER BY clause
print(run("SELECT firstname, lastname, salary FROM employees WHERE salary between 60000 AND 100000 ORDER BY salary LIMIT 2")) # OUTPUT - [('Chris', 'Brown', 76000), ('Olumide', 'Ayeni', 100000)]
# COUNT clause and grouping using GROUP BY clause
print(run("SELECT region, count(region) FROM employees GROUP BY region")) # OUTPUT - [('Abeokuta', 3), ('Abuja', 5), ('Ibadan', 2), ('Lagos', 5)]
# Working with Date and Time objects
print(run("SELECT * FROM departments WHERE YEAR(start_date) = 2020 AND MONTH(start_date) = 10")) # OUTPUT - [('E0006', 'Software development', datetime.datetime(2020, 10, 20, 10, 10, 10))]
# INNER JOIN using aliases E and D for table names
print((run("SELECT E.firstname, E.lastname, D.dep_name FROM employees as E INNER JOIN departments as D WHERE E.emp_id=D.emp_id_dep LIMIT 3"))) # OUTPUT - [('Alice', 'Warner', 'Software development'), ('Muhamaddu', 'Buhari', 'Business and Sales'), ('Ayo', 'Balogun', 'Service operations')]
# OUTER JOIN (LEFT OUTER JOIN) with AVG CLAUSE
print(run("SELECT D.dep_name, AVG(E.salary) FROM employees as E LEFT OUTER JOIN departments as D ON E.emp_id=D.emp_id_dep GROUP BY D.dep_name LIMIT 2")) # OUTPUT - [('Business and Sales', Decimal('78666.6667')), ('Database management', Decimal('67500.0000'))]