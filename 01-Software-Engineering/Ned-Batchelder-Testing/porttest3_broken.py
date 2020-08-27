# porttest3_broken.py
from portfolio1 import Portfolio

p = Portfolio()
print("Empty portfolio cost: {}, should be 0.0".format(p.cost()))
assert p.cost() == 0.0

p.buy("IBM", 100, 176.48)
print("With 100 IBM @ 176.48: {}, should be 17648.0".format(p.cost()))
# AssertionError will raise here.
assert p.cost() == 17600.0

p.buy("HPQ", 100, 36.15)
print("With 100 HPQ @ 36.15: {}, should be 21263.0".format(p.cost()))
assert p.cost() == 21263.0
