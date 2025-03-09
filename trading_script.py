import random
import time

def execute_trade():
    print("🔄 Executing Trade...")
    result = random.choice(["✅ Trade Success", "❌ Trade Loss"])
    print(result)
    return result

if __name__ == "__main__":
    print("🚀 Trading script running...")
    while True:
        execute_trade()
        time.sleep(5)
