import os
import time
import random
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Monzo API Credentials
MONZO_ACCESS_TOKEN = os.getenv("MONZO_ACCESS_TOKEN")
MONZO_ACCOUNT_ID = os.getenv("MONZO_ACCOUNT_ID")
MONZO_POT_ID = os.getenv("MONZO_POT_ID")  # If using a Monzo pot


def monzo_withdraw(amount):
    """Withdraw funds by transferring them to a Monzo account."""
    url = f"https://api.monzo.com/pots/{MONZO_POT_ID}/withdraw"

    headers = {
        "Authorization": f"Bearer {MONZO_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "source_account_id": MONZO_ACCOUNT_ID,
        "amount": int(amount * 100),  # Convert to pence
        "dedupe_id": f"withdraw-{int(amount)}-{int(time.time())}"
    }

    response = requests.put(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print(f"💸 Successfully withdrew £{amount:.2f} to Monzo!")
    else:
        print(f"❌ Monzo withdrawal failed: {response.json()}")


# Simulating income generation from multiple streams
def generate_income():
    sources = {
        "Freelancing": (500, 1000),
        "Betting": (200, 800),
        "Digital Sales": (300, 900),
        "Trading": (400, 1000),
        "Affiliate Marketing": (250, 700)
    }
    
    balance = 10000  # Initial balance
    while True:
        for source, (low, high) in sources.items():
            earnings = round(random.uniform(low, high), 2)
            balance += earnings
            print(f"💰 {source} Earned: £{earnings:.2f}, New Balance: £{balance:.2f}")
            
            # Withdraw excess funds over £10,000
            if balance > 10500:
                withdraw_amount = balance - 10000  # Withdraw the excess
                monzo_withdraw(withdraw_amount)
                balance -= withdraw_amount

        time.sleep(5)  # Runs every 5 seconds


if __name__ == "__main__":
    print("🚀 Starting Automated Income System with Monzo Integration...")
    generate_income()
