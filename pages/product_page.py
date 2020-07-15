from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def check_product_name_and_sum(self):
        name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_ON_PAGE)
        check_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        total = self.browser.find_element(*ProductPageLocators.CHECKING_SUM)
        assert name.text == check_name.text and price.text == total.text, \
            "Product name is wrong or Price is different to sum"
