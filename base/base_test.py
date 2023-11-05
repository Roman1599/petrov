import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_page import PersonalPage
from pages.buzz_page import BuzzPage

class BaseTest:

    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage
    buzz_page: BuzzPage

    @pytest.fixture(autouse=True)
    def setup(self,request,driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)
        request.cls.buzz_page = BuzzPage(driver)

