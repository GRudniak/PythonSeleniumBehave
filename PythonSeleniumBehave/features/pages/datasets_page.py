from selenium.webdriver.common.by import By
from browser import Browser

class DatasetsPageLocator(object):
    # Home Page Locators

    DATASETS = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/h4')
    DATASET_TILE = (By.ID, 'yPCFir6Tgb95wRppm')


class DatasetsPage(Browser):
    # Home Page Actions

   def get_element(self):
   		return self.driver.find_element(*DatasetsPageLocator.DATASETS)

   def get_dataset_tail(self):
   		self.driver.find_element(*DatasetsPageLocator.DATASET_TILE)
