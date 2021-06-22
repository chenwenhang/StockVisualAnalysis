import pymysql


class MysqlHelper(object):
    conn = None

    def __init__(self, host, username, password, db, charset='utf8', port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.charset = charset
        self.port = port

    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password,
                                    db=self.db,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, params=()):
        try:
            self.connect()
            self.cursor.execute(sql, params)
            row_headers = [x[0] for x in self.cursor.description]
            rv = self.cursor.fetchone()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers, result)))
            self.close()
        except Exception as e:
            raise e
        return json_data

    def get_all(self, sql, params=()):
        try:
            self.connect()
            self.cursor.execute(sql, params)
            row_headers = [x[0] for x in self.cursor.description]
            rv = self.cursor.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers, result)))
            self.close()
        except Exception as e:
            raise e
        return json_data

    def insert(self, sql, params=()):
        return self.__edit(sql, params)

    def update(self, sql, params=()):
        return self.__edit(sql, params)

    def delete(self, sql, params=()):
        return self.__edit(sql, params)

    def insert_many(self, sql, params=()):
        return self.__edit_many(sql, params)

    def update_many(self, sql, params=()):
        return self.__edit_many(sql, params)

    def delete_many(self, sql, params=()):
        return self.__edit_many(sql, params)

    def __edit(self, sql, params):
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            self.conn.rollback()
            raise e
        return count

    def __edit_many(self, sql, params):
        try:
            self.connect()
            print(sql)
            print(params)
            count = self.cursor.executemany(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            self.conn.rollback()
            raise e
        return count
