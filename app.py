from flask import Flask, make_response
from flask_restful import reqparse, abort, Api, Resource

from controllers.stock import Stock
from settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)

api = Api(app)

api.add_resource(Stock, '/stock/<action>')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)
