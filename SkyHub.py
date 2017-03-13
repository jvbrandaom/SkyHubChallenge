from io import BytesIO
import io
import requests
import os
from PIL import Image
import gridfs

small = 320, 320
medium = 384, 288
large = 640, 480
images_path = "images/"
app_url = "http://127.0.0.1:5000/"


def get_images_urls():
    response = requests.get("http://54.152.221.29/images.json")
    data = response.json()
    image_urls = [image_url['url'] for image_url in data['images']]

    return image_urls


def write_images_to_disk():
    urls = get_images_urls()
    i = 0
    for image_url in urls:
        image = requests.get(image_url)
        file = open(images_path + "image" + str(i) + ".jpg", 'wb')
        file.write(image.content)
        i += 1


def write_images_to_db(db):
    urls = get_images_urls()
    fs = gridfs.GridFS(db)
    i = 0
    for image_url in urls:
        image = requests.get(image_url)
        filename = "image" + str(i)
        small_filename = filename + "_small"
        medium_filename = filename + "_medium"
        large_filename = filename + "_large"
        fs.put(image.content, filename=filename, contentType="image/jpeg")
        resize_image(db, image.content, small, small_filename)
        resize_image(db, image.content, medium, medium_filename)
        resize_image(db, image.content, medium, large_filename)
        save_image_info(db, filename, small_filename, medium_filename, large_filename)
        i += 1


def resize_image(db, image_content, size, filename):
    fs = gridfs.GridFS(db)
    image_small = Image.open(BytesIO(image_content))
    image_small.thumbnail(size)
    img_io = io.BytesIO()
    image_small.save(img_io, 'JPEG')
    img_io.seek(0)
    fs.put(img_io, filename=filename, contentType="image/jpeg")


def save_image_info(db, filename, small_filename, medium_filename, large_filename):
    image = {"original_url": app_url + images_path + filename,
             "small_url": app_url + images_path + small_filename,
             "medium_url": app_url + images_path + medium_filename,
             "large_url": app_url + images_path + large_filename}
    images = db.images
    images.insert_one(image)


def main():


    write_images_to_disk()

if __name__ == '__main__':
    main()



