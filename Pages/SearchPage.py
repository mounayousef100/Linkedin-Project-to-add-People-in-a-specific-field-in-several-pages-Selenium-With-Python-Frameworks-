from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities import read_configuration
from utilities.Action import Action
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchPage(Action):
    def __init__(self, driver, logger):
        super().__init__(driver)
        self.logger = logger

    search_field_xpath = "//input[@placeholder='Search']"
    search_text = read_configuration.read_config("Search", "search")
    selected_people_xpath = "//button[@role='link'][normalize-space()='People']"
    selected_See_all_people_results_xpath = "//a[normalize-space()='See all people results']"
    add_connect_xpath = "//div[@class='entity-result__actions entity-result__divider']/div/button"
    add_connect_message_xpath = "//div[@class='entity-result__actions entity-result__divider']/div/div/button"
    send_button_xpath = "//button[@aria-label='Send now']"
    close_button_xpath = "//li-icon[@type='cancel-icon']"
    button_get_xpath = "//*[@id='ember467']"

    def search_with_valid_data(self):
        wait = WebDriverWait(self.driver, 60)
        search_field = wait.until(EC.presence_of_element_located((By.XPATH, self.search_field_xpath)))
        search_field.send_keys(self.search_text)
        search_field.send_keys(Keys.ENTER)
        time.sleep(5)
        wait.until(EC.presence_of_element_located((By.XPATH, self.selected_people_xpath))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, self.selected_See_all_people_results_xpath))).click()
        time.sleep(3)

        current_page = 2
        max_pages = 11

        while current_page <= max_pages:
            time.sleep(3)
            try:
                add_connect_buttons = wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, self.add_connect_xpath)))
            except TimeoutException:
                self.logger.info("No more add/connect buttons found. Exiting loop.")
                break

            for add_connect_button in add_connect_buttons:
                time.sleep(3)
                try:
                    if add_connect_button.text == "Follow":
                        add_connect_button.click()
                        time.sleep(2)
                    elif add_connect_button.text == "Connect":
                        add_connect_button.click()
                        time.sleep(2)
                        send_button = wait.until(EC.presence_of_element_located((By.XPATH, self.send_button_xpath)))
                        if send_button.is_enabled():
                            send_button.click()
                            time.sleep(2)
                        elif not send_button.is_enabled():
                            close_button = wait.until(EC.presence_of_element_located((By.XPATH, self.close_button_xpath)))
                            close_button.click()
                            time.sleep(2)

                    elif add_connect_button.text == "Message":
                        continue
                    else:
                        break
                except StaleElementReferenceException:
                    continue

            if current_page < max_pages:
                time.sleep(3)
                next_page = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Page " + str(current_page) + "']")))
                next_page.click()
                time.sleep(3)
                current_page += 1
