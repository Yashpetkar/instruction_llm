from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import google.generativeai as genai
import io

app = Flask(_name_)
CORS(app)

api_key = 'AIzaSyA17JhtXqfPCa_CrBz1A8S6Dl08QSd-KnI'
genai.configure(api_key=api_key)

@app.route("/",methods=['GET'])
def home():
    return jsonify("Hello World :-) ")

@app.route('/upload', methods=['POST'])
def upload():
    if 'images' not in request.files:
        return jsonify({"error": "No images part in the request"}), 400

    images = request.files.getlist('images')

    if len(images) < 1 or len(images) > 4:
        return jsonify({"error": "Please upload between 1 to 4 images"}), 400

    image_list = []

    for image_file in images:
        try:
            img = Image.open(image_file)
            image_list.append(img)
        except Exception as e:
            return jsonify({"error": f"Error processing image: {str(e)}"}), 400

    descriptions = []
    vision_model = genai.GenerativeModel('gemini-1.5-flash')

    for idx, img in enumerate(image_list):
        question = f"describe a detailed, step-by-step guide {idx + 1}"
        
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        response = vision_model.generate_content([question, img])
        
        if hasattr(response, 'text'):
            descriptions.append(response.text)
        else:
            descriptions.append(f"Error generating description for image {idx + 1}")

    return jsonify({"descriptions": descriptions}), 200

if _name_ == '_main_':
    app.run(debug=True)
