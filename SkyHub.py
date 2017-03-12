import requests


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
        file = open("images/image" + str(i) + ".jpg", 'wb')
        file.write(image.content)
        i += 1


def main():
    write_images_to_disk()

if __name__ == '__main__':
    main()



