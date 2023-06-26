from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib3.util import wait


class Action:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def click_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        self.wait.until(EC.element_to_be_clickable((locator_name, locator_value))).click()

    def type_into_element(self, locator_name, locator_value, text):
        element = self.get_element(locator_name, locator_value)
        element = wait.until(EC.presence_of_element_located((locator_name, locator_value)))
        element.send_keys(text)

    def get_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return self.wait.until(EC.visibility_of_element_located((locator_name, locator_value))).text

    def wait_for_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        self.wait.until(EC.visibility_of_element_located((locator_name, locator_value)))


    def wait_for_element_to_disappear(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        self.wait.until(EC.invisibility_of_element_located((locator_name, locator_value)))

    def get_page_title(self):
        return self.driver.title

    def navigate_to_url(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def switch_to_frame(self, frame_locator):
        frame = self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
        self.driver.switch_to.default_content()
        return frame

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def take_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)

    def close_browser(self):
        self.driver.quit()

    def get_element_attribute(self, locator_name, locator_value, attribute):
        element = self.get_element(locator_name, locator_value)
        return self.wait.until(EC.visibility_of_element_located((locator_name, locator_value))).get_attribute(attribute)

    def is_element_visible(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        try:
            return self.wait.until(EC.visibility_of_element_located((locator_name, locator_value))).is_displayed()
        except:
            return False

    def is_element_enabled(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        try:
            return self.wait.until(EC.visibility_of_element_located((locator_name, locator_value))).is_enabled()
        except:
            return False

    def is_element_selected(self, locator):
        element = self.get_element(locator)
        try:
            return element.wait.until(EC.visibility_of_element_located(locator)).is_selected()
        except:
            return False

    def get_element_count(self, locator):
        element = self.get_element(locator)
        return len(element.wait.until(EC.presence_of_all_elements_located(locator)))

    def switch_to_alert(self):
        return self.wait.until(EC.alert_is_present())

    def accept_alert(self):
        self.switch_to_alert().accept()

    def dismiss_alert(self):
        self.switch_to_alert().dismiss()

    def get_alert_text(self):
        return self.switch_to_alert().text

    def select_option_by_value(self, locator, value):
        element = self.get_element(locator)
        element.wait.until(EC.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_value(value)

    def select_option_by_index(self, locator, index):
        element = self.get_element(locator)
        element.wait.until(EC.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_index(index)

    def select_option_by_visible_text(self, locator, visible_text):
        element = self.get_element(locator)
        element.wait.until(EC.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_visible_text(visible_text)

    def get_selected_option(self, locator):
        element = self.get_element(locator)
        element.wait.until(EC.visibility_of_element_located(locator))
        select = Select(element)
        selected_option = select.first_selected_option
        return selected_option.text

    def get_all_options(self, locator):
        element = self.get_element(locator)
        return element.find_elements(By.TAG_NAME, 'option')

    def hover_over_element(self, locator):
        element = self.get_element(locator)
        self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click_element(self, locator):
        element = self.get_element(locator)
        self.wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).double_click(element).perform()

    def right_click_element(self, locator):
        element = self.get_element(locator)
        self.wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).context_click(element).perform()

    def press_key(self, locator, key):
        element = self.get_element(locator)
        self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(key)

    def press_enter_key(self, locator):
        element = self.get_element(locator)
        self.press_key(locator, Keys.ENTER)

    def press_tab_key(self, locator):
        element = self.get_element(locator)
        self.press_key(locator, Keys.TAB)

    def get_element_css_property(self, locator, property_name):
        element = self.get_element(locator)
        self.wait.until(EC.visibility_of_element_located(locator))
        return element.value_of_css_property(property_name)

    def execute_script(self, script):
        self.driver.execute_script(script)

    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    def get_current_url(self):
        return self.driver.current_url

    def get_window_handle(self):
        return self.driver

    def get_all_window_handles(self):
        return self.driver.window_handles

    def switch_to_next_window(self):
        handles = self.get_all_window_handles()
        current_handle = self.driver.current_window_handle
        index = handles.index(current_handle)
        next_index = (index + 1) % len(handles)
        self.driver.switch_to.window(handles[next_index])

    def switch_to_previous_window(self):
        handles = self.get_all_window_handles()
        current_handle = self.driver.current_window_handle
        index = handles.index(current_handle)
        prev_index = (index - 1) % len(handles)
        self.driver.switch_to.window(handles[prev_index])

    def wait_for_element_text(self, locator, text):
        element = self.get_element(*locator)
        self.wait.until(EC.text_to_be_present_in_element_value(locator, text))

    def wait_for_element_attribute_value(self, locator, attribute, value):
        self.wait.until(EC.attribute_to_be_value(locator, attribute, value))

    def switch_to_new_window(self):
        main_window = self.driver.current_window_handle
        new_window = None
        for handle in self.driver.window_handles:
            if handle != main_window:
                new_window = handle
                break
        if new_window:
            self.driver.switch_to.window(new_window)

    def switch_to_main_window(self):
        main_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(main_window)

    def switch_to_frame_by_index(self, index):
        self.driver.switch_to.frame(index)

    def switch_to_frame_by_locator(self, locator):
        frame = self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
        self.driver.switch_to.default_content()
        return frame

    def execute_async_script(self, script, timeout=10):
        return self.driver.execute_async_script(script, timeout)

    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.wait.until(EC.visibility_of_element_located(source_locator))
        target_element = self.wait.until(EC.visibility_of_element_located(target_locator))
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def drag_and_drop_by_offset(self, locator, x_offset, y_offset):
        element = self.get_element(locator)
        self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).drag_and_drop_by_offset(element, x_offset, y_offset).perform()

    def get_current_window_size(self):
        return self.driver.get_window_size()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def maximize_window(self):
        self.driver.maximize_window()

    def minimize_window(self):
        self.driver.minimize_window()

    def scroll_to_element_center(self, locator):
        element = self.get_element(locator)
        self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)