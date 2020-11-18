import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def connection(db):
    "connect to database and return connection and cursor"
    if not db:
        db = "sparkifydb"
    conn = psycopg2.connect(
    database="template1 ", user='mehdi', password='mehdi', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    return cursor,conn

def create_database():
    conn=connection("template1")
    
    # Create sparkifydb 
    cursor.execute(''' DROP DATABASE IF EXISTS sparkifydb''')
    cursor.execute(" CREATE DATABASE sparkifydb ENCODING 'utf8' TEMPLATE template0; ")
    # Close connection
    cursor.close
    conn.close

def create_tables(cursor, conn):
    for query in create_table_queries:
        cursor.execute(query)
        conn.commit()

def drop_tables(cursor, conn):
    for query in drop_table_queries:
        cursor.execute(query)
        conn.commit()

if __name__ == "__main__":
    cursor, conn = create_database()
    drop_tables(cursor, conn)
    create_tables(cursor, conn)

    cursor.close()
    conn.close()
    