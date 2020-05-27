import unittest
from appium import webdriver
from Resources.DesiredCapabilities import desired_capabilities


class BaseSpecification(unittest.TestCase):
    def setUp(self):
        self.desired_caps = desired_capabilities(self)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def tearDown(self):
        self.driver.quit()
