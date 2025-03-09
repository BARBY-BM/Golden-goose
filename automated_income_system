import json
import time

# Load balance from file or initialize
try:
    with open("balance.json", "r") as f:
        balance_data = json.load(f)
except FileNotFoundError:
    balance_data = {"balance": 10000, "profit": 0}

def update_balance(profit):
    global balance_data
    balance_data["profit"] += profit
    balance_data["balance"] += profit
    
    # Dynamic withdrawal system
    if balance_data["balance"] < 500000:
        withdraw_amount = balance_data["profit"] * 0.10  # 10% of profit
    else:
        withdraw_amount = 50000  # Fixed £50K once past £500K
    
    if withdraw_amount > 0 and balance_data["balance"] - withdraw_amount >= 10000:
        balance_data["balance"] -= withdraw_amount
        print(f"💸 Withdrawn: £{withdraw_amount:.2f}, New Balance: £{balance_data['balance']:.2f}")
    
    # Reset profit after withdrawal
    balance_data["profit"] = 0
    
    with open("balance.json", "w") as f:
        json.dump(balance_data, f)

# Simulated trading and betting functions
def execute_trade():
    profit = 100 * (1 if time.time() % 2 == 0 else -1)  # Random profit/loss
    print(f"🔄 Executing Trade... {'✅ Trade Success' if profit > 0 else '❌ Trade Loss'}")
    update_balance(profit)

def place_bet():
    profit = 50 * (1 if time.time() % 2 == 0 else -1)
    print(f"🎲 Placing Bet... {'✅ Bet Won!' if profit > 0 else '❌ Bet Lost'}")
    update_balance(profit)

# Run automation loop
while True:
    execute_trade()
    place_bet()
    time.sleep(5)  # Runs every 5 seconds
