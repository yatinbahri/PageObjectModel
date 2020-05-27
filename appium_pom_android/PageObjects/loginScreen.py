from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Resources.ScreenLocators import Locators



class LoginToEmployee():
    locator_obj = Locators()

    def __init__(self, driver):
        self.driver = driver
        print('Initiated Login Process for an Employee')

        # Local Variables
        self.username_textbox_xpath = driver.find_element(By.XPATH, self.locator_obj.username_textbox_xpath)
        self.password_textbox_xpath = driver.find_element(By.XPATH, self.locator_obj.password_textbox_xpath)
        self.sign_in_button_xpath = driver.find_element(By.XPATH, self.locator_obj.sign_in_button_xpath)

    def enter_username(self, username):
        self.driver.implicitly_wait(10)
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, self.locator_obj.username_textbox_xpath)))
            print('Found Username Element')
        except:
            print('Can not find element on login to validate. Could be the element on Home is updated')
            self.driver.quit()
        self.username_textbox_xpath.clear()
        self.username_textbox_xpath.send_keys(username)

    def enter_password(self, password):
        self.password_textbox_xpath.clear()
        self.password_textbox_xpath.send_keys(password)

    def click_sign_in(self):
        self.sign_in_button_xpath.click()

