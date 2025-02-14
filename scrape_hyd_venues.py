from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

# Initialize Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the website
url = "https://www.weddingwire.in/wedding-venues/hyderabad"
driver.get(url)
time.sleep(5)  # Wait for page to load

venues = []

# Find venue details
venue_cards = driver.find_elements(By.CLASS_NAME, "vendorTile")

for card in venue_cards:
    try:
        name = card.find_element(By.CLASS_NAME, "vendorTile__title").text
    except:
        name = "N/A"

    try:
        location = card.find_element(By.CLASS_NAME, "vendorTile__location").text
    except:
        location = "N/A"

    try:
        price = card.find_element(By.CLASS_NAME, "vendorTile__price").text
    except:
        price = "N/A"

    venues.append({"Name": name, "Location": location, "Price": price})

# Save data to CSV
df = pd.DataFrame(venues)
df.to_csv("venues.csv", index=False)

print("✅ Scraping complete. Data saved in venues.csv")

# Close browser
driver.quit()
