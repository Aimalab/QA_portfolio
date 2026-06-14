from selenium.webdriver.common.by import By


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def __init__(self, driver):
        self.driver = driver

    def open(self, driver):
        self.driver.get(self.URL)

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()