import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

CHROME_DRIVER_PATH = config["flipkart"]["chrome_driver_path"]

def before_all(context):

    try:
        service = Service(CHROME_DRIVER_PATH)
        context.driver = webdriver.Chrome(service=service)
        print("WebDriver started")
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")

def after_all(context):

    if context.driver:
        context.driver.quit()
        print("WebDriver closed")
