import time

@step('I see Datasets page')
def step_impl(context):
    datasets_page = context.datasets_page.get_element()
    assert datasets_page.text == 'DATASETS'
    time.sleep( 5 )