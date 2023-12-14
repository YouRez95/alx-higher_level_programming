#!/usr/bin/python3
"""select states by name passed as argument and safe from MySQL injection"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         password=sys.argv[2], database=sys.argv[3])
    sql = db.cursor()
    query = """SELECT * FROM states WHERE states.name=%s
            ORDER BY states.id"""
    sql.execute(query, (sys.argv[4],))

    result = sql.fetchall()

    for r in result:
        print(r)
    sql.close()
