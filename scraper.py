from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

def read_priority_keywords(file_path):
    with open(file_path, 'r') as file:
        keywords = [line.strip() for line in file.readlines()]
    return keywords

def scrape_cs_scripts(progress_bar, url='https://assetstore.unity.com/packages/tools/audio/simple-music-maker-240781#content', driver_path='/usr/local/bin/geckodriver', priority_keywords_file='priority_keywords.txt'):
    # Set up the Firefox options to run in headless mode (without GUI)
    options = Options()
    options.add_argument("--headless")

    # Initialize the Firefox WebDriver with the specified options
    service = Service(driver_path)
    driver = webdriver.Firefox(service=service, options=options)

    try:
        # Read priority keywords from the specified file
        priority_keywords = read_priority_keywords(priority_keywords_file)

        # Open the webpage
        driver.get(url)

        # Wait for the page to load fully
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_2_W2p')))
        progress_bar.update(10)  # Update the progress bar after loading the page

        # Handle the overlay, e.g., cookie consent popup
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()
        except Exception:
            print("No overlay to handle or failed to close overlay.")
        progress_bar.update(10)  # Update the progress bar after handling overlay

        # Function to recursively click all expandable elements
        def click_expandable_elements():
            while True:
                expandable_elements = driver.find_elements(By.CLASS_NAME, '_2_W2p')
                found_new_elements = False

                for element in expandable_elements:
                    try:
                        driver.execute_script("arguments[0].scrollIntoView(true);", element)
                        if "arrow-down" in element.get_attribute('outerHTML'):
                            driver.execute_script("arguments[0].click();", element)
                            found_new_elements = True
                            WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_2_W2p')))
                    except (StaleElementReferenceException, NoSuchElementException):
                        continue

                if not found_new_elements:
                    break

        # Recursively click expandable elements
        click_expandable_elements()
        progress_bar.update(30)  # Update after expanding elements

        # After all elements have been expanded, collect all texts from elements with class "_1PwS0"
        visible_elements = driver.find_elements(By.CLASS_NAME, '_1PwS0')

        # Collect only texts ending with ".cs"
        cs_files = [element.text for element in visible_elements if element.text.endswith('.cs')]

        # Filter the collected C# script file names based on the priority keywords
        filtered_cs_files = [script for script in cs_files if any(keyword in script for keyword in priority_keywords)]

        progress_bar.update(20)  # Update the progress bar after filtering scripts

        return filtered_cs_files

    finally:
        driver.quit()
