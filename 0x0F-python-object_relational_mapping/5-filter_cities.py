#!/usr/bin/python3
"""this is the file"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=args[1], password="password", db=args[3])

    cursor = db_connection.cursor()
    a = f"SELECT states.id FROM states WHERE states.name = '{args[4]}'"
    cursor.execute(f"SELECT name FROM cities WHERE cities.state_id = ({a});")

    m = cursor.fetchall()

    for i in m:
        print(f"{i[0]}", end="\n" if m[-1][0] == i[0] else ", ")
    
    db_connection.close()
