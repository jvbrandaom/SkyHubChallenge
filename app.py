import gridfs
from PIL import Image
import io
from pymongo import MongoClient
from flask import Flask, jsonify
from flask import send_from_directory
from flask import send_file

import SkyHub

app = Flask("SkyHubChallenge")
app_url = "http://127.0.0.1:5000/"
db = MongoClient().skyhub
fs = gridfs.GridFS(db)


@app.route("/")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200


@app.route("/images/<image_name>")
def images(image_name):
    image_stream = fs.get_last_version(filename=image_name)
    image = Image.open(image_stream)
    return serve_pil_image(image)


def serve_pil_image(pil_img):
    img_io = io.BytesIO()
    pil_img.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':

    SkyHub.write_images_to_db(db)
    app.run()
