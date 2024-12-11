from flask import Flask, request, jsonify
from services.image_processor import process_image
from .services.storage_service import upload_cloudinary
from .utils.validators import validate_input

app = Flask(__name__)

@app.route('/remove-background', methods=['POST'])
def remove_background():
    data = request.json
    
    validation_result = validate_input(data)

    if not validation_result['valid']:
        return jsonify({"error": validation_result['message']}), 400
    
    try:
        # Process image
        processed_image = process_image(
            data['image_url'], 
            data['bounding_box']
        )


        
        processed_url = upload_cloudinary(processed_image)
        
        return jsonify({
            "original_image_url": data['image_url'],
            "processed_image_url": processed_url['secure_url']
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500