# coding=utf-8
from flask import request
from flask_restful import Resource, abort

from libs import wrap_success, wrap_fail
from services.block import upload_block
from services.strength import upload_strength, get_strengths, get_blocks


class Stock(Resource):
    def get(self, action):
        if action == "getStrengths":
            return _get_strengths()
        elif action == "getBlocks":
            return _get_blocks()
        else:
            abort(404)

    def post(self, action):
        if action == "uploadStrength":
            return _upload_strength()
        elif action == "uploadBlock":
            return _upload_block()
        else:
            abort(404)


def _get_strengths():
    try:
        query_dict = {
            "date": request.args["date"]
        }
        res = get_strengths(query_dict)
        return wrap_success(res)
    except Exception as e:
        return wrap_fail(e)


def _get_blocks():
    try:
        query_dict = {
            "code": request.args["code"],
            "start_date": request.args["start_date"],
            "end_date": request.args["end_date"]
        }
        res = get_blocks(query_dict)
        return wrap_success(res)
    except Exception as e:
        return wrap_fail(e)


def _upload_strength():
    try:
        res = upload_strength(request.files['file'], request.args['type'])
        return wrap_success(res)
    except Exception as e:
        return wrap_fail(e)


def _upload_block():
    try:
        res = upload_block(request.files['file'], request.args['type'])
        return wrap_success(res)
    except Exception as e:
        return wrap_fail(e)
