menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    priceCal()
    
def priceCal():
    rememberPrice = 0
    while True:
        try:
            price = menuPrice()
            total = rememberPrice ++ price
            rememberPrice = total
            print(f"Total: ${total:.2f}")
        except EOFError:
            break


def menuPrice():
    while True:
        try:
            x = menu[input("Item: ").lower().title()]
            price = float(x)
            return price
        except KeyError:
            continue
        
main()