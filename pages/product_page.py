from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_cart_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()
         
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def correct_item_in_cart(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_message = self.browser.find_element(*ProductPageLocators.ITEM_MESSAGE).text
        assert item_name in item_message, "No item name were added to cart"

    def correct_price_in_cart(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE)
        assert item_price.text == total_price.text, "Prices isn`t equal"
        
        
