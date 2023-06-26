import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.Action import Action
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from utilities import read_configuration

class LoginPage(Action):
    def __init__(self, driver,logger):
        super().__init__(driver)
        self.logger = logger

    email_field_name = "session_key"
    password_field_xpath = "//input[@id='session_password']"
    login_button_xpath = "//button[@type='submit']"
    actual_warning_message_xpath ="//div[@id='error-for-password']"

    def login_with_valid_email_and_password(self):
        wait = WebDriverWait(self.driver,20)
        time.sleep(5)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, self.email_field_name)))
        email_field.send_keys(read_configuration.read_config("locator login", "email"))
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, self.password_field_xpath)))
        password_field.send_keys(read_configuration.read_config("locator login", "password"))
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, self.login_button_xpath)))
        login_button.click()
        time.sleep(9)

    def login_with_invalid_email_and_password(self,email,password):
        wait = WebDriverWait(self.driver, 20)
        time.sleep(10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, self.email_field_name)))
        email_field.send_keys(email)
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, self.password_field_xpath)))
        password_field.send_keys(password)
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, self.login_button_xpath)))
        login_button.click()
        time.sleep(4)
        expected_warning_message = "That’s not the right password. Forgot password?"
        actual_warning_message = wait.until(EC.presence_of_element_located((By.XPATH, self.actual_warning_message_xpath)))
        actual_warning_message_text = actual_warning_message.text
        self.logger.info(actual_warning_message_text)
        time.sleep(4)
        assert actual_warning_message_text.__eq__(expected_warning_message)
        time.sleep(5)



