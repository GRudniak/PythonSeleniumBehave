@step('I start the app')
def step_impl(context):
    context.browser.get("http://0.0.0.0:3000/")