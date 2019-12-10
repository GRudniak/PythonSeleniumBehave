from selenium.webdriver.common.by import By
from browser import Browser

class VideosPageLocator(object):
    # Home Page Locators

    VIDEOS = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/h4')
    VIDEO_TILE = (By.ID, 'DWPy2xRrjrzmgyr2i')
    VIDEO_TILE_PAGE_4 = (By.ID, 'gLLRpAysR77hCM6bP')
    VIDEOS_PAGE_4_PAGINATION = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[4]/div/ul/li[5]/button')


class VideosPage(Browser):
    # Home Page Actions

   def get_element(self):
   		return self.driver.find_element(*VideosPageLocator.VIDEOS)

   def get_video_tail(self):
   		self.driver.find_element(*VideosPageLocator.VIDEO_TILE)

   def get_video_tail_page_4(self):
   		self.driver.find_element(*VideosPageLocator.VIDEO_TILE_PAGE_4)

   def navigate_to_page(self, page_number):
   		self.driver.get('http://0.0.0.0:3000/videos?page=' + page_number + '')

   def navigate_to_page_4(self):
   		self.driver.find_element(*VideosPageLocator.VIDEOS_PAGE_4_PAGINATION).click()
