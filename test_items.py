import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button_shopping_basket(browser):
    browser.get(link)
    time.sleep(30)
    backet = browser.find_element_by_css_selector("#add_to_basket_form")
    button = backet.text
    print(button)
    assert button == "Добавить в корзину"