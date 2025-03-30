from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckOutAndConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_proceedButton = (By.XPATH, "//button[@type='button' and contains(text(),'Checkout')]")
        self.search_countryWith = (By.ID, "country")
        self.conditionsCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchaseButton = (By.XPATH, "//input[@value='Purchase']")
        self.successMessage = (By.CSS_SELECTOR, ".alert-success strong")
        self.checkout_prodName = (By.XPATH, "//h4[@class='media-heading']/a")

    def checkout(self, prod_name):
        prodNameCheckOut = self.driver.find_element(*self.checkout_prodName).text
        assert prod_name == prodNameCheckOut
        self.driver.find_element(*self.checkout_proceedButton).click()

    def countrySelect(self, keywordToSearchCountry, countryToSelect):
        self.driver.find_element(*self.search_countryWith).send_keys(keywordToSearchCountry)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, countryToSelect)))
        self.driver.find_element(By.LINK_TEXT, countryToSelect).click()

    def validate_order(self):
        self.driver.find_element(*self.conditionsCheckbox).click()
        self.driver.find_element(*self.purchaseButton).click()
        successMessage = self.driver.find_element(*self.successMessage).text
        assert "Success" in successMessage
