
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import sys
from dxf_creator import create_dxf_document, setup_layers
from osm_processor import process_osm_file
from config import LAYER_MAPPING

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.abspath('uploads')
OUTPUT_FOLDER = os.path.abspath('output')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/convert', methods=['POST'])
def convert_osm_to_dxf():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = file.filename
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_filename = os.path.splitext(filename)[0] + '.dxf'
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        file.save(input_path)

        try:
            doc = create_dxf_document()
            msp = doc.modelspace()
            setup_layers(doc, LAYER_MAPPING)
            process_osm_file(input_path, msp)
            doc.saveas(output_path)
            
            return send_file(output_path, as_attachment=True)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)

