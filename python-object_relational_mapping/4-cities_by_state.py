#!/usr/bin/python3
""" Script that lists all cities from the database """
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
