def main():
    #prompt a user for the items untin user ctrl-d
    #i need to asign an amount value to each str of items   
    #for loop the list of str by and turn it into a dict with values of amount of each key
    #if multiple keys exist add their values
    #sort the keys alpha
    
    items = getItems()
    items.sort()
    print(items)
    
def getItems():
    items = list()
    while True:
        try:
            item = input().upper()
            items.append(item)
        except EOFError:
            return items


main()