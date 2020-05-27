import unittest
from Resources.BaseSpecifications import BaseSpecification
from PageObjects.loginScreen import LoginToEmployee

'''
Login to the app with valid username and password
'''
USERNAME = "u@m.co"
PASSWORD = "Abc@1234"


class LoginTest(BaseSpecification):

    def test_LoginToEmployee(self):
        driver = self.driver
        login = LoginToEmployee(driver)
        login.enter_username(USERNAME)
        login.enter_password(PASSWORD)
        login.click_sign_in()

if __name__ == '__main__':
    unittest.main()
