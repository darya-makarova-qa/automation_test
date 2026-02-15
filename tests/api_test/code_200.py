import requests  # библиотека для HTTP-запросов (GET/POST и т.д.)


def test_api_products_list_returns_products():
    # 1) URL эндпоинта, который мы тестируем
    url = "https://automationexercise.com/api/productsList"

    # 2) Отправляем GET-запрос на API
    response = requests.get(url, timeout=30)

    # 3) Проверяем, что сервер ответил HTTP-статусом 200 (успех на уровне HTTP)
    assert response.status_code == 200

    # 4) Парсим тело ответа как JSON (превращаем строку в Python-словарь)
    data = response.json()

    # 5) Проверяем, что в JSON есть поле responseCode (это их “внутренний” код ответа)
    assert "responseCode" in data

    # 6) Проверяем, что их внутренний responseCode тоже 200 (успех по бизнес-логике API)
    assert data["responseCode"] == 200

    # 7) Проверяем, что в ответе есть ключ products
    assert "products" in data

    # 8) Проверяем, что products — это список
    assert isinstance(data["products"], list)

    # 9) Проверяем, что список товаров не пустой
    assert len(data["products"]) > 0

    # 10) Берём первый товар из списка, чтобы проверить структуру (минимальная валидация)
    first_product = data["products"][0]

    # 11) Проверяем, что у товара есть обязательные поля
    assert "id" in first_product
    assert "name" in first_product
    assert "price" in first_product
    assert "brand" in first_product
    assert "category" in first_product
 
    # 12) Проверяем, что category — это словарь, и внутри есть category + usertype
    assert isinstance(first_product["category"], dict)
    assert "category" in first_product["category"]
    assert "usertype" in first_product["category"]

    # 13) Проверяем вложенность usertype (в ответе она выглядит как {"usertype": {"usertype": "Women"}})
    assert isinstance(first_product["category"]["usertype"], dict)
    assert "usertype" in first_product["category"]["usertype"]
