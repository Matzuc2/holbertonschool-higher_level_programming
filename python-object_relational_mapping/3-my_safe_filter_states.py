#!/usr/bin/python3
""" Script that lists all states with a name starting with """
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = %s \
            ORDER BY states.id"
    cur.execute(sql, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
