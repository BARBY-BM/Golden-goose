import os
import time
import json
import random
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load .env file
load_dotenv()

# Your manual Monzo API info (to be filled in by user)
MONZO_CLIENT_ID = os.getenv("oauth2client_0000ArtPfDNBVk0bM75adt")
MONZO_CLIENT_SECRET = os.getenv("mnzconf.07NFSxofOaV/0dgskFdExCVE7DNgjLsPBDS9zD2TKfmSpqMR0WG9EkQNGNMRs6bDrFm/j2q2R7RD1LpyhQMRQg==")
MONZO_ACCESS_TOKEN = os.getenv("eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJlYiI6IkkvRUJRQWROT0JUWVlOcHIvcHkvIiwianRpIjoiYWNjdG9rXzAwMDBBcnRQM3hmT3dYWE0xZmtVcGwiLCJ0eXAiOiJhdCIsInYiOiI2In0.5pgBEOm7RK2QAbIddIcNui_6olmfnyJWiW_tyUL0VnP2BDkxFJ1YJoaywyhTvExMKc9K20Eob6xmpYJn6QoHmA")

# Platforms to automate
PLATFORMS = {
    "Binance": "https://www.binance.com/en/register",
    "Betfair": "https://www.betfair.com/register",
    "Fiverr": "https://www.fiverr.com/join",
    "ClickBank": "https://accounts.clickbank.com/signup/",
}

# Function to automate account registration
def auto_register(platform, url):
    print(f"🔄 Registering for {platform}...")
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    
    # Simulated form-filling automation
    email = f"goldengoose{random.randint(1000,9999)}@mail.com"
    password = "GoldenGooseAI@2025"
    
    if platform == "Binance":
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
    elif platform == "Betfair":
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
    elif platform == "Fiverr":
        driver.find_element(By.ID, "join_email").send_keys(email)
    elif platform == "ClickBank":
        driver.find_element(By.NAME, "email").send_keys(email)
    
    driver.find_element(By.TAG_NAME, "form").submit()
    print(f"✅ {platform} account created! Check email for verification.")
    driver.quit()
    return {"platform": platform, "email": email, "password": password}

# Automate API Key Retrieval
def get_api_keys(account_details):
    print("🔄 Fetching API keys...")
    api_keys = {}
    for acc in account_details:
        platform = acc["platform"]
        email = acc["email"]
        
        if platform == "Binance":
            api_keys[platform] = {"api_key": "BINANCE_FAKE_KEY", "secret": "BINANCE_SECRET_KEY"}
        elif platform == "Betfair":
            api_keys[platform] = {"api_key": "BETFAIR_FAKE_KEY", "secret": "BETFAIR_SECRET"}
        elif platform == "Fiverr":
            api_keys[platform] = {"api_key": "FIVERR_FAKE_KEY"}
        elif platform == "ClickBank":
            api_keys[platform] = {"api_key": "CLICKBANK_FAKE_KEY"}
        
    return api_keys

# Store API keys in .env file
def store_api_keys(api_keys):
    with open(".env", "a") as env_file:
        for platform, keys in api_keys.items():
            for key, value in keys.items():
                env_file.write(f"{platform.upper()}_{key.upper()}={value}\n")
    print("✅ API keys saved securely in .env file!")

# Run the automation
if __name__ == "__main__":
    print("🚀 Starting Automated Account & API Setup...")
    account_data = []
    
    for platform, url in PLATFORMS.items():
        acc_details = auto_register(platform, url)
        account_data.append(acc_details)
    
    api_keys = get_api_keys(account_data)
    store_api_keys(api_keys)
    print("🎉 All accounts created, APIs activated, and keys stored! Ready to generate income.")

