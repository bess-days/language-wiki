import os
from logging.config import dictConfig
import app
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from app.services import Services


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})



app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/search_lang": {"origins": "http://localhost:port"}})
services = Services()

@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("app/doc.html", "r") as f:
        return f.read()
@app.route('/web')
def web() -> str:
    app.logger.info("web - Got request")
    with open("web/wiki.html", "r") as f:
        return f.read()

@app.route("/languages", methods=["GET"])
def get_languages():
    return jsonify({'languages': services.load_languages_json()})

@app.route("/search_lang", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def get_lang():
    data = request.get_json()
    app.logger.info(f"/lang - Got Language: {data}")
    s = services.search_by_lang(data.get("lang"))
    return jsonify({'languages': s})
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)