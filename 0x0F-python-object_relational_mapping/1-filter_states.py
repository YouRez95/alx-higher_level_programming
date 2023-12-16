#!/usr/bin/python3
"""select states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         password=sys.argv[2], database=sys.argv[3])
    sql = db.cursor()
    sql.execute(
        """SELECT * FROM states WHERE states.name
        LIKE BINARY 'N%' ORDER BY states.id"""
    )

    result = sql.fetchall()

    for r in result:
        print(r)
    sql.close()
