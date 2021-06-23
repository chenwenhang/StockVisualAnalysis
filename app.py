from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from controllers.stock import Stock
from libs import wrap_success
from settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)
CORS(app, supports_credentials=True, resources=r'/*')

api = Api(app)


@app.route('/', methods=['OPTIONS'])
def option_handle():
    return wrap_success({})


api.add_resource(Stock, '/api/stock/<action>')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)
