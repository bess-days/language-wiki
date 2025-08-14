import os
from logging.config import dictConfig
import app
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from app.services import Services

def create_app():
    from logging.config import dictConfig
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

    @app.route("/search_lang", methods=["GET"])
    @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
    def get_lang():
        query = request.args.get("lang")
        results = [lang.get_json() for lang in services.search_by_lang(query)]
        return jsonify(results)

    @app.route("/search_family", methods=["GET"])
    @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
    def get_family():
        query = request.args.get("family")
        results = [lang.get_json() for lang in services.search_by_family(query)]
        return jsonify(results)

    @app.route("/search_script", methods=["GET"])
    @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
    def get_script():
        query = request.args.get("script")
        results = [lang.get_json() for lang in  services.search_by_scripts(query)]
        return jsonify(results)

    @app.route("/search_speakers", methods=["GET"])
    @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
    def get_speakers():
        min_val = int(request.args.get('min'))
        max_val = int(request.args.get('max'))
        results = [lang.get_json() for lang in services.search_by_speakers(min_val, max_val)]
        return jsonify(results)

    @app.route("/search_countries", methods=["GET"])
    @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
    def get_counties():
        min_val = int(request.args.get('min1'))
        max_val = int(request.args.get('max1'))
        results = [lang.get_json() for lang in services.search_by_countries(min_val, max_val)]
        return jsonify(results)

    return app


if __name__ == "__main__":
    t = create_app()
    t.run(host='0.0.0.0', port=5000)