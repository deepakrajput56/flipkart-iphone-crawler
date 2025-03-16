import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
from behave import given, when, then

# Load configuration

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

FLIPKART_URL = config["flipkart"]["url"]
SEARCH_ITEM = config["flipkart"]["search_item"]
OUTPUT_FILE = config["flipkart"]["output_file"]

@given("I open the Flipkart website")
def step_open_flipkart(context):

    try:
        context.driver.get(FLIPKART_URL)
        context.driver.maximize_window()
        sleep(2)


        try:
            close_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'X')]")
            close_button.click()
        except NoSuchElementException:
            pass  # Popup not present

    except Exception as e:
        print(f"Error opening Flipkart: {e}")
        context.driver.quit()

@when('I search for "{item}"')
def step_search_item(context, item):
    """ Search for the given item (iPhone) """
    try:
        search_box = context.driver.find_element(By.NAME, "q")
        search_box.send_keys(item)
        search_box.send_keys(Keys.RETURN)
        sleep(3)
    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error during search: {e}")
        context.driver.quit()

@then("I should save the iPhone list in a file and print it")
def step_save_results(context):

    try:
        iphones = context.driver.find_elements(By.XPATH, "//div[contains(@class, 'KzDlHZ')]")
        prices = context.driver.find_elements(By.XPATH, "//div[contains(@class, '_4b5DiR')]")

        if not iphones or not prices:
            assert ValueError, "No iPhones found on the page."

        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            print("Debug: Printing data")  # Debugging line

            for i in range(min(len(iphones), len(prices))):
                name = iphones[i].text.strip()
                price = prices[i].text.strip()
                print(name,price)
                if not name or not price:
                    continue  # Skip empty results

                print(f"{name} - {price}")  # Print in console
                file.write(f"{name} - {price}\n")  # Save to file

    except Exception as e:
        print(f"Error fetching data: {e}")
    finally:
        context.driver.quit()


