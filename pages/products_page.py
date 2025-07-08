from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductsPage(BasePage):
    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    
    def get_page_title(self):
        """Get page title text"""
        return self.get_text(self.PAGE_TITLE)
    
    def is_on_products_page(self):
        """Check if user is on products page"""
        return "inventory.html" in self.get_current_url()
    
    def get_products_count(self):
        """Get number of products displayed"""
        return len(self.find_elements(self.INVENTORY_ITEMS))
    
    def add_first_product_to_cart(self):
        """Add first product to cart"""
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if buttons:
            buttons[0].click()
        return self
    
    def get_cart_items_count(self):
        """Get number of items in cart badge"""
        try:
            badge = self.find_element(self.SHOPPING_CART_BADGE)
            return int(badge.text)
        except:
            return 0
    
    def go_to_cart(self):
        """Click on shopping cart"""
        self.click(self.SHOPPING_CART_LINK)
        return self