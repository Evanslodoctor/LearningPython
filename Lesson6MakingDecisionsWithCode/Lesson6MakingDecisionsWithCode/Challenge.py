
while True:
    purchase = float(input("Enter the amount: "))
    shippingCost = 10
    total = 0
    if purchase >= 50:
        total = float (purchase + shippingCost)
        print("Total Purchase is %f "%total)
    else:
        total = float(purchase)
        print("Total Purchase is %f "%total)
