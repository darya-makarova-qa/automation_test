# tests/conftest.py

import os  # нужен, чтобы читать переменные окружения (HEADLESS)
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    """
    Фикстура page:
    - запускает Playwright
    - открывает браузер + новую вкладку (page)
    - отдаёт page в тесты
    - после теста закрывает браузер
    """

    # Читаем переменную окружения HEADLESS
    # Если HEADLESS=true -> headless режим (без окна)
    # Если HEADLESS не задан -> будет false -> окно будет видно (удобно для обучения)
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    with sync_playwright() as p:
        # Запускаем Chromium. headless зависит от переменной окружения
        browser = p.chromium.launch(headless=headless)

        # Открываем новую страницу (вкладку)
        page = browser.new_page()

        # Увеличиваем таймаут навигации (по умолчанию 30 сек)
        page.set_default_navigation_timeout(60000)

        # Увеличиваем общий таймаут ожиданий
        page.set_default_timeout(10000)

        # Передаём page в тест
        yield page

        # Закрываем браузер после теста
        browser.close()