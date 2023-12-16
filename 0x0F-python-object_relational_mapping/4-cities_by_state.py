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
    query = "SELECT * FROM cities ORDER BY cities.id"
    sql.execute(query)
    result = sql.fetchall()

    for r in result:
        print(r)
