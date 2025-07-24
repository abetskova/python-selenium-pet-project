import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import geckodriver_autoinstaller
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage

class TestNavigation:
    def setup_method(self):
        geckodriver_autoinstaller.install()
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.navigation_page = NavigationPage(self.driver)
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")
        time.sleep(2)

    def teardown_method(self):
        time.sleep(1)
        self.driver.quit()

    def test_navigation_menu(self):
        # Открыть меню
        self.navigation_page.open_menu()
        assert self.navigation_page.is_sidebar_visible()

        # Перейти на страницу "All Items"
        self.navigation_page.click_all_items()
        assert "inventory.html" in self.driver.current_url

        # Открыть меню и перейти на "About"
        self.navigation_page.open_menu()
        self.navigation_page.click_about()
        assert "saucelabs.com" in self.driver.current_url

        # Вернуться на сайт и открыть меню для сброса состояния
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.navigation_page.open_menu()
        self.navigation_page.click_reset_app()
        assert self.navigation_page.is_sidebar_visible()

        # Закрыть меню (если нужно)
        self.navigation_page.close_menu()

        # Открыть меню и выйти
        self.navigation_page.open_menu()
        self.navigation_page.click_logout()
        assert self.driver.current_url == "https://www.saucedemo.com/"
        
        # Проверка, что поле логина отображается
        from selenium.webdriver.common.by import By
        assert self.driver.find_element(By.ID, "user-name").is_displayed()