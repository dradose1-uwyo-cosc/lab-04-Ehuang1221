item_list = ["milk", "bread", "beef", "apples", "pizza"]
prices = [2.89, 3.12, 10.32, 3.50, 7.99]

for item in range(len(item_list)):
    print(f" I bought {item_list[item]} for ${prices[item]}")

items_total = 0

for price in prices:
    items_total = price + items_total
print(f"I paid total ${items_total}")

Maxprice = max(prices)
index_remove = prices.index(Maxprice)
del item[index_remove]
del prices[index_remove]
print(items)
print(prices)