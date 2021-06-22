import json
from datetime import datetime, date


def wrap_success(data):
    return {
        "code": "ok",
        "data": convert_to_json(data),
    }


def wrap_fail(msg):
    return {
        "code": "fail",
        "msg": msg
    }


def convert_to_json(data):
    return json.loads(json.dumps(data, cls=ComplexEncoder))


def dict_get_some(dct, *key_list):
    value_list = []
    for k in key_list:
        value_list.append(dct.get(k, None))
    return value_list[0] if len(value_list) == 1 else tuple(value_list)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
