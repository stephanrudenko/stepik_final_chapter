import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

@pytest.mark.skip(reason="promo ends")
@pytest.mark.parametrize("promo_offer", [0, 1, 2, 3, 4, 5, 6,
                                         pytest.param(7, marks=pytest.mark.xfail(reason="mistake on page")),
                                         8, 9]) 
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)           
    page.open()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    page.success_message_dissapeared()
    page.correct_item_in_cart()
    page.correct_price_in_cart()

@pytest.mark.skip(reason="works as expected")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.should_not_be_success_message()

@pytest.mark.skip(reason="works as expected")
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip(reason="works as expected")   
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.success_message_disappeared()



