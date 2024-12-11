import requests

def validate_input(data):
    
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
    
    return {"valid": True}