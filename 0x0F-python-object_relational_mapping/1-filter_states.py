#!/usr/bin/python3
"""this is the file"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv
    s = "WHERE name LIKE 'N%' ORDER BY id"

    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=args[1], password=args[2], db=args[3])

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states {:s}".format(s))

    m = cursor.fetchall()

    for i in m:
        print(i)

    db_connection.close()
