goods = [(60, 10),(100, 20),(120, 30)]

def fractional_backpack(goods, w): # goods：商品信息列表，以元组的形式存储商品的价格和重量
    goods.sort(key = lambda x: x[0]/x[1], reversed = True) # 以价值/重量的比值进行降序排列
    