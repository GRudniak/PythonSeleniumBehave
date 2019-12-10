@step('I see Welcome page')
def step_impl(context):
    signin_btn = context.welcome_page.get_element()

@step('I click Signin button')
def step_impl(context):
    signin_btn = context.welcome_page.click_element()
