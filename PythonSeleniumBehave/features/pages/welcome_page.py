from selenium.webdriver.common.by import By
from browser import Browser

class WelcomePageLocator(object):
    # Home Page Locators

    SIGNIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/a/span[1]')


class WelcomePage(Browser):
    # Home Page Actions

   def get_element(self):
   		return self.driver.find_element(*WelcomePageLocator.SIGNIN_BUTTON)

   def click_element(self):
   		self.driver.find_element(*WelcomePageLocator.SIGNIN_BUTTON).click()
