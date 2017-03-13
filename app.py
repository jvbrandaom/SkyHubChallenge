import gridfs
from PIL import Image
import io
from pymongo import MongoClient
from flask import Flask, jsonify
from flask import send_file
from bson.json_util import dumps
import SkyHub

app = Flask("SkyHubChallenge")

db = MongoClient().skyhub
fs = gridfs.GridFS(db)


@app.route("/")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200


@app.route("/images/<image_name>")
def image(image_name):
    image_stream = fs.get_last_version(filename=image_name)
    image = Image.open(image_stream)
    return serve_pil_image(image)


@app.route("/images/")
def images():
    image_list = []
    for image_entry in db.images.find():
        del image_entry["_id"]
        image_list.append(image_entry)

    return jsonify(image_list)


def serve_pil_image(pil_img):
    img_io = io.BytesIO()
    pil_img.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    SkyHub.write_images_to_db(db)
    app.run()
