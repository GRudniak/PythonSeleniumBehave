from selenium import webdriver

class Browser(object):

    driver = webdriver.Chrome('/home/grru/Documents/testAutomation/features/chromedriver')
    # driver = webdriver.Chrome() if you have set chromedriver in your PATH
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()

    def get(context, address):
    	context.driver.get(address)