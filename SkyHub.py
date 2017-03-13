import requests
import os
from PIL import Image
import gridfs

small = 320, 320
medium = 384, 288
large = 640, 480
image_folder = "images/"



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
        file = open(image_folder + "image" + str(i) + ".jpg", 'wb')
        file.write(image.content)
        i += 1


def write_images_to_db(db):
    urls = get_images_urls()
    fs = gridfs.GridFS(db)
    i = 0
    for image_url in urls:
        image = requests.get(image_url, stream=True)
        fs.put(image.raw, filename="image" + str(i) + ".jpg", contentType="image/jpeg")
        i += 1


def resize_images():
    images = os.listdir(image_folder)
    for image_name in images:
        image = Image.open(image_folder + image_name)
        image.thumbnail(small)
        splitted_image_name = image_name.split(".")
        image.save(image_folder + splitted_image_name[0] + "_small." + splitted_image_name[1])



def main():


    write_images_to_disk()
    resize_images()

if __name__ == '__main__':
    main()



