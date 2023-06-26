import allure
from Pages.SearchPage import SearchPage
from Pages.loginPage import LoginPage
from utilities.Base import BaseTest
from utilities.log import generate_log
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin(BaseTest):

   @allure.severity(allure.severity_level.CRITICAL)
   def test_login_with_valid_email_and_password(self):
       wait = WebDriverWait(self.driver,20)
       logger = generate_log()
       logger.info("Open successfully")
       login_page = LoginPage(self.driver, logger)
       login_page.login_with_valid_email_and_password()
       search_page = SearchPage(self.driver,logger)
       search_page.search_with_valid_data()

