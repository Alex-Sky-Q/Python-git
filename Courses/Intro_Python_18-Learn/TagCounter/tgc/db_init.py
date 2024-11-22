# In case new DB is needed - run this file to create a table in the DB
from tgc import func


def db_init():
    conn = func.db_conn()
    query = '''CREATE TABLE IF NOT EXISTS tags_count
                  (site TEXT, url TEXT UNIQUE, checkdate TEXT, tags BLOB)'''
    with conn:
        conn.execute(query)
    conn.close()


db_init()
