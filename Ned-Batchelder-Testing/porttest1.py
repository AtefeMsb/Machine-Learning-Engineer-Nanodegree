# porttest1.py
from portfolio1 import Portfolio

p = Portfolio()
print("Empty portfolio cost: ", p.cost())

p.buy("IBM", 100, 176.48)
print("With 100 IBM @ 176.48: ",  p.cost())

p.buy("HPQ", 100, 36.15)
print("With 100 HPQ @ 36.15: ", p.cost())

print(p.stocks)