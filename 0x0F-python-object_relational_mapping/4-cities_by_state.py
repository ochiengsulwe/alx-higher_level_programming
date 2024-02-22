#!/usr/bin/python3
"""Implements the `INNER JOIN` function in SQL."""

import MySQLdb
import sys


def inner_join(uname, passwd, dbname):
    """Joins two related tables on their association.

        Args:
            uname (str): The username.
            passwd (str): The user password.
            dbname (str): The database we are querying.

        Returns:
            list: A list of the name occurances as they exists.
    """
    try:
        db = MySQLdb.connect(host='localhost',
                             user=uname,
                             passwd=passwd,
                             db=dbname)

        cur = db.cursor()

        cur.execute("""
            SELECT `cities.id`, `cities.name`, `states.name`
            FROM `cities`
            INNER JOIN `states` ON `cities.state_id` = `states.id`
            ORDER BY `cities.id` ASC
            """)

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
    if len(sys.argv) != 4:
        sys.exit(1)

    uname = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    inner_join(uname, passwd, dbname)
