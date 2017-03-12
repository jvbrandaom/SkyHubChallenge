import unittest
import os
from SkyHub import get_images_urls
from SkyHub import write_images_to_disk


class TestSkyHub(unittest.TestCase):
    def test_image_urls_amount(self):
        images_urls= get_images_urls()
        self.assertEqual(len(images_urls), 10)

    def test_write_images_to_disk(self):
        write_images_to_disk()
        self.assertEqual(len(os.listdir("images")), 10)

if __name__ == '__main__':
    unittest.main()
