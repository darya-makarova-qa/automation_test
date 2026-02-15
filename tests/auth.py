from playwright.sync_api import expect


def test_new_user_signup(page):
    # 1) Открываем страницу логина / регистрации
    page.goto("https://automationexercise.com/login", wait_until="domcontentloaded")

    # 2) Проверяем, что отображается блок "New User Signup!"
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    # 3) Находим поле Name по атрибуту data-qa и вводим имя
    #    data-qa — самый стабильный атрибут для автотестов
    page.locator("[data-qa='signup-name']").fill("Darya")

    # 4) Находим поле Email по data-qa и вводим email
    page.locator("[data-qa='signup-email']").fill("mdara4257@yandex.ru")

    # 5) Нажимаем кнопку Signup (по data-qa)
    page.locator("[data-qa='signup-button']").click()

    # 6) Ждём перехода на следующую страницу регистрации
    #    После клика должна появиться форма "Enter Account Information"
    expect(page.get_by_text("Enter Account Information")).to_be_visible()
