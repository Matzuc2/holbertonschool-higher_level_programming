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
    sql = "SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s"\
            "ORDER BY cities.id"
    cur.execute(sql, (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
