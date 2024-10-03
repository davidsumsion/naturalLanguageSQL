import os

from db import create_table, create_connection
from schema import *


def select_all_from_class(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    # cur.execute("SELECT * FROM class")
    cur.execute("SELECT tablename FROM pg_tables WHERE schemaname = 'public';")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def insert_to_class(conn):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = """
        INSERT INTO class VALUES
        (1, 'CS 452', 'Database Modeling'),
        (2, 'CS 393', 'Leet Code'),
        (3, 'CS 340', 'Software Design'),
        (4, 'CS 224', 'bit and byte stuff'),
        (5, 'CS 204', 'Software Lab');
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_student(conn):
    sql = """
        INSERT INTO student VALUES
        (1, 'Haul Stewart'),
        (2, 'John Doe'),
        (3, 'Jane Smith'),
        (4, 'Emily Davis'),
        (5, 'Michael Johnson'),
        (6, 'Sarah Wilson'),
        (7, 'David Brown'),
        (8, 'Sophia Miller'),
        (9, 'James Garcia'),
        (10, 'Olivia Martinez');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_enrollment(conn):
    sql = """
        INSERT INTO enrollment VALUES
        (1, 2),
        (1, 6),
        (2, 6),
        (2, 7),
        (3, 3),
        (3, 5),
        (4, 10),
        (4, 7),
        (5, 10),
        (5, 1);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_building(conn):
    sql = """
         INSERT INTO building VALUES
        (1, 'No leg room, always warm', 'MARB'),
        (2, 'I am lost', 'JKB'),
        (3, 'How is everyone sick already?', 'TMCB');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_class_student(conn):
    sql = """
         INSERT INTO class_building (class_id, building_id) VALUES
                (1, 1), 
                (1, 2),
                (2, 1), 
                (2, 3), 
                (3, 2), 
                (4, 3), 
                (5, 1), 
                (5, 3); 
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def drop_table(conn):
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS albums, students, student, players, sodas, jobs, studentnew, enrolled_in, course, employee, public.class CASCADE;")

def main():
    database = "postgres://tsdbadmin:cyny7stzegherpjm@ofz0110e5v.iohe4w4ipq.tsdb.cloud.timescale.com:34261/tsdb?sslmode=require"
    # create a database connection
    conn = create_connection(database)
    # select_all_from_class(conn)
    # drop_table(conn)

    create_table(conn, sql_create_class_table)
    insert_to_class(conn)
    create_table(conn, sql_create_student_table)
    insert_to_student(conn)
    create_table(conn, sql_create_enrollment_table)
    insert_to_enrollment(conn)
    create_table(conn, sql_create_building_table)
    insert_to_building(conn)
    create_table(conn, sql_create_class_student_table)
    insert_to_class_student(conn)

    print("Database build successful!")

if __name__ == "__main__":
    main()

