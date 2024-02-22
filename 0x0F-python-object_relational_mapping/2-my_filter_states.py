#!/usr/bin/python3
"""Takes the name to search as the last argument.

    Displays all values where name matches argument
    """

import MySQLdb
import sys


def arg_search(uname, passwd, dbname, nsearch):
    """Searches for a name as parsed from the database.

        Args:
            uname (str): The username.
            passwd (str): The user password.
            dbname (str): The database we are querying.
            nsearch (str): The state we are to search from the database.

        Returns:
            list: A list of the name occurances as they exists.
    """
    try:
        db = MySQLdb.connect(host='localhost',
                             user=uname,
                             passwd=passwd,
                             db=dbname)

        cur = db.cursor()

        query = "SELECT * FROM `states` WHERE `name` LIKE %s ORDER BY `id` ASC"

        cur.execute(query, (nsearch + "%",))

        res = cur.fetchall()

        for i in res:
            print(i)

    except MySQLdb.Error as e:
        sys.exit(1)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    uname, passwd, dbname, nsearch = sys.argv[1], sys.argv[2], sys.argv[3],
    sys.argv[4]
    search(uname, passwd, dbname, nsearch)
