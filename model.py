import sqlite3
import logging

logging.basicConfig(level="INFO")

class UserDB(object):

    def __init__(self):
        super(UserDB, self).__init__()

    def _get_connection(self):
        conn = sqlite3.connect("sqlite.db")
        return conn

    def init_db(self):
        conn = self._get_connection()

        try:
            cursor = conn.cursor()

            with open("create_user.sql") as f:
                statement = ""
                for line in f:
                    line = line.strip()
                    logging.info("line : %s" % line)
                    if line.endswith(";"):
                        statement += line
                        logging.info("SQL : %s" % statement)
                        cursor.execute(statement)
                        statement = ""
                    else:
                        statement += line

            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def dump_database(self):
        conn = self._get_connection()

        with open("dump.sql", "w") as f:
            for line in conn.iterdump():
                f.write("%s\n" % line)

        conn.close()

    def get_users(self):
        conn = self._get_connection()

        try:
            cursor = conn.cursor()
            result = cursor.execute("SELECT uid, login, fullname FROM user").fetchall()
        finally:
            conn.close()

        return result

if __name__ == "__main__":
    user_db = UserDB()
    user_db.init_db()
    user_db.dump_database()