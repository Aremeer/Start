def main():
    #prompt a user for the items untin user ctrl-d
    #i need to asign an amount value to each str of items   
    #for loop the list of str by and turn it into a dict with values of amount of each key
    #if multiple keys exist add their values
    #sort the keys alpha
    
    items = getItems()
    sortedItems = asignNumberItems(items)
    print(sortedItems)
    
def getItems():
    items = list()
    while True:
        try:
            item = input().upper()
            items.append(item)
        except EOFError:
            return items


def asignNumberItems(items):
    #we make a list of dictioneries
    #dicts and keys of name and amount
    #we add new dict to the list if it doesn't exist
    #is dict exist we change the add 1 to the amount
    numberedItems = []
    for item in items:
        x = {"name":item, "amount":1}
        if
            numberedItems.append(x)





main()