#!/usr/bin/python3
"""
  list all cities from database
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         password=sys.argv[2], database=sys.argv[3])
    sql = db.cursor()
    query = """SELECT c.id, c.name, s.name
            FROM cities c
            JOIN states s ON c.state_id = s.id
            ORDER BY c.id"""
    sql.execute(query)
    result = sql.fetchall()
    # print(type(result))
    # print(result)
    for r in result:
        print(r)
