from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    PASSWORD_FIELD_CONFIRM = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
    REGISTER_USER = (By.CSS_SELECTOR, ".register_form button.btn.btn-lg.btn-primary")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")
    
