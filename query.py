import argparse
from db import create_connection


def select_all_from_student(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_from_table(conn, query):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

if __name__ == "__main__":
    database = "postgres://tsdbadmin:cyny7stzegherpjm@ofz0110e5v.iohe4w4ipq.tsdb.cloud.timescale.com:34261/tsdb?sslmode=require"
    conn = create_connection(database)

    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, default="SELECT * FROM student where student_id > 1")
    args = parser.parse_args()
    print(f"Executing query: {args.query}")
    select_from_table(conn, args.query)