"""
    Description :- This script is used to run the complete flask app locally with all the API endpoints.
"""

import json, os, requests, csv, uuid
import pandas as pd
from flask import Flask, request, jsonify, abort, make_response
from werkzeug.utils import secure_filename
from Model import Data, DataSchema, db 
from flask_cors import CORS 
from Model import db
from datetime import datetime
from utils.DateTimeEncoder import DateTimeEncoder
from utils.csvreader import readCSV
from utils.xlsxreader import readXLSX


def create_app(config):
    app = Flask(__name__)

    # Handling CORS (Cross Origin Resource Sharing) easily using thr flask_cors extension
    CORS(app)
    
    app.config.from_object(config)
    
    db.init_app(app)

    return app

app = create_app("config")
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = [".csv", ".xlsx", ".txt"]
app.config["UPLOADS_DIR"] = "uploads"

# Instantiating the Model Schemas

data_schema_multiple = DataSchema(many = True)

data_schema_single = DataSchema()


if not os.path.isdir(app.config["UPLOADS_DIR"]):
    os.mkdir(app.config["UPLOADS_DIR"])

@app.errorhandler(413)
def too_large(e):
    return "Max file size is 10MB, Please compress your image.", 413

@app.route("/", methods = ["POST"])
def upload_from_url():
    """
        This function basically uploads a file from the URL and saves to the database.
    """

    file_url = request.args.get("file_url")
    return file_url.encode("utf-8")

@app.route("/upload", methods = ["POST"])
def upload():
    """
        This function basically parses a .csv or .xlsx or .txt or a file from a url and saves to the database.
    """
        
    # UPLOADED FILE
    uploaded_file = request.files["file"]

    filename = secure_filename(uploaded_file.filename)

    if not uploaded_file:
        return make_response({
            "message" : "Please upload a .csv or .xlsx file or enter the file's URL."
        }, 400
    )

    if filename != "":
        extension = os.path.splitext(filename)[-1].lower()
        if extension not in app.config["UPLOAD_EXTENSIONS"]:
            return make_response({
                "message" : f"Cannot process .{extension} files. Please upload a valid file with extension .csv, .xlsx, or enter the URL."
            }), 500
        
    uploaded_file.save(os.path.join(app.config["UPLOADS_DIR"], filename))

    if filename.endswith(".csv"):
        data = readCSV(os.path.join(app.config["UPLOADS_DIR"], filename))
    elif filename.endswith(".xlsx"):
        data = readXLSX(os.path.join(app.config["UPLOADS_DIR"], filename))



    for record in data:
        
        d = json.dumps({
            "phone_number" : record["phone_number"],
            "run_time" : record["run_time"],
            "created_at" : datetime.now()
        }, cls = DateTimeEncoder)
        
        d = data_schema_single.loads(d)
        
        d = Data(
            phone_number = d["phone_number"],
            run_time = d["run_time"],
            created_at = d["created_at"]
        )
        
        db.session.add(d)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            pass

    # result = data_schema_multiple.dump(data)
        
    return make_response(
        { "message" : f"{len(data)} row(s) added successfully !."},
        201
    )

@app.route("/<int:id>", methods = ["GET", "POST"])
def query_by_id(id):
    
    response = Data.query.filter_by(id = id).first()

    serialized_response = data_schema_single.dump(response)

    return make_response(
        {"result" : serialized_response or f"No data found for id = {id}"},
        200
    )


if __name__ == "__main__":
    app.run(debug = True, threaded = True)



