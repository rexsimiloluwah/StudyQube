# Importing required packages
import pymysql

# Creating database connection to MySQL

# Credentials
HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
DATABASE_NAME = 'bookstore'

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

#conn.close() → To close the connection.

def create_table(name):
    """
        Desc - For Creating tables in the database
    """
    try:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), quantity INT, author VARCHAR(255), price INT)")
        print(f"Successfully created table {name}")
    except Exception as e:
        print(e)

# create_table("bookstore")

# Inserting a single record
def insert_single(title, quantity, author, price):
    try:
        query = f"INSERT INTO bookstore (id, title, quantity, author, price) VALUES (%s, %s, %s, %s, %s)"
        # Execute query
        cursor.execute(query, (None, title, quantity, author, price))
        # Commit to save changes to database
        conn.commit()
        print(f"{str(cursor.rowcount)} row inserted")
    except Exception as e:
        print(e)

# insert_single("Ego is the Enemy", 12, "Ryan Holiday", 150)

# Inserting multiple records
def insert_multiple(list_of_values):
    try:
        query = f"INSERT INTO bookstore (id, title, quantity, author, price) VALUES {','.join('(%s, %s, %s, %s, %s)' for _ in list_of_values)}"
        cursor.execute(query, [item for _ in list_of_values for item in _] ) # Flatten the values
        conn.commit()
        print(f"{str(cursor.rowcount)} row inserted")
    except Exception as e:
        print(e)

# insert_multiple([(None,"Rich dad, Poor dad",10, "Robert Kiyosaki", 300), (None, "Art of War", 2, "Sun Tzu", 100)])

# Read or Retrive operations
def read(query):
    # Executing and printing the query results
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
read("SELECT * FROM bookstore")
read("SELECT * FROM bookstore ORDER BY quantity")
read("SELECT * FROM bookstore LIMIT 1")
read("SELECT * FROM bookstore WHERE title LIKE '%habits%' ")


# Update operation
def update(query):
    cursor.execute(query)
    conn.commit()
    print("Updated !")
update(f"UPDATE bookstore SET quantity = {12} WHERE ID = '1' ")

# Delete operation
def delete(row_id):
    cursor.execute(f"DELETE FROM bookstore WHERE ID = {row_id}")
    conn.commit()
    print("Deleted !")
delete(9) # Deleted row 9

conn.close()