import random
import allure
import pytest
from base.base_test import BaseTest
from pages.buzz_page import BuzzPage



@allure.feature("Profile Functionaloty")
class TestProfileFeature(BaseTest):

    @allure.title("change profile name")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_name(f"Test {random.randint(1,100)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screen("Success")

    @allure.title("Click on sections Most")
    @allure.severity("Critical")
    def test_click_on_sections(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_buzz()
        self.buzz_page.is_opened()
        self.buzz_page.click_most()

    @allure.title("Post random information")
    @allure.severity("Critical")
    def test_post(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_buzz()
        self.buzz_page.is_opened()
        self.buzz_page.click_post_area(f"Test text {random.randint(1, 100)}")
        self.buzz_page.click_post_btn()
        self.personal_page.make_screen("Post success")

    @allure.title("Search assistant")
    @allure.severity("Critical")
    def test_search_assistant(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_directory()
        self.directory_page.is_opened()
        self.directory_page.add_field_employee(f"Test text {random.randint(1, 100)}")
        self.directory_page.choose_params_employee()
        self.directory_page.click_search_btn()
        self.personal_page.make_screen("Search success")



