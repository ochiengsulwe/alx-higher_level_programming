#!/usr/bin/python3
"""The script lists all states with a name starting with N.
    
    The script only allow returns with capital N. Lower case n is ignored.
"""


import MySQLdb
import sys


def begin_N(uname, passwd, dbName):
    """Queries the parsed db to find states with names starting in N.

        Args:
            uname (str): The user to be accessing the database.
            passwd (str): The user password to allow access to the db.
            dbName (str): The database we shall be querying.

        Returns:
            list: A list of all selected states in an ascending order.
    """
    try:
        db = MySQLdb.connect(host: 'localhost'
                             port: 3306,
                             user: uname,
                             passwd: passwd,
                             db: dbName)

        cur = db.cursor()

        cur.execute("""
               SELECT *
               FROM `states`
               WHERE `name` LIKE 'N%'
               ORDER BY `id` ASC
               """)

        states = cur.fetch()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Failed to connect to the database")
        sys.exit(1)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    uname, passwd, dbName = sys.argv[1], sys.argv[2], sys.argv[3]
    begin_N(uname, passwd, dbName)
