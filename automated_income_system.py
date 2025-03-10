import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONZO_ACCESS_TOKEN = os.getenv("MONZO_ACCESS_TOKEN")
MONZO_ACCOUNT_ID = os.getenv("MONZO_ACCOUNT_ID")
MONZO_POT_ID = os.getenv("MONZO_POT_ID", None)  # Optional

# Simulated balance tracking
balance_data = {"balance": 10000.00, "profit": 0.00}


def get_monzo_balance():
    """Fetch current Monzo balance."""
    url = f"https://api.monzo.com/balance?account_id={MONZO_ACCOUNT_ID}"
    headers = {"Authorization": f"Bearer {MONZO_ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("balance", 0) / 100  # Convert from pence to pounds
    print("❌ Error fetching Monzo balance:", response.json())
    return None


def withdraw_to_monzo(amount):
    """Withdraw funds from the system to Monzo."""
    headers = {"Authorization": f"Bearer {MONZO_ACCESS_TOKEN}"}

    # Convert amount to pence
    amount_pence = int(amount * 100)

    # If using a Monzo Pot, transfer funds from the pot
    if MONZO_POT_ID:
        url = f"https://api.monzo.com/pots/{MONZO_POT_ID}/withdraw"
        data = {
            "source_account_id": MONZO_ACCOUNT_ID,
            "amount": amount_pence,
            "dedupe_id": f"withdraw-{int(time.time())}"
        }
    else:
        # Transfer directly to the Monzo account
        url = "https://api.monzo.com/transactions"
        data = {
            "account_id": MONZO_ACCOUNT_ID,
            "amount": -amount_pence,  # Negative amount for withdrawal
            "description": "Automated Income Withdrawal"
        }

    print(f"🔄 Debug: Sending Withdrawal Request - {data}")  # Debugging statement

    response = requests.post(url, headers=headers, json=data)

    if response.status_code in [200, 201]:
        print(f"💸 Withdrawn: £{amount:.2f}, New Balance: £{balance_data['balance']:.2f}")
        balance_data["balance"] -= amount
        balance_data["profit"] = 0  # Reset profit after withdrawal
    else:
        print(f"❌ Withdrawal failed: {response.status_code} - {response.json()}")


def run_income_automation():
    """Simulates income generation and withdrawals."""
    global balance_data
    while True:
        earned = {
            "Freelancing": round(500 + (200 * time.time() % 1), 2),
            "Betting": round(300 + (200 * time.time() % 1), 2),
            "Digital Sales": round(400 + (250 * time.time() % 1), 2),
            "Trading": round(350 + (300 * time.time() % 1), 2),
            "Affiliate Marketing": round(250 + (150 * time.time() % 1), 2)
        }
        
        for source, amount in earned.items():
            balance_data["balance"] += amount
            balance_data["profit"] += amount
            print(f"💰 {source} Earned: £{amount:.2f}, New Balance: £{balance_data['balance']:.2f}")
        
        # Withdraw logic: only if balance exceeds £10,500
        if balance_data["balance"] > 10500:
            withdraw_amount = balance_data["profit"] * 0.10  # Withdraw 10% of profit
            if balance_data["balance"] > 500000:
                withdraw_amount = 50000  # Fixed £50K withdrawals beyond £500K
            if withdraw_amount > 0 and balance_data["balance"] - withdraw_amount >= 10000:
                withdraw_to_monzo(withdraw_amount)
        
        time.sleep(5)  # Run every 5 seconds


if __name__ == "__main__":
    print("🚀 Starting Automated Income System...")
    run_income_automation()
