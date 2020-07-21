price = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

print('key:%s value:%s' % (price.keys(), price.values()))
price2 = {key: value for key, value in price.items() if value > 100}
print(price2)

L = [1, 2, 3, 4, 5]
print(len(L))

for i in range(len(L)):
    print(L[i])
    pass
