distance = int(input())
fuel_100km = float(input())
price_per_litre = float(input())
price_100km = price_per_litre * fuel_100km
price_final = (distance * price_100km)/100
print (round(price_final, 2))
