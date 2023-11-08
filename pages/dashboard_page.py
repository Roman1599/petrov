from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure

class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    MY_INFO_BUTTON = ("xpath","//span[text()='My Info']")
    BUZZ_BUTTON = ("xpath", "//span[text()='Buzz']")
    DIRECTORY_BUTTON = ("xpath", "//span[text()='Directory']")
    PIM_BUTTON = ("xpath", "//span[text()='PIM']")

    @allure.step("Click on 'My info' link" )
    def click_my_info(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()

    @allure.step("Click on 'Buzz' link")
    def click_buzz(self):
        self.wait.until(EC.element_to_be_clickable(self.BUZZ_BUTTON)).click()

    @allure.step("Click on 'Directory' link")
    def click_directory(self):
        self.wait.until(EC.element_to_be_clickable(self.DIRECTORY_BUTTON)).click()

    @allure.step("Click on 'Pim' link")
    def click_pim(self):
        self.wait.until(EC.element_to_be_clickable(self.PIM_BUTTON)).click()