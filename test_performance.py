import pytest
import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import geckodriver_autoinstaller
from pages.login_page import LoginPage

class TestPerformance:
    
    def test_api_response_time(self):
        """Test API response time under 1 second"""
        start_time = time.time()
        response = requests.get("https://httpbin.org/get")
        end_time = time.time()
        
        response_time = end_time - start_time
        
        assert response.status_code == 200
        assert response_time < 1.0, f"Response took {response_time:.2f}s, expected < 1.0s"
    
    def test_multiple_api_requests(self):
        """Test performance with multiple concurrent requests"""
        urls = [
            "https://httpbin.org/get",
            "https://httpbin.org/json", 
            "https://httpbin.org/headers"
        ]
        
        start_time = time.time()
        responses = []
        
        for url in urls:
            response = requests.get(url)
            responses.append(response)
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # All requests should complete successfully
        for response in responses:
            assert response.status_code == 200
        
        # Total time should be reasonable
        assert total_time < 5.0, f"Multiple requests took {total_time:.2f}s, expected < 5.0s"
    
    def test_page_load_time(self):
        """Test SauceDemo page load time"""
        geckodriver_autoinstaller.install()
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")  # Headless for faster execution
        
        driver = webdriver.Firefox(options=firefox_options)
        
        try:
            start_time = time.time()
            driver.get("https://www.saucedemo.com/")
            
            # Wait for page to fully load
            login_page = LoginPage(driver)
            login_page.find_element(login_page.USERNAME_FIELD)  # Wait for element
            
            end_time = time.time()
            load_time = end_time - start_time
            
            assert load_time < 5.0, f"Page loaded in {load_time:.2f}s, expected < 5.0s"
            
        finally:
            driver.quit()