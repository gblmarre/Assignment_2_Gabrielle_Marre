
import sys
import requests

# Check command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Get Bitcoin price
try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin",
        headers={"Authorization": "Bearer b741241d5f9777b6487b8f17b6a8b53c9a9e646b1cc0b449457d2344184caff4"}
    )
    response.raise_for_status()
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit()

# Calculate total
total = n * price
print(f"${total:,.4f}")

