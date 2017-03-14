from io import BytesIO
import io
import PIL
import requests
from PIL import Image
import gridfs
from pymongo import MongoClient

small_dimension = 320, 320
medium_dimension = 384, 288
large_dimension = 640, 480
small_str = "small"
medium_str = "medium"
large_str = "large"
images_path = "images/"
app_url = "http://127.0.0.1:5000/"
db = MongoClient().skyhub
fs = gridfs.GridFS(db)


def get_images_urls():
    response = requests.get("http://54.152.221.29/images.json")
    data = response.json()
    image_urls = [image_url['url'] for image_url in data['images']]
    return image_urls


def write_image_to_db(image, filename):
    fs.put(image, filename=filename, contentType="image/jpeg")


def write_images_to_db():
    urls = get_images_urls()
    i = 0
    for image_url in urls:
        image = requests.get(image_url)
        filename = "image" + str(i)
        write_image_to_db(image.content, filename)
        resized_images = generate_resized_images(image.content)
        save_resized_images(resized_images, filename)
        save_image_info(filename)
        i += 1


def generate_resized_images(image):
    images = {small_str: resize_image(image, small_dimension),
              medium_str: resize_image(image, medium_dimension),
              large_str: resize_image(image, large_dimension)}
    return images


def resize_image(image_content, size):
    image = Image.open(BytesIO(image_content))
    return image.resize(size, PIL.Image.BICUBIC)


def save_resized_images(images, original_filename):
    for size_str, image in images.items():
        filename = generate_filename(original_filename, size_str)
        save_resized_image(image, filename)


def save_resized_image(resized_image, filename):
    img_io = io.BytesIO()
    resized_image.save(img_io, 'JPEG')
    img_io.seek(0)
    write_image_to_db(img_io, filename)


def save_image_info(filename):
    small_filename = generate_filename(filename, small_str)
    medium_filename = generate_filename(filename, medium_str)
    large_filename = generate_filename(filename, large_str)
    image = {"original_url": app_url + images_path + filename,
             "small_url": app_url + images_path + small_filename,
             "medium_url": app_url + images_path + medium_filename,
             "large_url": app_url + images_path + large_filename}
    images = db.images
    images.insert_one(image)


def generate_filename(filename, size_str):
    return filename + "_" + size_str


def get_all_images_from_db():
    return db.images.find()


def get_image_from_db(image_name):
    return fs.get_last_version(filename=image_name)
