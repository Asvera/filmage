# FilMage
# version: 1.0
# author: asvera

## Simple Image Processing REST API

FilMage is a REST API built with the Flask micro web framework that allows users to upload images and apply various filters. The API processes the images and returns the filtered images.

### Features

- Apply a variety of image filters such as:
  - blur
  - contour
  - detail
  - edge enhancement
  - edge enhancement more
  - emboss
  - find edges
  - sharpen
  - smooth
  - smooth more
- Upload images through HTTP POST requests.
- Get information about available filters and usage instructions.

### Technologies Used

- Python
- Flask
- PILLOW (Python Imaging Library)
- io module

### Installation

1. **Clone the repository:**

   ```sh
git clone https://github.com/asvera/FilMage.git
cd FilMage
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
	```
### Install the required packages:

```sh
pip install -r requirements.txt
```

### Run the Flask app:

```sh
    python app.py #or flask run
```

### Get available filters and usage information:

```sh
curl http://127.0.0.1:5000/
```
```sh
    curl -X POST -F "Image=@/Path/to/sample.jpeg" http://127.0.0.1:5000/blur/ --output filtered_image.jpeg
```
## Endpoints

    GET /: Provides information about available filters and usage instructions.
    POST /<filter>: Applies the specified filter to the uploaded image and returns the filtered image.
