from models.db import MysqlHelper
from settings import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE


class StockModel(MysqlHelper):
    __tablename__ = "stock"

    def __init__(self):
        MysqlHelper.__init__(self, DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)


