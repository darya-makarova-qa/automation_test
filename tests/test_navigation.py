def test_logo_refreshes_page(page):
    page.goto("https://automationexercise.com/", wait_until="domcontentloaded", timeout=60000)

    with page.expect_navigation(wait_until="domcontentloaded"):
        page.locator("div.logo a").click()

    assert page.url.rstrip("/") == "https://automationexercise.com"


def test_products_button_opens_products_page(page):
    page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    page.locator("a[href='/products']").click()

    page.wait_for_url("**/products")

    assert page.locator(".features_items").is_visible()


def test_cart_button_opens_cart_page(page):
    # 1) Открываем главную страницу
    page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    # 2) Кликаем именно по ссылке "Cart" (а не по "View Cart")
    #    get_by_role ищет элемент по "роли" (link/button) и видимому имени.
    page.get_by_role("link", name="Cart").click()

    # 3) Ждём, пока откроется нужный URL
    page.wait_for_url("**/view_cart")

    # 4) Проверяем, что мы действительно на странице корзины
    assert "/view_cart" in page.url

    # 5) Дополнительно убеждаемся, что на странице есть текст "Shopping Cart"
    assert page.locator("text=Shopping Cart").is_visible()



from playwright.sync_api import expect

def test_signup_login_button_opens_login_page(page):
    # 1) Открываем главную страницу сайта и ждём, пока прогрузится DOM
    page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    # 2) Кликаем по ссылке Signup / Login (по href — самый стабильный вариант)
    page.locator("a[href='/login']").click()

    # 3) Ждём, что мы точно оказались на странице /login
    page.wait_for_url("**/login")

    # 4) Дополнительно убеждаемся, что URL действительно содержит /login
    assert "/login" in page.url

    # 5) Находим именно форму Login (а не Signup), потому что на странице их две
    login_form = page.locator("form").filter(has_text="Login")

    # 6) Проверяем, что форма Login видима
    expect(login_form).to_be_visible()

    # 7) Внутри формы Login проверяем видимость поля Email Address
    expect(login_form.get_by_placeholder("Email Address")).to_be_visible()

    # 8) Внутри формы Login проверяем видимость поля Password
    expect(login_form.locator("input[name='password']")).to_be_visible()

