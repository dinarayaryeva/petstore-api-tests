# Тесты API Petstore

Этот проект содержит автоматические тесты для API Petstore, используя Python, Pytest и Requests.

## Структура
```
petstore-api-tests/
├── tests/
│   ├── petstore_api.py
│   ├── test_petstore.py
│   ├── test_petstore_negative.py
├── requirements.txt
├── README.md
├── pytest.ini
└── .gitignore
```

## Настройка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/petstore-api-tests.git
   cd petstore-api-tests
2. Создайте и активируйте виртуальное окружение (необязательно, но рекомендуется):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4. Чтобы запустить тесты, используйте:
    ```bash
    pytest
    ```
## Описание тестов
Тесты базовых методов:
- `test_get_pet_by_id`: Тестирует метод GET для получения питомца по его ID.
- `test_create_pet`: Тестирует метод POST для создания нового питомца.
- `test_update_pet`: Тестирует метод PUT для обновления существующего питомца.
- `test_delete_pet`: Тестирует метод DELETE для удаления питомца по его ID.
- `test_find_pets_by_status`: Тестирует поиск питомцев по их статусу, используя метод GET с параметрами.
- `test_update_pet_with_more_parameters`: Тестирует обновление питомца с дополнительными параметрами, используя метод PUT.

Негативные тесты:
- `test_get_nonexistent_pet`: Тестирует метод GET для попытки получить несуществующего питомца.
- `test_create_pet_with_invalid_data`: Тестирует создание питомца с некорректными данными.
- `test_update_pet_with_invalid_data`: Тестирует обновление питомца с некорректными данными.
- `test_delete_pet_with_invalid_id`: Тестирует удаление питомца с некорректным ID.
- `test_get_pet_with_invalid_id`: Тестирует получение питомца с некорректным ID.