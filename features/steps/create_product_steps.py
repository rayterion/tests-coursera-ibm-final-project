from behave import when, given, then
import requests


@when("the user types in the name: {name}")
def step_impl(context, name):
    full_url = context.url + f"/"
    context.browser.get(full_url)
    context.log_element = context.browser.find_element("tag name", "ul")
    context.current_name = name

@then("the product listed appears on the screen")
def step_impl(context):
    items = context.log_element.find_element("tag name", "li")
    assert any(context.current_name in item.text for item in items)
