
from forex_python.converter import CurrencyRates
from currency_converter import CurrencyConverter
import pandas as pd
#c = CurrencyRates()
c = CurrencyConverter()
# amount = int(input("Enter the amount: "))
# from_currency = input("From Currency: ").upper()
# to_currency = input("To Currency: ").upper()
# print(from_currency, " To ", to_currency, amount)
# AUD = c.convert('USD', "AUD", 1)
# EUR = c.convert('USD', "EUR", 1)
# GBP = c.convert('USD', "GBP", 1)
# JPY = c.convert('USD', "JPY", 1)
# KRW = c.convert('USD', "KRW", 1)
# TWD = c.convert('USD', "TWD", 1)
TWD = c.convert(1,'TWD', "USD")
# output = pd.DataFrame({
#     'Currency':['AUD','EUR','GBP','JPY','KRW','TWD'],
#     'Rate':[AUD,EUR,GBP,JPY,KRW,TWD]
# })
# print(output)
