#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         password=sys.argv[2], database=sys.argv[3])
    sql = db.cursor()
    query = """
              SELECT DISTINCT c.name
              FROM cities c
              JOIN states s ON c.state_id = (
              SELECT id FROM states WHERE states.name = %s
              )
          """
    sql.execute(query, (sys.argv[4],))
    result = sql.fetchall()
    for r in result:
        print(r[0], end=", ")
