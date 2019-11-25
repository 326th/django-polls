import unittest
from selenium import webdriver

DRIVER_PATH = "C:/Chrome driver/chromedriver.exe"
BROWSER_PATH = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

class TestEndToEnd(unittest.TestCase):

    def set_up(self,driver_path,browser_path):
        """
        set up  browser with custom driver and browser path
        """

        option = webdriver.ChromeOptions()
        option.binary_location = browser_path
        browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        return browser

    def test_find_head1(self):
        """go to /polls and find head1 with the  text of "Polls" """
        browser = self.set_up(DRIVER_PATH,BROWSER_PATH)
        browser.get("http://localhost:8000/polls/")
        element = browser.find_element_by_tag_name("h1")
        self.assertEqual(element.text,"Polls")

    def test_find_polls(self):
        """got to /polls, click the last link and check the url"""
        browser = self.set_up(DRIVER_PATH,BROWSER_PATH)
        browser.get("http://localhost:8000/polls/")
        elements = browser.find_elements_by_name("1")
        elements[-1].click()

        self.assertEqual(browser.current_url,"http://localhost:8000/polls/1/")
