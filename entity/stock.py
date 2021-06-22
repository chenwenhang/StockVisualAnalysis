# coding=utf-8
from entity.item_entity import ItemEntity


class StockEntity(ItemEntity):
    def __init__(self, stock):
        ItemEntity.__init__(self)
        self.field_set = stock

    def get_code(self):
        return self.field_set["code"]

    def get_name(self):
        return self.field_set["name"]

    def get_industry(self):
        return self.field_set["industry"]

    def get_price(self):
        # 股价
        return self.field_set["price"]

    def get_market_value(self):
        # 流通市值
        return self.field_set["market_value"]

    def get_rise_and_fall(self):
        # 涨跌
        return self.field_set["rise_and_fall"]

    def get_turnover(self):
        # 换手率
        return self.field_set["turnover"]

    def get_region(self):
        return self.field_set["region"]

    def get_quantity_relative_ratio(self):
        # 量比
        return self.field_set["quantity_relative_ratio"]

    def get_amplitude(self):
        # 振幅
        return self.field_set["amplitude"]

    def set_code(self, code):
        self.field_set["code"] = code

    def set_name(self, name):
        self.field_set["name"] = name

    def set_industry(self, industry):
        self.field_set["industry"] = industry

    def set_price(self, price):
        self.field_set["price"] = price

    def set_market_value(self, market_value):
        self.field_set["market_value"] = market_value

    def set_rise_and_fall(self, rise_and_fall):
        self.field_set["rise_and_fall"] = rise_and_fall

    def set_turnover(self, turnover):
        self.field_set["turnover"] = turnover

    def set_region(self, region):
        self.field_set["region"] = region

    def set_quantity_relative_ratio(self, quantity_relative_ratio):
        self.field_set["quantity_relative_ratio"] = quantity_relative_ratio

    def set_amplitude(self, amplitude):
        self.field_set["amplitude"] = amplitude
