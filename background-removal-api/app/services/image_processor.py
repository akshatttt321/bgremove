import cv2
import numpy as np
import requests
from rembg import remove
from PIL import Image
import io as io

def process_image(image_url, bounding_box):

    response = requests.get(image_url)
    original_image = Image.open(io.BytesIO(response.content))
    
    cropped_image = original_image.crop((
        bounding_box['x_min'], 
        bounding_box['y_min'], 
        bounding_box['x_max'], 
        bounding_box['y_max']
    ))
    
    
    processed_image = remove(np.array(cropped_image))
    
    return Image.fromarray(processed_image)