import allure
import pytest
from Pages.loginPage import LoginPage
from utilities.Base import BaseTest
from utilities.log import generate_log
from utilities import Excel

class TestLogin(BaseTest):

   @allure.severity(allure.severity_level.CRITICAL)
   def test_login_with_valid_email_and_password(self):
       logger = generate_log()
       logger.info("Open successfully")
       login_page = LoginPage(self.driver,logger)
       login_page.login_with_valid_email_and_password()

   @pytest.mark.parametrize("email_text,password_text",Excel.get_data("utilities/ExcelFiles/TestExcel.xlsx", "TastLogin"))
   @allure.severity(allure.severity_level.CRITICAL)
   def test_login_with_invalid_email_and_password(self, email_text, password_text):
       logger = generate_log()
       logger.info("Open successfully")
       login_page = LoginPage(self.driver, logger)
       login_page.login_with_invalid_email_and_password(email_text, password_text)
