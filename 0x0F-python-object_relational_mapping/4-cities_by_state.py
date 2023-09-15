#!/usr/bin/python3
"""this is the file"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv

    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=args[1], password=args[2], db=args[3])

    cursor = db_connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM states INNER JOIN cities ON \
            cities.state_id = states.id ORDER BY cities.id ASC")

    m = cursor.fetchall()

    for i in m:
        print(f"{i}")
    db_connection.close()
