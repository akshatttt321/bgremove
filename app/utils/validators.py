import requests
from PIL import Image
import io

def validate_input(data):
    response = requests.get(data['image_url'])
    original_image = Image.open(io.BytesIO(response.content))

    if not all(key in data for key in ['image_url', 'bounding_box']):
        return {"valid": False, "message": "Missing required fields"}
    
    try:
        response = requests.head(data['image_url'], timeout=5)
        if response.status_code != 200:
            return {"valid": False, "message": "Invalid image URL"}
    except:
        return {"valid": False, "message": "Could not access image URL"}
    
    box = data['bounding_box']
    required_keys = ['x_min', 'y_min', 'x_max', 'y_max']
    if not all(key in box for key in required_keys):
        return {"valid": False, "message": "Invalid bounding box format"}

    if box['x_min'] < 0 or box['y_min'] < 0 or box['x_max'] > original_image.width or box['y_max'] > original_image.height:
        return {"valid": False, "message": "Bounding box is out of image bounds"}
    
    return {"valid": True}