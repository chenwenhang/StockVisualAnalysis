from models.db import MysqlHelper
from settings import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE


class BlockModel(MysqlHelper):
    __tablename__ = "block"
    __fieldlist__ = (
        "id",
        "code",
        "name",
        "indicator",
        "RPS250",
        "RPS120",
        "RPS60",
        "RPS30",
        "RPS10",
        "date",
        "grade"
    )

    def __init__(self):
        MysqlHelper.__init__(self, DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)

    def get_all_blocks(self, params):
        sql = """SELECT * FROM block
                 WHERE code=%s
                 AND DATE_FORMAT(date,'%%Y-%%m-%%d')>=%s
                 AND DATE_FORMAT(date,'%%Y-%%m-%%d')<=%s"""
        return self.get_all(sql, (params["code"], params["start_date"], params["end_date"]))

    def insert_blocks(self, data):
        sql = """INSERT INTO block (code, name, RPS250, RPS120, RPS60, RPS30, RPS10, grade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        return self.insert_many(sql, data)
