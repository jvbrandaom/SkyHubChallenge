import unittest
import os
import SkyHub
from SkyHub import get_images_urls, resize_image, generate_resized_images

test_images_folder = "test_images/"


class TestSkyHub(unittest.TestCase):
    def test_image_urls_amount(self):
        images_urls = get_images_urls()
        self.assertEqual(len(images_urls), 10)

    def test_resize_image_small(self):
        for image in os.listdir(test_images_folder):
            file = open(test_images_folder + image, 'rb')
            resized_image = resize_image(file.read(), SkyHub.small_dimension)
            width, height = resized_image.size

        self.assertEqual((width, height), SkyHub.small_dimension)

    def test_resize_image_medium(self):
        for image in os.listdir(test_images_folder):
            file = open(test_images_folder + image, 'rb')
            resized_image = resize_image(file.read(), SkyHub.medium_dimension)
            width, height = resized_image.size

        self.assertEqual((width, height), SkyHub.medium_dimension)

    def test_resize_image_large(self):
        for image in os.listdir(test_images_folder):
            file = open(test_images_folder + image, 'rb')
            resized_image = resize_image(file.read(), SkyHub.large_dimension)
            width, height = resized_image.size

        self.assertEqual((width, height), SkyHub.large_dimension)

    def test_generate_resized_images(self):
        file = open(test_images_folder + "image0.jpg", 'rb')
        resized_images = generate_resized_images(file.read())
        self.assertEqual(resized_images[SkyHub.small_str].size, SkyHub.small_dimension)
        self.assertEqual(resized_images[SkyHub.medium_str].size, SkyHub.medium_dimension)
        self.assertEqual(resized_images[SkyHub.large_str].size, SkyHub.large_dimension)


if __name__ == '__main__':
    unittest.main()
