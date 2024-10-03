import argparse
import openai
import json

from schema import *
from openai import OpenAI

from query import select_from_table
from db import create_connection

DATABASE = "postgres://tsdbadmin:cyny7stzegherpjm@ofz0110e5v.iohe4w4ipq.tsdb.cloud.timescale.com:34261/tsdb?sslmode=require"

def ask_openai(client, question):
    with open("multiShot.json", "r") as f:
        multiShot = json.load(f)

    query = ("ONLY RETURN SQL CODE: Give me SQL code to return an answer to: " + question + " This is based on the following PostgreSQL schema.")
    schema = ("Schema:" + sql_create_student_table + "\n\n" + sql_create_enrollment_table + "\n\n" +
             sql_create_class_table + "\n\n" + sql_create_building_table + "\n\n" +
              sql_create_class_student_table)

    # print(query)

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": query},
            {"role": "user", "content": schema},
            {"role": "user", "content": "Here are some example queries in a json format:"},
            {"role": "user", "content": str(multiShot)}
        ],
        stream=True
    )
    result = ''
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            result +=chunk.choices[0].delta.content

    return result[6:-3]


def main(conn):
    with open("auth.json", "r") as f:
        auth = json.load(f)
    # Load your API key from an environment variable or secret management service
    # openai.api_key = os.getenv(auth['api_key'])
    openai.api_key = auth['openaiKey']

    # TODO: setup prompt, API call, and result
    client = openai.OpenAI(
        api_key = auth['openaiKey']
    )

    while True:
        query = input("\nEnter your Question: ")


        result = ask_openai(client, query)

        print('sql query:', result)

        select_from_table(conn, result)





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, default="natural language query")
    args = parser.parse_args()
    conn = create_connection(DATABASE)

    main(conn)