import pytest
from pages.launchpage import LaunchPage
from pages.loginpage import LoginPage
from pages.myaccountpage import MyAccountPage
from pages.registerpage import RegisterPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.rp = RegisterPage(self.driver)
        self.lgp = LoginPage(self.driver)
        self.mp = MyAccountPage(self.driver)

    def test_login_from_my_account_option(self):
        self.lp.click_on_my_account_option()
        self.lp.click_on_login_option()
        self.lgp.set_email("abcd@xyz.com")
        self.lgp.set_password("test123")
        self.lgp.click_on_login_btn()
        result = self.mp.verify_my_account_page()
        assert result

    def test_login_from_right_column_option(self):
        self.lp.click_on_my_account_option()
        self.lp.click_on_register_option()
        self.rp.click_on_login_btn_from_right_column_option()
        self.lgp.set_email("abcd@xyz.com")
        self.lgp.set_password("test123")
        self.lgp.click_on_login_btn()
        result = self.mp.verify_my_account_page()
        assert result
