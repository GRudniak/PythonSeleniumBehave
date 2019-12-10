from selenium import webdriver
from browser import Browser
from pages.datasets_page import DatasetsPage
from pages.videos_page import VideosPage
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage
from pages.left_menu_page import LeftMenuPage

def before_all(context):
    context.browser = Browser()
    context.datasets_page = DatasetsPage()
    context.left_menu_page = LeftMenuPage()
    context.login_page = LoginPage()
    context.welcome_page = WelcomePage()
    context.videos_page = VideosPage()

def after_all(context):
    context.browser.close()