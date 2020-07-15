from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.NOT_EMPTY_BASKET), \
            "Basket is not empty, but should be"

    def should_be_empty_message(self):
        lst_a = self.browser.find_elements(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert len(lst_a) == 1, "There is no 'Your basket is empty' message"

    def basket_is_not_empty(self):
        lst_a = self.browser.find_elements(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert len(lst_a) > 1, "There is empty basket"

