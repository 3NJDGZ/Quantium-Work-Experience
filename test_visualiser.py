import unittest
from visualise_data import app
from selenium.webdriver.common.by import By

class TestVisualiseData(unittest.TestCase):
    def test_if_header_exists(self):
        app.run_server()
        element = app.driver.find_elements_by_css_selector("#header")
        self.assertTrue(element)

    def test_if_visualization_exists(self):
        app.run_server()
        element = app.driver.find_elements_by_css_selector("#visualization")
        self.assertTrue(element)

    def test_if_region_picker_exists(self):
        app.run_server()
        element = app.driver.find_elements_by_css_selector("#region_picker")
        self.assertTrue(element)

if __name__ == '__main__':
    unittest.main()