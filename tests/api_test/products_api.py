import requests  # библиотека для отправки HTTP-запросов


def test_api_products_list_returns_products(api_base_url):
    # 1️⃣ Формируем полный URL, используя фикстуру api_base_url
    url = f"{api_base_url}/api/productsList"

    # 2️⃣ Отправляем GET-запрос к API
    # timeout защищает от "вечного зависания"
    response = requests.get(url, timeout=30)

    # 3️⃣ Проверяем HTTP-статус (уровень протокола)
    assert response.status_code == 200

    # 4️⃣ Преобразуем тело ответа из JSON-строки в Python-словарь
    data = response.json()

    # 5️⃣ Проверяем внутренний код ответа API
    assert "responseCode" in data
    assert data["responseCode"] == 200

    # 6️⃣ Проверяем, что поле products существует
    assert "products" in data

    # 7️⃣ Проверяем, что products — это список
    assert isinstance(data["products"], list)

    # 8️⃣ Проверяем, что список не пустой
    assert len(data["products"]) > 0

    # 9️⃣ Берём первый товар для проверки структуры
    first_product = data["products"][0]

    # 🔟 Проверяем обязательные поля товара
    assert "id" in first_product
    assert "name" in first_product
    assert "price" in first_product
    assert "brand" in first_product
    assert "category" in first_product

    # 1️⃣1️⃣ Проверяем, что id — число
    assert isinstance(first_product["id"], int)

    # 1️⃣2️⃣ Проверяем, что price начинается с "Rs."
    assert first_product["price"].startswith("Rs.")
