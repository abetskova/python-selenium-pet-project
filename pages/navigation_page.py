from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class NavigationPage(BasePage):
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    ALL_ITEMS_LINK = (By.ID, "inventory_sidebar_link")
    ABOUT_LINK = (By.ID, "about_sidebar_link")
    RESET_APP_LINK = (By.ID, "reset_sidebar_link")
    SIDEBAR = (By.ID, "menu_button_container")
    CLOSE_MENU_BUTTON = (By.ID, "react-burger-cross-btn")

    def open_menu(self):
        # Проверяем, что меню закрыто (кнопка закрытия не видна)
        try:
            close_btn = self.driver.find_element(*self.CLOSE_MENU_BUTTON)
            if close_btn.is_displayed():
                # Меню уже открыто, не кликаем повторно
                return
        except Exception:
            pass  # Кнопка не найдена, меню закрыто

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )
        self.click(self.MENU_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CLOSE_MENU_BUTTON)
        )

    def close_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLOSE_MENU_BUTTON)
        )
        self.click(self.CLOSE_MENU_BUTTON)
        # Ждем, пока кнопка закрытия исчезнет
        WebDriverWait(self.driver, 10).until_not(
            EC.visibility_of_element_located(self.CLOSE_MENU_BUTTON)
        )

    def click_logout(self):
        self.click(self.LOGOUT_LINK)

    def click_all_items(self):
        self.click(self.ALL_ITEMS_LINK)

    def click_about(self):
        self.click(self.ABOUT_LINK)

    def click_reset_app(self):
        self.click(self.RESET_APP_LINK)

    def is_sidebar_visible(self):
        return self.is_element_present(self.SIDEBAR)