from playwright.sync_api import expect


def test_products_button_opens_products_page(page):
    page.goto("https://automationexercise.com/") # Открываем главную страницу сайта
    products_link = page.get_by_role("link", name="Products") # Находим ссылку "Products" (тег <a>)
    expect(products_link).to_be_visible() # Проверяем что ссылка видна пользователю
    products_link.click() # Нажимаем на ссылку "Products"
    expect(page).to_have_url("https://automationexercise.com/products") # Проверяем, что после клика мы перешли на страницу /products
    expect(page.get_by_text("All Products")).to_be_visible     # Проверяем что на странице есть заголовок All Products
    expect(page.get_by_text("View Product").first).to_be_visible() # Проверяем что товары отображаются и есть кнопка "View Product"
