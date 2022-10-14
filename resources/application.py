from flask import Flask, Response, request
from datetime import datetime
import json
from tables import Tables
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/tables/',
            template_folder='web/templates')

CORS(app)


@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "Tables",
        "health": "Good",
        "at time": t
    }

    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


#####################################################################################################################
#                                                 add tables                                                        #
#####################################################################################################################
@app.route("/api/tables/add/indoor/<cap>", methods=["PUT"])
def add_indoor_table(cap):
    result = Tables.add_table(cap, True)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/tables/add/outdoor/<cap>", methods=["PUT"])
def add_outdoor_table(cap):
    result = Tables.add_table(cap, False)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


#####################################################################################################################
#                                                 get tables                                                        #
#####################################################################################################################
@app.route("/api/tables/get/seats/<num>", methods=["GET"])
def get_by_number(num):
    result = Tables.get_by_number(num)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/tables/get/indoor", methods=["GET"])
def get_indoor():
    result = Tables.get_indoor(True)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/tables/get/outdoor", methods=["GET"])
def get_outdoor():
    result = Tables.get_indoor(False)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


#####################################################################################################################
#                                                delete tables                                                      #
#####################################################################################################################
@app.route("/api/tables/delete/outdoor/<cap>", methods=["PUT"])
def delete_outdoor_table(cap):
    result = Tables.delete_last_table(cap, False)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/tables/delete/indoor/<cap>", methods=["PUT"])
def delete_indoor_table(cap):
    result = Tables.delete_last_table(cap, True)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

