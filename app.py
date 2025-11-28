from flask import Flask,request,jsonify
from main import zipUpload

import io
app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Flask is working!"
@app.route('/upload',methods=['POST'])
def upload():
    # upload_file=request.files.get["file"]
    upload_file = request.files.get("file")
    if not upload_file:
        return{"error: no file uploaded"},400
    
    file_bytes=upload_file.read()
    zip_bytes=io.BytesIO(file_bytes)
    results=zipUpload(zip_bytes)
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
