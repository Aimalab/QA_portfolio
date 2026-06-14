import pytest
from pages.login_page import LoginPage


class TestLogin:

    def test_successful_login(self, driver):
        """TC-001: Успешная авторизация с корректными данными"""
        page = LoginPage(driver)
        page.open()
        page.login("standard_user", "secret_sauce")

        assert "inventory" in driver.current_url, "Не перешли на страницу товаров"

    def test_wrong_password(self, driver):
        """TC-002: Авторизация с неверным паролем"""
        page = LoginPage(driver)
        page.open()
        page.login("standard_user", "wrong_password")

        error = page.get_error_message()
        assert "Epic sadface" in error, "Сообщение об ошибке не появилось"

    def test_empty_fields(self, driver):
        """TC-003: Авторизация с пустыми полями"""
        page = LoginPage(driver)
        page.open()
        page.click_login()

        error = page.get_error_message()
        assert "Username is required" in error, "Нет ошибки валидации"

    def test_locked_user(self, driver):
        """TC-004: Заблокированный пользователь"""
        page = LoginPage(driver)
        page.open()
        page.login("locked_out_user", "secret_sauce")

        error = page.get_error_message()
        assert "locked out" in error, "Нет сообщения о блокировке"

    def test_empty_password(self, driver):
        """TC-005: Только логин, пароль пустой"""
        page = LoginPage(driver)
        page.open()
        page.enter_username("standard_user")
        page.click_login()

        error = page.get_error_message()
        assert "Password is required" in error, "Нет ошибки про пароль"