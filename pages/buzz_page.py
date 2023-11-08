from base.base_page import BasePage

from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class BuzzPage(BasePage):

    PAGE_URL = Links.BUZZ_PAGE

    RESENT_POSTS = ("xpath","//*[@class='oxd-button oxd-button--medium oxd-button--label-warn orangehrm-post-filters-button']")
    LIKED_POSTS = ("xpath","//*[text() = ' Most Liked Posts ']")
    COMMENT_POSTS = ("xpath", "//*[text() = ' Most Commented Posts ']")
    POST_AREA = ("xpath", "//*[@class='oxd-buzz-post-input']")
    POST_BTN = ("xpath", "//*[@class='oxd-button oxd-button--medium oxd-button--main']")

    @allure.step("Click on section Most")
    def click_most(self):
        self.wait.until(EC.element_to_be_clickable(self.RESENT_POSTS)).click()
        self.make_screen("Most Popular Posts")
        self.wait.until(EC.element_to_be_clickable(self.LIKED_POSTS)).click()
        self.make_screen("Most Liked Posts")
        self.wait.until(EC.element_to_be_clickable(self.COMMENT_POSTS)).click()
        self.make_screen("Most Commented Posts")

    @allure.step("Click on Post area")
    def click_post_area(self, new_value):
        post_area_field = self.wait.until(EC.element_to_be_clickable(self.POST_AREA))
        post_area_field.send_keys(new_value)
        self.value = new_value

    @allure.step("Click on Post button")
    def click_post_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.POST_BTN)).click()

