import os
import time
import json
import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env")

# ChromeDriver setup
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Platforms for auto-registration
PLATFORMS = {
    "Binance": "https://www.binance.com/en/register",
    "Coinbase": "https://www.coinbase.com/signup",
    "Kraken": "https://www.kraken.com/sign-up",
    "Bet365": "https://www.bet365.com/register",
    "Etsy": "https://www.etsy.com/join",
    "Fiverr": "https://www.fiverr.com/join"
}

def auto_register(platform, url):
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 15)  # Wait for page load

        email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"], input[name="email"], input[placeholder*="email"]')))
        email_field.send_keys("your-email@example.com")
        
        password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"], input[name="password"], input[placeholder*="password"]')))
        password_field.send_keys("YourSecurePassword123")
        
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"], button[name="register"], input[type="submit"]')))
        submit_button.click()

        print(f"✅ Successfully registered on {platform}!")
    except Exception as e:
        print(f"❌ {platform} registration failed: {e}")
    finally:
        time.sleep(3)

def simulate_income():
    income_sources = {
        "Freelancing": random.uniform(300, 800),
        "Betting": random.uniform(200, 900),
        "Digital Sales": random.uniform(100, 600),
        "Trading": random.uniform(400, 1000),
        "Affiliate Marketing": random.uniform(250, 750)
    }
    return income_sources

def main():
    print("🚀 Starting Automated Account & API Setup...")
    registered_accounts = [auto_register(p, u) for p, u in PLATFORMS.items()]
    
    balance = 10000.0  # Starting balance
    while True:
        income = simulate_income()
        total_earned = sum(income.values())
        balance += total_earned
        print(f"💰 Income Earned: £{total_earned:.2f}, New Balance: £{balance:.2f}")

        # Withdrawal logic
        withdraw_amount = max(balance * 0.10, 50000) if balance > 500000 else balance * 0.10
        if withdraw_amount > 0 and balance - withdraw_amount >= 10000:
            balance -= withdraw_amount
            print(f"💸 Withdrawn: £{withdraw_amount:.2f}, New Balance: £{balance:.2f}")

        time.sleep(5)  # Run every 5 seconds

if __name__ == "__main__":
    main()
    driver.quit()
