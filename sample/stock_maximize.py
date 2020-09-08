#!/bin/python3

def stockmax(n, prices):
    nos_stock = 0
    sell_amt = 0
    buy_amt = 0
    zip_list = zip(prices, prices[1:], prices[2:])

    if n == 0 or n == 1:
        return 0
    elif n == 2:
        if prices[1] > prices[2]:
            return 0
        elif prices[1] == prices[2]:
            return 0
        else:
            return prices[2]-prices[1]
    else:
        for i, j, k in zip_list:
            #print("stioc list", i, j, k)
            if (i < j and i < k) or (i < j and i == k) or (i > j and i == k) or (i < j and i > k):
                #print("Have to see me!!")
                buy_amt = buy_amt + i
                nos_stock = nos_stock+1
            elif (i > j and i > k) or (i < j and i == k) or (i == j and i < k) or (i == j and i > k) or (i > j and i < k) or (i == j and i == k):
                if nos_stock == 0:
                    #print("oh! no stock")
                    continue
                else:
                    sell_amt = sell_amt + (nos_stock*i)
                    nos_stock = 0
                    #print("sell_amt: ", sell_amt)

            #print("nos_stock: ", nos_stock, "bought: ",
                #   buy_amt, "sell:", sell_amt)

        #print("--------------------------")
        if prices[-2] < prices[-1]:
            buy_amt = buy_amt + prices[-2]
            nos_stock = nos_stock+1
            sell_amt = sell_amt + (nos_stock*prices[-1])
            nos_stock = 0
            #print("nos_stock: ", nos_stock, "bought: ",
                #   buy_amt, "sell:", sell_amt)
            return sell_amt - buy_amt

        if (prices[-2] > prices[-1]) or (prices[-2] == prices[-1]):
            if nos_stock == 0:
                return sell_amt - buy_amt
            else:
                sell_amt = sell_amt + (nos_stock*prices[-1])
                nos_stock = 0
                # print("nos_stock: ", nos_stock, "bought: ",
                #   buy_amt, "sell:", sell_amt)
                return sell_amt - buy_amt


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        prices = list(map(int, input().rstrip().split()))
        result = stockmax(n, prices)
        print("Total Profit---->", result)
