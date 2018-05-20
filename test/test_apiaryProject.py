import unittest

from apiaryProject import processes


class TestProcessesMethods(unittest.TestCase):

    def setUp(self):
        self.page = processes.get_page("https://apiary.docs.apiary.io")
        self.post = processes.post_to_page("https://api.apiary.io/blueprint/publish/publicpersonalapi",
                                           "myFile.json")
        self.error_content = '{"error":1,"message":"This resource requires authenticated API call."}'

    def test_get_page_return_code(self):
        self.assertEqual(self.page.status_code, 200)

    def test_post_page_return_code(self):
        self.assertEqual(self.post.status_code, 403)

    def test_post_page_content(self):
        self.assertEqual(self.post.content, self.error_content)

    def tearDown(self):
        # empty list (not to keep in memory)
        self.page = None
        self.post = None


if __name__ == '__main__':
    unittest.main()
