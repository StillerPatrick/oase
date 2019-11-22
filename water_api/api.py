import flask
from flask import request, jsonify
import sqlite3
from database import Waterholes_DB



app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/waterholes/all', methods=['GET'])
def get_all():
    wh_db = Waterholes_DB("waterholes.db")
    response = wh_db.get_all_waterholes()
    json_style_response = wh_db.response_to_json(response)
    return jsonify(json_style_response)

@app.route('/api/v1/waterholes/all', methods=['GET'])
def get_all():
    wh_db = Waterholes_DB("waterholes.db")
    response = wh_db.get_all_waterholes()
    json_style_response = wh_db.response_to_json(response)
    return jsonify(json_style_response)


@app.route('/api/v1/waterholes', methods=['GET'])
def get_by_id():
    wh_db = Waterholes_DB("waterholes.db")
    
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    response = wh_db.get_all_waterholes()
    if id >= len(response):
        return "Error: No waterhole is available with id: " + str(id)
    else:
        response = [response[id]]
        json_style_response = wh_db.response_to_json(response)
        return jsonify(json_style_response)







if __name__ == "__main__":
    app.run()
