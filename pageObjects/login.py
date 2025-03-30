from selenium.webdriver.common.by import By

from Utils.browserUtils import BrowserUtils
from pageObjects.shop import ShopPage


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signInButton = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signInButton).click()
        shopPage = ShopPage(self.driver)  # creating object for upcoming screen which is shop and returning it
        return shopPage
