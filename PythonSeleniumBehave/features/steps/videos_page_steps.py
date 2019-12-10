import time

@step('I see Videos page')
def step_impl(context):
    videos_page = context.videos_page.get_element()
    assert videos_page.text == 'VIDEOS'
    time.sleep( 5 )