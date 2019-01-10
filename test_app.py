import unittest
import app
import requests

class TestFlaskRequest(unittest.TestCase):
    def test_hello(self):
        response = requests.get('http://localhost:5000/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, "Hello Stranger!")

    def test_hello_bob(self):
        response = requests.get('http://localhost:5000/hello?name=bob')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, "Hello bob!")

if __name__ == "__main__":
    unittest.main()