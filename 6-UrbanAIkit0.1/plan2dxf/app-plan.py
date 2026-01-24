from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import cv2
import ezdxf
import numpy as np
import os

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert_to_dxf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = file.filename
        filepath = os.path.join('./', filename)
        file.save(filepath)

        try:
            img = cv2.imread(filepath)
            if img is None:
                raise ValueError("图片加载失败，请检查路径或将图片放到英文路径下再试。")

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
            contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            epsilon = 2.0
            polylines = [cv2.approxPolyDP(cnt, epsilon, closed=True) for cnt in contours]

            dxf_path = os.path.join('./', filename.replace('.jpg', '.dxf').replace('.png', '.dxf'))
            doc = ezdxf.new('R2010')
            msp = doc.modelspace()
            road_width = float(request.form.get('road_width', 5.0))

            for poly in polylines:
                points = poly.squeeze().tolist()
                if isinstance(points[0], int) or len(points) <= 1:
                    continue
                msp.add_lwpolyline(points, close=True, dxfattribs={'const_width': road_width})

            doc.saveas(dxf_path)
            
            return send_file(dxf_path, as_attachment=True)

        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
