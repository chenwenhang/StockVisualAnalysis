# coding=utf-8
from etl.file_handler import upload_file
from models.block import BlockModel
from models.strength import StrengthModel
import pandas as pd

from settings import INDUSTRY_NUM_MAP


def upload_strength(file_obj, type_name):
    table = upload_file(file_obj, type_name, ["industry"])
    sts_dict = pd.DataFrame(table).industry.value_counts().to_dict()
    strengths = []
    for k, v in sts_dict.items():
        strengths.append((k, v, 100 * v / INDUSTRY_NUM_MAP[k]))
    model = StrengthModel()
    try:
        count = model.insert_strengths(strengths)
    except Exception as e:
        raise e
    return count


def get_strengths(query_dict):
    model = StrengthModel()
    try:
        data = model.get_all_strengths(query_dict)
        for i in range(len(data)):
            data[i].update({"total": INDUSTRY_NUM_MAP[data[i]["industry"]]})
    except Exception as e:
        raise e
    return data


def get_blocks(query_dict):
    model = BlockModel()
    try:
        data = model.get_all_blocks(query_dict)
    except Exception as e:
        raise e
    return data


def get_blocks_in_range(query_dict):
    model = BlockModel()
    try:
        data = model.get_all_blocks_in_range(query_dict)
    except Exception as e:
        raise e
    return data
