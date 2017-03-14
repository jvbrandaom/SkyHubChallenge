from PIL import Image
import io
from flask import Flask, jsonify
from flask import send_file
import SkyHub

app = Flask("SkyHubChallenge")


@app.route("/")
@app.route("/images/")
def images():
    image_list = []
    # removes id attribute from response since it's not relevant to expose such a internal information on this service
    for image_entry in SkyHub.get_all_images_from_db():
        del image_entry["_id"]
        image_list.append(image_entry)

    return jsonify(image_list)


@app.route("/images/<image_name>")
def image(image_name):
    image_stream = SkyHub.get_image_from_db(image_name)
    pil_image = Image.open(image_stream)
    return serve_image(pil_image)


def serve_image(pil_img):
    img_io = io.BytesIO()
    pil_img.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


if __name__ == '__main__':
    SkyHub.write_images_to_db()
    app.run()
