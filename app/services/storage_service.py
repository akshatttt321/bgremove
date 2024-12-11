import cloudinary 
import cloudinary.uploader
import cloudinary.api
import os
from io import BytesIO
from PIL import Image


cloud_name = os.getenv('CLOUD_NAME')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')


cloudinary.config(
    cloud_name=cloud_name,
    api_key=api_key,
    api_secret=api_secret
)


def upload_cloudinary(processed_image):
    try:
        img_byte_arr = BytesIO()
        processed_image.save(img_byte_arr, format='PNG') 
        img_byte_arr.seek(0) 
        processed_url = cloudinary.uploader.upload(img_byte_arr)
        return processed_url
    except Exception as e:
        return f"Error uploading the image: {e}"
