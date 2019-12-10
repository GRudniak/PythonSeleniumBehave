from selenium.webdriver.common.by import By
from browser import Browser

class LoginPageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/h2')
    LOGIN = (By.XPATH, '//*[@id="signin-username"]')
    PASSWORD = (By.XPATH, '//*[@id="signin-password"]')
    SIGNIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div/div[3]/button')


class LoginPage(Browser):
    # Home Page Actions

   def login_to_app(self):
      self.driver.find_element(*LoginPageLocator.LOGIN).send_keys('grzegorz.rudniak@mobica.com')
      self.driver.find_element(*LoginPageLocator.PASSWORD).send_keys('Qwerty07')
      self.driver.find_element(*LoginPageLocator.SIGNIN_BUTTON).click()

   def get_element(self):
      return self.driver.find_element(*LoginPageLocator.HEADER_TEXT)