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
    cur.execute("SELECT * FROM states WHERE CONVERT(name USING Latin1) \
        COLLATE Latin1_General_CS LIKE 'N%' ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
