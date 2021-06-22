# coding=utf-8
from entity.item_entity import ItemEntity


class StrengthEntity(ItemEntity):
    def __init__(self, stock):
        ItemEntity.__init__(self)
        self.field_set = stock

    def get_industry(self):
        return self.field_set["industry"]

    def get_count(self):
        # 行业
        return self.field_set["count"]

    def get_grade(self):
        # 分数
        return self.field_set["grade"]

    def get_date(self):
        return self.field_set["date"]

    def set_industry(self, industry):
        self.field_set["industry"] = industry

    def set_count(self, count):
        self.field_set["count"] = count

    def set_grade(self, grade):
        self.field_set["grade"] = grade

    def set_date(self, date):
        self.field_set["date"] = date
