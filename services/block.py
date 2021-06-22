# coding=utf-8
from etl.file_handler import upload_file
from models.block import BlockModel


def upload_block(file_obj, type_name):
    table = upload_file(file_obj, type_name, ["code", "name", "RPS250", "RPS120", "RPS60", "RPS30", "RPS10"])

    blocks = ((row["code"], row["name"], row["RPS250"], row["RPS120"], row["RPS60"], row["RPS30"], row["RPS10"],
               row["RPS10"] * 0.4 + row["RPS30"] * 0.3 + row["RPS60"] * 0.2 + row["RPS120"] * 0.1) for row in table)
    model = BlockModel()
    try:
        count = model.insert_blocks(blocks)
    except Exception as e:
        raise e
    return count
