---
title: Bgremove
emoji: 🐠
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
license: mit
short_description: Background removal API in Flash
---
# Background Removal API

This Space provides an API for background removal using a Python-based application.

## Usage

1. Send a POST request to the endpoint `/remove-background` with the required parameters:
   - `image_url`: URL of the image to process.
   - `bounding_box`: The area of the image to process (x_min, y_min, x_max, y_max).

Example request:
```json
{
    "image_url": "https://example.com/image.jpg",
    "bounding_box": {
        "x_min": 0,
        "y_min": 0,
        "x_max": 1000,
        "y_max": 1000
    }
}
