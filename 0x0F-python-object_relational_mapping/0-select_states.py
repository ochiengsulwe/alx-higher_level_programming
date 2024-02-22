#!/usr/bin/python3
"""The script lists all `states` from the database `hbtn_0e_0_usa`."""


import MySQLdb
import sys


def all_states(mysql_uname, mysql_passwd, db_name):
    """`all_states` fetches from the database parsed all states entries.

        Args:
            mysql_uname (str): The name of the user to access the database.
            mysql_passwd (any) : The password the user will enter before
                                 access is granted.
            db_name (str): The database will be doing our queries.

        Returns:
            list: Returns a list of key:value items in an ascending order.
    """
    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=mysql_uname,
                             passwd=mysql_passwd,
                             db=db_name)

        cur = db.cursor()

        cur.execute("""
                SELECT *
                FROM `states`
                ORDER BY `id` ASC
                """)

        states = cur.fetchall()

        for state in states:
            print(state)
    except MySQLdb.Errpr as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 0-select_states.py <mysql_uname> <mysql_passwd> "
              "<db_name>")
        sys.exit(1)

    mysql_uname, mysql_passwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    all_states(mysql_uname, mysql_passwd, db_name)
