from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.greenCart import GreenCart


def test_sorting(browserInstance):
    driver = browserInstance
    browserSortedVeggies = []
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    greenCart = GreenCart(driver)
    greenCart.sorting1(browserSortedVeggies)
