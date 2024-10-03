import sqlite3
from sqlite3 import Error
import psycopg2


"""
    https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
"""

"""def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()"""

def create_connection(conn_string):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = psycopg2.connect(conn_string)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    database = "postgres://tsdbadmin:ojqef3bfm7aa7t1z@xydu17c1xz.iohe4w4ipq.tsdb.cloud.timescale.com:37694/tsdb?sslmode=require"
    create_connection(database)

