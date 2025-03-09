import os
import time
import random
import json
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load environment variables
load_dotenv()

# Platforms for automated setup
PLATFORMS = {
    "Binance": "https://www.binance.com/en/register",
    "Coinbase": "https://www.coinbase.com/signup",
    "Kraken": "https://www.kraken.com/sign-up",
    "Bet365": "https://www.bet365.com/register",
    "Etsy": "https://www.etsy.com/join",
    "Fiverr": "https://www.fiverr.com/join"
}

def auto_register(platform, url):
    """Automates account registration."""
    print(f"🔄 Registering for {platform}...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)
    
    try:
        email = f"user{random.randint(1000, 9999)}@example.com"
        password = "SecurePass123!"
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(5)
        print(f"✅ {platform} account created: {email}")
        return {"platform": platform, "email": email, "password": password}
    except Exception as e:
        print(f"❌ {platform} registration failed: {e}")
        return None
    finally:
        driver.quit()

def auto_generate_income():
    """Simulates automated income generation from various sources."""
    balance = 10000
    while True:
        method = random.choice(["Betting", "Trading", "Affiliate Marketing", "Digital Sales", "Freelancing"])
        profit = round(random.uniform(50, 1000), 2)
        balance += profit
        print(f"💰 {method} Earned: £{profit}, New Balance: £{balance}")
        time.sleep(5)

def auto_withdraw(balance):
    """Withdraws funds dynamically based on balance."""
    if balance > 50000:
        withdraw_amount = min(5000, balance * 0.1)
        balance -= withdraw_amount
        print(f"💸 Withdrawn: £{withdraw_amount:.2f}, New Balance: £{balance:.2f}")
    return balance

if __name__ == "__main__":
    print("🚀 Starting Automated Account & API Setup...")
    registered_accounts = [auto_register(p, u) for p, u in PLATFORMS.items()]
    
    # Start automated income generation
    print("🔄 Running Income Automation...")
    auto_generate_income()

