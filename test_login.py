import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import geckodriver_autoinstaller
import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestLogin:
    def setup_method(self):
        """Setup browser before each test"""
        geckodriver_autoinstaller.install()
        
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        
        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.maximize_window()
        
        # Initialize page objects
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        
        # Open login page
        self.login_page.open()
        time.sleep(2)  # Wait for page load
    
    def teardown_method(self):
        """Close browser after each test"""
        time.sleep(1)
        self.driver.quit()

    def test_successful_login(self):
        """Test login with valid credentials"""
        # Perform login
        self.login_page.login("standard_user", "secret_sauce")
        
        # Verify successful login
        assert self.products_page.get_page_title() == "Products"
        assert self.products_page.is_on_products_page()
        assert self.products_page.get_products_count() > 0
    
    def test_login_with_invalid_credentials(self):
        """Test login with invalid credentials"""
        # Attempt login with invalid credentials
        self.login_page.login("invalid_user", "wrong_password")
        
        # Verify error message
        assert self.login_page.is_error_displayed()
        assert "Username and password do not match" in self.login_page.get_error_message()
    
    def test_empty_credentials(self):
        """Test login with empty credentials"""
        self.login_page.login("", "")
        
        assert self.login_page.is_error_displayed()
        assert "Username is required" in self.login_page.get_error_message()