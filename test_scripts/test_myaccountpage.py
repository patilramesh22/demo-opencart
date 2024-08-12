import pytest
from pages.launchpage import LaunchPage
from pages.loginpage import LoginPage
from pages.myaccountpage import MyAccountPage
from pages.registerpage import RegisterPage


@pytest.mark.usefixtures("setup")
class TestMyAccountPage:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.lgp = LoginPage(self.driver)
        self.mp = MyAccountPage(self.driver)

    def test_my_account_page(self):
        self.lp.click_on_my_account_option()
        self.lp.click_on_login_option()
        self.lgp.set_email("abcd@xyz.com")
        self.lgp.set_password("test123")
        self.lgp.click_on_login_btn()
        self.mp.click_on_desktops_link()
        self.mp.click_on_mack_link()
        result = self.mp.get_price_of_mac()
        assert result
