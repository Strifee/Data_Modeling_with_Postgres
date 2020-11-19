import psycopg2
from psycopg2.extensions import connection, cursor
from sql_queries import create_table_queries, drop_table_queries

def connection(db: str=None) -> (connection, cursor):
    if not db:
        db = "startupdb"
    conn = psycopg2.connect(
    database=db, user='postgres', password='12345', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    return cursor,conn

def create_database():
    cursor, conn=connection("template1")
    
    # Create startupdb 
    cursor.execute(''' DROP DATABASE IF EXISTS startupdb''')
    cursor.execute("CREATE DATABASE startupdb ENCODING 'utf8'TEMPLATE template0")
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
    create_database()
    cursor, conn = connection()
    drop_tables(cursor, conn)
    create_tables(cursor, conn)

    cursor.close()
    conn.close()
    