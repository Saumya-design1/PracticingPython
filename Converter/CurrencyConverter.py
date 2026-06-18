# CurrencyConverter

amount = float(input("Enter the amount in usd to convert: "))
usd_to_inr = 94.40  # Example exchange rate from USD to INR
converted_amount = amount * usd_to_inr
print(f"The converted amount is: {converted_amount.__round__(2)} INR")