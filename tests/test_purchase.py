import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestPurchase:

    @pytest.fixture(autouse=True)
    def login(self, driver):
        """Авторизуемся перед каждым тестом"""
        page = LoginPage(driver)
        page.open()
        page.login("standard_user", "secret_sauce")
        self.driver = driver

    def test_add_to_cart(self):
        """TC-006: Товар добавляется в корзину"""
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()

        count = inventory.get_cart_count()
        assert count == "1", f"Ожидали 1 товар в корзине, получили: {count}"

    def test_cart_contains_correct_item(self):
        """TC-007: В корзине верный товар"""
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        item_name = cart.get_item_name()
        assert item_name == "Sauce Labs Backpack", f"Неверный товар в корзине: {item_name}"

    def test_successful_purchase(self):
        """TC-008: Полный цикл покупки"""
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        cart.click_checkout()

        checkout = CheckoutPage(self.driver)
        checkout.fill_form("Aima", "Salimova", "190000")
        checkout.click_continue()
        checkout.click_finish()

        success = checkout.get_success_message()
        assert "Thank you" in success, f"Заказ не оформлен, получили: {success}"

    def test_checkout_without_filling_form(self):
        """TC-009: Оформление без заполнения формы"""
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        cart.click_checkout()

        checkout = CheckoutPage(self.driver)
        checkout.click_continue()

        error = checkout.get_error_message()
        assert "First Name is required" in error, f"Нет ошибки валидации: {error}"

    def test_remove_item_from_cart(self):
        """TC-010: Удаление товара из корзины"""
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        cart.remove_item()

        items = cart.get_cart_items()
        assert len(items) == 0, f"Товар не удалился, в корзине: {len(items)} товаров"