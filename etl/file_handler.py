# coding=utf-8
import pandas as pd


def upload_file(file_obj, type_name, fields_list=None):
    if type_name == "excel":
        return upload_file_excel(file_obj, fields_list)


def upload_file_excel(file_obj, fields_list=None):
    df = pd.read_excel(file_obj, engine='openpyxl')
    df.fillna("", inplace=True)
    df_list = []
    for i in df.index.values:
        df_line = df.loc[i, fields_list].to_dict() if fields_list else df.loc[i].to_dict()
        df_list.append(df_line)
    return df_list
