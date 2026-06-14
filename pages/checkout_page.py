from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    SUCCESS_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    TOTAL_PRICE = (By.CSS_SELECTOR, "[data-test='total-label']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_success_message(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_HEADER))
        return self.driver.find_element(*self.SUCCESS_HEADER).text

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def get_total_price(self):
        return self.driver.find_element(*self.TOTAL_PRICE).text