def main():
    #prompt a user for the items untin user ctrl-d
    #i need to asign an amount value to each str of items   
    #for loop the list of str by and turn it into a dict with values of amount of each key
    #if multiple keys exist add their values
    #sort the keys alpha
    
    items = asignNumberItems(getItems())
    while True:
        #we have to prin a value of the key = "amount" then value of the key = "name" basted on the alphabetial position of the value of the key "name"
        #one way i could do it is to make a list of "name" then, sort it then print "amount", "name" based on the index of the "name" in the list.
        print()    
    
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
        dictItem = {
            "name":f"{item}",
            "amount":int(items.count(f"{item}"))}
        numberedItems.append(dictItem)
        if numberedItems.count(dictItem) > 1:
            del numberedItems[numberedItems.index(dictItem)]
    return numberedItems


main()