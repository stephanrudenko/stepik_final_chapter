from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=newYear2019/"
    page = ProductPage(browser, link)           
    page.open()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.correct_item_in_cart()
    page.correct_price_in_cart()



