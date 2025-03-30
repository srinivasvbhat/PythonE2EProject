import json
import pytest

from pageObjects.login import LoginPage
test_data_path = "C:\\Users\\shree\\PycharmProjects\\PythonProject\\Data\\test_e2e.json"
with open(test_data_path) as f:  # opening the json file and reading
    test_data = json.load(f)
    test_list = test_data["data"]  # reading dict and storing it as list


@pytest.mark.smoke
# From the list, reading each list item as parametrize method expects a list
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):  # then sending that into method as an argument
    driver = browserInstance
    loginPage = LoginPage(driver)  # creating object for Login class
    print(loginPage.getTitle())
    shopPage = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    # collecting shop page object name returned from login page
    shopPage.shop(test_list_item["prod_name"])
    print(shopPage.getTitle())
    checkout_confirmationPage = shopPage.goToCart()

    checkout_confirmationPage.checkout(test_list_item["prod_name"])
    checkout_confirmationPage.countrySelect(test_list_item["keywordToSearchCountry"],
                                            test_list_item["countryToSelect"])
    checkout_confirmationPage.validate_order()
