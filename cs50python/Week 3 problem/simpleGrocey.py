#https://www.programiz.com/python-programming/methods/list/index

def main():
    #prompt a user for the items untin user ctrl-d
    #sort the list
    
    #for loop a new list with amounts already asigned
    items = getItems()
    items.sort()
    asignedItems = asignItems(items)
    for x in asignedItems:
        print(x)
    
def getItems():
    items = list()
    while True:
        try:
            item = input().upper()
            items.append(item)
        except EOFError:
            return items

def asignItems(items):
    asignedItems = list()
    for item in items:
        count = items.count(item)
        asignedItems.append(f"{count} {item}")
        if asignedItems.count(f"{count} {item}") >= 2:
            del asignedItems[asignedItems.index(f"{count} {item}")]
    return asignedItems

main()