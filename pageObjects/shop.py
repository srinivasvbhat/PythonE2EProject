from selenium.webdriver.common.by import By

from Utils.browserUtils import BrowserUtils
from pageObjects.checkout_and_confirmation import CheckOutAndConfirmationPage


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.go_to_cart = (By.XPATH, "//div[@id='navbarResponsive']//a")

    def shop(self, prod_name):
        products = self.driver.find_elements(*self.products)
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == prod_name:
                product.find_element(By.CSS_SELECTOR, ".btn-info").click()

    def goToCart(self):
        self.driver.find_element(*self.go_to_cart).click()
        checkout_confirmationPage = CheckOutAndConfirmationPage(self.driver)
        return checkout_confirmationPage
