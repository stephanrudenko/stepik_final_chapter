import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage

@pytest.mark.need_review
@pytest.mark.parametrize("promo_offer", [0, 1, 2, 3, 4, 5, 6,
                                         pytest.param(7, marks=pytest.mark.xfail(reason="founded promo link with bug - (expected behaviour)")),
                                         8, 9]) 
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)           
    page.open()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
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

@pytest.mark.skip(reason="works as expected")   
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review 
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review  
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.com"
        password = "itsmypassword9999$"
        confirm_password = f"{password}"
        page.register_new_user(email, password, confirm_password)
        base_page = BasePage(browser, browser.current_url)
        base_page.should_be_authorized_user()

    @pytest.mark.xfail(reason="works as expected, used 'should_not_be...'")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart_button()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)           
        page.open()
        page.add_to_cart_button()
        page.solve_quiz_and_get_code()
        page.correct_item_in_cart()
        page.correct_price_in_cart()

