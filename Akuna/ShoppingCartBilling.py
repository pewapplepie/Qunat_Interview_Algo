def find_lowest_price(products: List[List[str]], discounts: List[List[str]]) -> int:
    discounts_map = dict()
    for discount in discounts:
        discounts_map[discount[0]] = discount[1:]
    sum = 0
    for product in products:
        price = int(product[0])
        discounted = price
        for tag in product[1:]:
            if tag == 'EMPTY':
                continue
            kind, value = discounts_map[tag]
            value = int(value)
            discounted = min(discounted, discount_calc(kind, value, price))
        sum += round(discounted)
    return sum

def discount_calc(Type, discount, price):
    if Type == '1':
        price *= (1 - discount*0.01)
    elif Type == '2':
        price -= discount
    elif Type == '0':
        price = discount
    return int(price)

products = [['10', 'd0', 'd1'], ['15', 'EMPTY', 'EMPTY'], ['20', 'd1', 'EMPTY']]
discounts = [['d0','1','27'], ['d1', '2', '5']]
print(findlowestprice(products, discounts))