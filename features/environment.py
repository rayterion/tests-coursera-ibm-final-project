from src.service.web_driver import host_app, shutdown_app
from selenium import webdriver

def before_all(context):
    host_app(3000)
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    context.browser = webdriver.Chrome(options=options)
    context.url = "http://localhost:3000"

def after_all(context):
    shutdown_app()
    context.browser.quit()