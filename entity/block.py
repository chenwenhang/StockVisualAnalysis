from entity.item_entity import ItemEntity


class BlockEntity(ItemEntity):
    def __init__(self, block):
        ItemEntity.__init__(self)
        self.field_set = block

    def get_code(self):
        return self.field_set["code"]

    def get_name(self):
        return self.field_set["name"]

    def get_indicator(self):
        return self.field_set["indicator"]

    def get_RPS250(self):
        return self.field_set["RPS250"]

    def get_RPS120(self):
        return self.field_set["RPS120"]

    def get_RPS60(self):
        return self.field_set["RPS60"]

    def get_RPS30(self):
        return self.field_set["RPS30"]

    def get_RPS10(self):
        return self.field_set["RPS10"]

    def get_date(self):
        return self.field_set["date"]

    def get_grade(self):
        return self.field_set["grade"]

    def set_code(self, code):
        self.field_set["code"] = code

    def set_name(self, name):
        self.field_set["name"] = name

    def set_indicator(self, indicator):
        self.field_set["indicator"] = indicator

    def set_RPS250(self, RPS250):
        self.field_set["RPS250"] = RPS250

    def set_RPS120(self, RPS120):
        self.field_set["RPS120"] = RPS120

    def set_RPS60(self, RPS60):
        self.field_set["RPS60"] = RPS60

    def set_RPS30(self, RPS30):
        self.field_set["RPS30"] = RPS30

    def set_RPS10(self, RPS10):
        self.field_set["RPS10"] = RPS10

    def set_date(self, date):
        self.field_set["date"] = date

    def set_grade(self, grade):
        self.field_set["grade"] = self.field_set["RPS10"] * 0.4 + \
                                  self.field_set["RPS30"] * 0.3 + \
                                  self.field_set["RPS60"] * 0.2 + \
                                  self.field_set["RPS120"] * 0.1
