from currency_converter import CurrencyConverter
amount= int (input("Amount:"))
convertnig=CurrencyConverter().convert(amount,'INR','USD')
print(convertnig)