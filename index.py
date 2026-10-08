amount = float(input("What's the amount of money? "))
usdOrEuro = str(input("Euro (E) Or USD (U) "))

def usdToEuro():
    Euro = round(amount / 1.1184, 2)
    print(f"{Euro} euro")

def euroToUsd():
    USD = round(amount * 1.1184, 2)
    print(f"{USD} usd")

def convert():
    if usdOrEuro == "E":
        euroToUsd()
    elif usdOrEuro == "U":
        usdToEuro()
    else:
        print("Please choose E or U")

convert()
