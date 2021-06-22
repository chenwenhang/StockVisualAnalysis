from models.db import MysqlHelper
from settings import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE


class StrengthModel(MysqlHelper):
    __tablename__ = "strength"
    __fieldlist__ = (
        "id",
        "industry",
        "count",
        "grade",
        "date"
    )

    def __init__(self):
        MysqlHelper.__init__(self, DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)

    def get_all_strengths(self, params):
        # 使用'%%Y-%%m-%%d'当sql有 % s它会进行预编译其它有 % 的字符就会被编译然后 % Y不是任何一种
        sql = """SELECT * FROM strength 
                 WHERE DATE_FORMAT(date,'%%Y-%%m-%%d')=%s"""
        return self.get_all(sql, (params["date"]))

    def insert_strengths(self, data):
        sql = """INSERT INTO strength (industry,count,grade) VALUES (%s,%s,%s)"""
        return self.insert_many(sql, data)
