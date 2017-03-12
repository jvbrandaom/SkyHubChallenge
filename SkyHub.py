import requests


def get_images_urls():
    response = requests.get("http://54.152.221.29/images.json")
    data = response.json()
    image_urls = [image_url['url'] for image_url in data['images']]

    return image_urls

get_images_urls()
