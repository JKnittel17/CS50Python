"""
Prompt:
In a file called bitcoin.py, implement a program that:
Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, 
the program should exit via sys.exit with an error message.

Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys 
is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.
"""

import sys, requests, json

def main():

    coin = get_bitcoin_to_buy()

    cost = retrieve_conversion(coin)

    print(f"${cost:,.4f}")

# Ensure user has entered # of bitcoin in command line and that it is a valid float
def get_bitcoin_to_buy():

    if len(sys.argv) != 2:

        sys.exit("Missing command-line argument or too many arguments")

    else:
         
        try: 
         
            coin = abs(float(sys.argv[1]))

        except: 

            sys.exit("Command - line argument is not a number")

    return coin
            
# Retrieve BTC converstion rate and return total cost
def retrieve_conversion(coin):
    
    try: 

        btc_info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

    except requests.RequestException:

        sys.exit("Request Exception")

    btc_price = btc_info["bpi"]["USD"]["rate_float"]

    return btc_price * coin

main()