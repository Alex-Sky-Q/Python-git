import func


def db_create():
    conn = func.db_conn()
    query = '''CREATE TABLE IF NOT EXISTS tags_count
                  (site TEXT, url TEXT UNIQUE, checkdate TEXT, tags BLOB)'''
    with conn:
        conn.execute(query)
    conn.close()


db_create()
