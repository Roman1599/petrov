

from base.base_page import BasePage

from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
import time
from selenium.webdriver import Keys

class PimPage(BasePage):

    PAGE_URL = Links.PIM_PAGE

    ADD_EMPLOYEE = ("xpath","//*[text()='Add Employee']")
    FIRST_NAME_FIELD = ("xpath","//*[@placeholder='First Name']")
    LAST_NAME_FIELD = ("xpath", "//*[@placeholder='Last Name']")
    SAVE_BTN = ("xpath", " //*[text()=' Save ']")

    @allure.step("Click click add emloyee")
    def click_add_emloyee(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_EMPLOYEE)).click()


    @allure.step("Fill fields")
    def fill_fields(self, new_value_fir,new_value_sec):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
        first_name_field.send_keys(new_value_fir)
        self.value = new_value_fir
        second_name_field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD))
        second_name_field.send_keys(new_value_sec)
        self.value = new_value_sec

    @allure.step("Click Save button")
    def click_save_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()