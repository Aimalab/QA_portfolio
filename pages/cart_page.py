from selenium.webdriver.common.by import By


class CartPage:
    CART_ITEM = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEM)

    def get_item_name(self):
        return self.driver.find_element(*self.ITEM_NAME).text

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def remove_item(self):
        self.driver.find_element(*self.REMOVE_BUTTON).click()