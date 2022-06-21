from selenium.webdriver.common.by import By

#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")
    
