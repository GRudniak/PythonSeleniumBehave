from selenium.webdriver.common.by import By
import time


@step('I navigate to Datasets page')
def step_impl(context):
   context.left_menu_page.click_menu_datasets_btn()

@step('I navigate to Videos page 0 and check load time')
def step_impl(context):
    context.left_menu_page.click_menu_videos_btn()
    start = time.time()
    context.videos_page.get_video_tail()
    end = time.time() - start
    print('Videos page 0 load time {}'.format(end))
    with open("performance.txt", "a") as myfile:
        myfile.write('\nVideos page 0 load time {}'.format(end))

@step('I navigate to Videos page "{page_number}"')
def step_impl(context, page_number):
    context.videos_page.navigate_to_page(page_number)

@step('I navigate to Videos page 4 and check load time')
def step_impl(context):
    context.videos_page.navigate_to_page_4()
    start = time.time()
    context.videos_page.get_video_tail_page_4()
    end = time.time() - start
    print('Videos page 4 load time {}'.format(end))
    with open("performance.txt", "a") as myfile:
    	myfile.write('\nVideos page 4 load time {}'.format(end))


@step('I navigate to Datasets page 0 and check load time')
def step_impl(context):
    context.left_menu_page.click_menu_datasets_btn()
    start = time.time()
    context.datasets_page.get_dataset_tail()
    end = time.time() - start
    print('Dataset page 0 load time {}'.format(end))
    with open("performance.txt", "a") as myfile:
        myfile.write('\nDatasets page 0 load time {}'.format(end))