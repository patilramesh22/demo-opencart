import pytest
from pages.launchpage import LaunchPage
from pages.loginpage import LoginPage
from pages.registerpage import RegisterPage


@pytest.mark.usefixtures("setup")
class TestRegister:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.rp = RegisterPage(self.driver)
        self.lgp = LoginPage(self.driver)

    def test_register_from_myaccount_button(self):
        self.lp.click_on_my_account_option()
        self.lp.click_on_register_option()
        self.rp.register_account("abc", "xyz", "test123@prqs.com", "test@123")
        result = self.rp.verify_account_is_created()
        assert result

    def test_register_from_login_page(self):
        self.lgp.click_on_myaccount_option()
        self.lgp.click_on_login_option()
        self.lgp.click_on_continue_btn()
        self.rp.register_account("abc", "xyz", "test123@prqs.com", "test@123")
        result = self.rp.verify_account_is_created()
        assert result

    def test_register_from_right_column_option(self):
        self.lgp.click_on_myaccount_option()
        self.lgp.click_on_login_option()
        self.lgp.click_on_register_from_right_column_option()
        self.rp.register_account("abc", "xyz", "test123@prqs.com", "test@123")
        result = self.rp.verify_account_is_created()
        assert result
