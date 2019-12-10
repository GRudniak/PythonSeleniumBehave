from selenium.webdriver.common.by import By
from browser import Browser

class LeftMenuPageLocator(object):
    # Home Page Locators

    FLIRPROJECTS = (By.XPATH, '//*[@id="menusidebar"]/div[1]/div/div[1]/span')
    ALLVIDEOS = (By.XPATH, '//*[@id="menusidebar"]/div[2]/div/div[1]')
    ALLIMAGES = (By.XPATH, '//*[@id="menusidebar"]/div[3]/div/div[1]/span')
    RECENT = (By.XPATH, '//*[@id="menusidebar"]/div[4]/span')
    FAVORITES = (By.XPATH, '//*[@id="menusidebar"]/div[5]/span')
    ALLDATASETS = (By.XPATH, '//*[@id="menusidebar"]/div[6]/div/div[1]/span')


class LeftMenuPage(Browser):
    # Home Page Actions

   def click_menu_videos_btn(self):
   		self.driver.find_element(*LeftMenuPageLocator.ALLVIDEOS).click()

   def click_menu_datasets_btn(self):
   		self.driver.find_element(*LeftMenuPageLocator.ALLDATASETS).click()