import sys
import requests


def main():
    try:
        bitcoin = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=6fb9ed5eb630bd46f27299db6fee5ec197d39687610b0f67a6db27cb6b1fd310"
    )
    price = float("+" + response.json()["data"]["priceUsd"])
    print("$" + "{:,}".format(round(bitcoin * price, 4)))
    # using , as a thousands separator.


main()
