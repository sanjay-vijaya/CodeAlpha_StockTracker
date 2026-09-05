# import the csv for store a data in csv file .
import csv

# create dictionary to store stock data
stock_data = {
    "APPLE": {
        'symbol': 'AAPL',
        'price': 150.00,
        'volume': 10000
    },
    "TESLA": {
        'symbol': 'TSLA',
        'price': 700.00,
        'volume': 50000
    },
    "MICROSOFT": {
        'symbol': 'MSFT',
        'price': 300.00,
        'volume': 20000
    },
    "AMAZON": {
        'symbol': 'AMZN',
        'price': 185.00,
        'volume': 15000
    }
}

# create function to get stock data


def main():
    print("-"*100)
    print("                  Welcome to Stock Tracker")
    print("-"*100)
    print("✅ Available Stocks")
    for stock_name, details in stock_data.items():
        print(
            f"Stock Name: {stock_name} | "
            f"Symbol: {details['symbol']} | "
            f"Price: ₹{details['price']:.2f} | "
            f"Volume: {details['volume']}"
        )
    print("-"*100)
# get the Stock  name from User :
    stock_name = input("Enter the Stock Name : ").upper().strip()

# check the stock name in the Stock data :
    if stock_name in stock_data:
        print(f"\"{stock_name}\" is Available ")

        print(f"Single Stock Price is :\" {stock_data[stock_name]['price']}\"")
        quantity = int(input("Enter the Quantity of Stock:"))
        print(f"✅  {quantity} shares of {stock_name} added!")
        print("-"*100)
        total_amount = stock_data[stock_name]["price"]*quantity

    else:
        print(f"\"{stock_name}\"not found in the Stock Data ❌")
        print("="*100)
        return
     # CSV section MUST be inside main()
    print("Do you wnat to save the file as CSV - Type \"Yes\"")
    save_choice = input("yes/no").lower().strip()

    if save_choice == "yes" or save_choice == "y":

        with open("portfolio.csv", mode="w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Stock Name",
                "Symbol",
                "Price",
                "Volume",
                "Quantity",
                "Total Amount"
            ])

            writer.writerow([
                stock_name,
                stock_data[stock_name]["symbol"],
                stock_data[stock_name]["price"],
                stock_data[stock_name]["volume"],
                quantity,
                total_amount
            ])

    print("-"*100)
# print the Details :
    print(
        f"\nStock Name: {stock_name}"
        f"\nStock Price: ₹{stock_data[stock_name]['price']:.2f}"
        f"\nStock Volume:{stock_data[stock_name]['volume']}"
        f"\nStock Symbol:{stock_data[stock_name]['symbol']}"
        f"\nSelect Quantity: {quantity}"
        f"\nTotal Amount: ₹{total_amount:.2f}"
    )
    if save_choice == "yes" or save_choice == "y":
        print(f"\n✅ Portfolio saved as portfolio.csv")
    else:
        print(f"\nPortfolio not saved ❌.")
    print("-"*100)
    print(f"\nThank you for using Stock Tracker!")


# call the function to execute

main()
