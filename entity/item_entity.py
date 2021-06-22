class ItemEntity:
    def __init__(self):
        self.field_set = {}

    def __repr__(self):
        return str(self.field_set)

    def get_property(self, key):
        return self.field_set[key] if key in self.field_set.keys() else None
