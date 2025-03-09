import random
import time

def place_bet():
    print("🎲 Placing Bet...")
    result = random.choice(["✅ Bet Won!", "❌ Bet Lost"])
    print(result)
    return result

if __name__ == "__main__":
    print("🚀 Betting script running...")
    while True:
        place_bet()
        time.sleep(5)
