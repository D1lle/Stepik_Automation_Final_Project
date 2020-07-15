from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "[name=registration-email]")
    PASSWORD = (By.CSS_SELECTOR, "[name=registration-password1]")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "[name=registration-password2]")
    REGISTER_BTN = (By.CSS_SELECTOR, "[name=registration_submit]")


class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, ".hidden-xs")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner a")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(1)"
                                               ".alert-success strong")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    CHECKING_SUM = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div")
