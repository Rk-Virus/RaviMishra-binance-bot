from binance.client import Client
import time
from dotenv import load_dotenv
import os
from tabulate import tabulate
from datetime import datetime

load_dotenv()

# Use your own API keys
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

client = Client(API_KEY, API_SECRET, testnet=True)

# Functions for placing orders
def place_buy_order(symbol, quantity):
    try:
        order = client.order_market_buy(
            symbol=symbol,
            quantity=quantity
        )
        print("Buy order done:", order)
    except Exception as e:
        print("Error placing buy order:", e)

def place_sell_order(symbol, quantity):
    try:
        order = client.order_market_sell(
            symbol=symbol,
            quantity=quantity
        )
        print("Sell done:", order)
    except Exception as e:
        print("Error placing sell order:", e)

# Function to get current price
def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

# get account balances
def get_account_balances(symbol):
    symbol = symbol.replace("USDT", "")  # Assumes USDT pairs
    account_data = client.get_account()
    balances = account_data['balances']
    table = []
    for balance in balances:
        if balance['asset'] == symbol:
            free = float(balance['free'])
            locked = float(balance['locked'])
            total = free + locked
            table.append([symbol, free, locked, total])
            break
    return tabulate(table, headers=["Asset", "Free", "Locked", "Total"], tablefmt="pretty") if table else f"No balance found for {symbol}"

# Trading loop function
def startTradingLoop(symbol, buy_price_threshold, sell_price_threshold, trade_quantity, delay=5):
    #error handling for invalid thresholds
    if buy_price_threshold >= sell_price_threshold:
        print("Buy price threshold must be less than sell price threshold.")
        return
    position = False # Used to apply single buy sell strategy
    while True:
        print("\nCurrent position : ", position)
        print(f"Buy Price Threshold: {buy_price_threshold} | Sell Price Threshold: {sell_price_threshold}")

        current_price = get_current_price(symbol)
        print(f"\nCurrent price of {symbol}: {current_price}")

        if not position and current_price <= buy_price_threshold:
            print(f"\nPrice is below {buy_price_threshold}, placing buy order.")
            place_buy_order(symbol, trade_quantity)
            position = True
        elif position and current_price >= sell_price_threshold:
            print(f"\nPrice is above {sell_price_threshold}, placing sell order.")
            place_sell_order(symbol, trade_quantity)
            position = False
        else:
            print("\nNo trading action taken.")

        time.sleep(delay)  # Wait for t seconds before checking again
        os.system('clear')  # Clear the console output


if __name__ == "__main__":
    print("\n*Welcome to the Trading Bot!* \n")

    symbol = "BTCUSDT"
    trade_quantity = 0.001

    try:
        print(f"Current BTCUSDT Price: {get_current_price(symbol)}")
        buy_price_threshold = float(input("Enter your buy price threshold: "))
        sell_price_threshold = float(input("Enter your sell price threshold: "))
        startTradingLoop(symbol, buy_price_threshold, sell_price_threshold, trade_quantity)

    except ValueError:
        print("Invalid input. Please enter decimal USD values.")

    except KeyboardInterrupt:
        print("Trading loop stopped by user. Check trade_logs.txt for details.")
        with open("trade_logs.txt", "a") as f:
            f.write(f"Trading session ended at {datetime.now()}\n")
            f.write(get_account_balances(symbol) + "\n")

    except Exception as e:
        print(f"Unexpected error: {e}")
        with open("trade_logs.txt", "a") as f:
            f.write(f"Error at {datetime.now()}: {e}\n")
            f.write(get_account_balances(symbol) + "\n")

    finally:
        print("Thank you for using the trading bot.")


## the code is a basic setup and can be improved definitely.