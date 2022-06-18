from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)      # ініціалізуємо Page Object, передаємо в конструктор екземпляр драйверу та url адресу
    page.open()                         # відкриваємо сторінку
    page.go_to_login_page()             # виконуємо метод сторінки - переходимо на сторінку логіну




