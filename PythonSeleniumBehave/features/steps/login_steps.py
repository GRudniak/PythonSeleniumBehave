@step('I see Login page')
def step_impl(context):
    signin_text = context.login_page.get_element()
    assert signin_text.text == 'Sign In'

@step('I login to app')
def step_impl(context):
    context.login_page.login_to_app()
