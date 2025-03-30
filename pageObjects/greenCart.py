from selenium.webdriver.common.by import By

from Utils.browserUtils import BrowserUtils


class GreenCart(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fruitVeggieNameColumn = (By.XPATH, "//span[text()='Veg/fruit name']")
        self.allfruitVeggies = (By.XPATH, "//tr/td[1]")

    def sorting1(self, browserSortedVeggies):
        self.driver.find_element(*self.fruitVeggieNameColumn).click()

        veggieWebElements = self.driver.find_elements(*self.allfruitVeggies)
        for ele in veggieWebElements:
            browserSortedVeggies.append(ele.text)

        originalBrowserSortedVeggies = browserSortedVeggies.copy()
        browserSortedVeggies.sort()
        assert browserSortedVeggies == originalBrowserSortedVeggies
