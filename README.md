# Python Selenium Pet Project

Проект для изучения автоматизированного тестирования с использованием Python, Selenium и pytest.

## 🎯 Описание

Этот проект содержит:
- **UI тесты** для сайта [SauceDemo](https://www.saucedemo.com/) с использованием Selenium WebDriver
- **API тесты** для различных REST API с использованием библиотеки requests
- Реализацию паттерна **Page Object Model** для UI тестов

## 🚀 Структура проекта

```
python-selenium-pet-project/
├── pages/                      # Page Object Model классы
│   ├── __init__.py
│   ├── base_page.py           # Базовый класс для всех страниц
│   ├── login_page.py          # Страница логина SauceDemo
│   └── products_page.py       # Страница товаров SauceDemo
├── test_login.py              # UI тесты для SauceDemo
├── test_api_reqres.py         # API тесты (ReqRes + HttpBin)
├── requirements.txt           # Зависимости проекта
├── pytest.ini               # Конфигурация pytest
└── README.md                 # Этот файл
```

## 🛠 Технологии

- **Python 3.9+**
- **Selenium WebDriver** - для UI тестирования
- **pytest** - фреймворк для тестирования
- **requests** - для API тестирования
- **Firefox WebDriver** - браузер для запуска UI тестов

## ⚙️ Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone <your-repo-url>
   cd python-selenium-pet-project
   ```

2. **Установите зависимости:**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Убедитесь, что Firefox установлен** (geckodriver устанавливается автоматически)

## 🧪 Запуск тестов

### Все тесты
```bash
# Запустить все тесты
python3 -m pytest -v

# Запустить все тесты без warnings
python3 -m pytest -v --disable-warnings
```

### UI тесты (SauceDemo)
```bash
# Только UI тесты
python3 -m pytest test_login.py -v

# Конкретный UI тест
python3 -m pytest test_login.py::TestLogin::test_successful_login -v
```

### API тесты
```bash
# Только API тесты
python3 -m pytest test_api_reqres.py -v

# Только HttpBin API тесты
python3 -m pytest test_api_reqres.py::TestHttpBinAPI -v

# Только ReqRes API тесты
python3 -m pytest test_api_reqres.py::TestReqResAPI -v
```

### HTML отчеты
```bash
# Создать HTML отчет
python3 -m pytest --html=report.html --self-contained-html -v
```

## 📋 Покрытие тестами

### UI тесты (SauceDemo)
- ✅ Успешный логин с валидными данными
- ✅ Логин с невалидными данными
- ✅ Логин с пустыми полями
- ✅ Проверка перехода на страницу товаров
- ✅ Валидация сообщений об ошибках

### API тесты

**ReqRes API:**
- ✅ GET запрос списка пользователей
- ✅ GET запрос одного пользователя
- ✅ Проверка структуры JSON ответа

**HttpBin API:**
- ✅ GET, POST, PUT, DELETE запросы
- ✅ Работа с query параметрами
- ✅ Проверка заголовков ответа
- ✅ Тестирование различных HTTP статус кодов
- ✅ Проверка времени ответа
- ✅ Basic Authentication
- ✅ Custom User-Agent

## 🏗 Page Object Model

Проект использует паттерн Page Object Model для UI тестов:

- **BasePage** - базовый класс с общими методами
- **LoginPage** - методы для работы со страницей логина
- **ProductsPage** - методы для работы со страницей товаров

### Пример использования:
```python
# Инициализация
login_page = LoginPage(driver)
products_page = ProductsPage(driver)

# Использование
login_page.open()
login_page.login("standard_user", "secret_sauce")
assert products_page.is_on_products_page()
```

## 🐛 Troubleshooting

### Проблемы с WebDriver
```bash
# Если проблемы с Firefox, попробуйте обновить geckodriver
pip3 install --upgrade geckodriver-autoinstaller
```

### Проблемы с зависимостями
```bash
# Переустановка зависимостей
pip3 install --upgrade -r requirements.txt
```

### Warnings от urllib3
Warnings подавляются в `pytest.ini`. Если они все еще появляются:
```bash
python3 -m pytest -v --disable-warnings
```

## 📝 Конфигурация

### pytest.ini
Содержит настройки pytest:
- Подавление warnings
- Маркеры для категоризации тестов
- Параметры вывода

### requirements.txt
Список всех необходимых зависимостей с фиксированными версиями.

## 🚀 Возможные улучшения

- [ ] Добавить тесты для корзины и checkout процесса
- [ ] Реализовать параллельный запуск тестов
- [ ] Добавить поддержку Chrome WebDriver
- [ ] Создать CI/CD pipeline
- [ ] Добавить Allure отчеты
- [ ] Реализовать Data-Driven тесты
- [ ] Добавить логирование

## 🤝 Участие в проекте

Этот проект создан в учебных целях для изучения автоматизированного тестирования.

## 📄 Лицензия

Проект создан в образовательных целях.