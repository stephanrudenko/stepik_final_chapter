from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):                         
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Something wrong, basket isn`t empty"

    def should_be_empty_basket_message(self):
        empty_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "basket is empty" in empty_basket, "Looks like your cart is`nt empty"
