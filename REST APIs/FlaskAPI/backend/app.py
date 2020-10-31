"""
    Description :- This script is used to run the complete flask app locally with all the API endpoints.
"""

import json
import os
import csv
from flask import Flask, request, jsonify, abort, make_response
from werkzeug.utils import secure_filename
from Model import Data, DataSchema, db 
from flask_cors import CORS 
from Model import db
from datetime import datetime
from utils.DateTimeEncoder import DateTimeEncoder
from utils.csvreader import readCSV


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

@app.route("/upload", methods = ["POST"])
def upload():
    """
        This function basically parses a .csv or .xlsx or .txt or a file from a url and saves to the database.
    """

    if request.method == "POST":
        
        # UPLOADED FILE
        uploaded_file = request.files["file"]

        filename = secure_filename(uploaded_file.filename)

        if filename != "":
            extension = os.path.splitext(filename)[-1].lower()
            if extension not in app.config["UPLOAD_EXTENSIONS"]:
                abort(400)
            
        uploaded_file.save(os.path.join(app.config["UPLOADS_DIR"], filename))

        if filename.endswith(".csv"):
            data = readCSV(os.path.join(app.config["UPLOADS_DIR"], filename))


        for record in data:
            
            d = json.dumps({
                "phone_number" : record["phone_number"],
                "run_time" : datetime.strptime(record["run_time"], '%d-%m-%y %H:%M:%S'),
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
            except:
                db.session.rollback()
                raise

        result = data_schema_single.dump(data)
            
        return make_response(
            result,
            201
        )



if __name__ == "__main__":
    app.run(debug = True, threaded = True)



