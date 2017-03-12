import unittest
from SkyHub import get_images_urls


class TestSkyHub(unittest.TestCase):
    def test_image_urls_amount(self):
        images_urls= get_images_urls()
        self.assertEqual(len(images_urls), 10)

if __name__ == '__main__':
    unittest.main()
