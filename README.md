# Python Selenium Pet Project

Проект для изучения автоматизированного тестирования с использованием Python, Selenium и pytest.

## 🎯 Описание

Этот проект содержит:
- **UI тесты** для сайта [SauceDemo](https://www.saucedemo.com/) с использованием Selenium WebDriver
- **API тесты** для различных REST API с использованием библиотеки requests
- **Performance тесты** для проверки времени отклика API и загрузки страниц
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
├── test_performance.py        # Performance тесты
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

### Performance тесты
```bash
# Только performance тесты
python3 -m pytest test_performance.py -v

# Конкретный performance тест
python3 -m pytest test_performance.py::TestPerformance::test_api_response_time -v
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

### Performance тесты
- ✅ **API Response Time** - проверка времени отклика API (< 1 секунды)
- ✅ **Multiple API Requests** - производительность при множественных запросах
- ✅ **Page Load Time** - время загрузки страницы SauceDemo (< 5 секунд)
- ✅ Headless режим для быстрого выполнения

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

## ⚡ Performance тестирование

### Метрики производительности:
- **API Response Time** - время отклика REST API
- **Page Load Time** - время загрузки веб-страниц
- **Multiple Requests** - производительность при нагрузке

### Пример performance теста:
```python
def test_api_response_time(self):
    start_time = time.time()
    response = requests.get("https://httpbin.org/get")
    response_time = time.time() - start_time
    
    assert response.status_code == 200
    assert response_time < 1.0  # Должно быть быстрее 1 секунды
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

### Performance тесты слишком медленные
```bash
# Запуск в headless режиме для ускорения
python3 -m pytest test_performance.py -v --disable-warnings
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

- [x] **Добавить performance тесты** ✅
- [ ] Добавить тесты для корзины и checkout процесса
- [ ] Реализовать Data-Driven тесты
- [ ] Реализовать параллельный запуск тестов
- [ ] Добавить поддержку Chrome WebDriver
- [ ] Создать CI/CD pipeline
- [ ] Добавить Allure отчеты
- [ ] Добавить логирование
- [ ] Добавить скриншоты при падении тестов
- [ ] Создать тесты для разных браузеров (Cross-browser testing)
- [ ] Добавить мониторинг производительности в реальном времени

## 🤝 Участие в проекте

Этот проект создан в учебных целях для изучения автоматизированного тестирования.

## 📄 Лицензия

Проект создан в образовательных целях.