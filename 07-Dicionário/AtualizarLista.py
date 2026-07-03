def produtcs():
    produtc1 = {
        "name": "coffe",
        "price": 5,
        "amount": 2
    }
    produtc2 = {
        "name": "sugar",
        "price": 2.5,
        "amount": 4
    }
    produtc3 = {
        "name": "milk",
        "price": 5,
        "amount": 2
    }
    
    lista = [produtc1, produtc2, produtc3]
    
    return lista

def produtc_update(lista):
    search = input("Enter the name you wish to updade: ")
    
    found = False
    
    for produtc in lista:
        if search == produtc["name"]:
            newpirce = int(input("Enter a new pirce: "))
            produtc["price"] = newpirce
            found = True
    
    if found == False:
        print("name not found!")

    print("="*100)
    print(f"Name: {produtc['name']}")
    print(f"Price: {produtc['price']}")
    print(f"Amount: {produtc['amount']}")
    print("="*100)
    
produto = produtcs()
produtc_update(produto)
            
            