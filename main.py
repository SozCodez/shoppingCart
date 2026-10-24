import time
import datetime

product = ["chips", "soda", "candy", "cookies", "water", "sandwich"]
prices = ["$2.0", "$2.5", "$1.5", "$3.0", "$1.0", "$5.0"]
productIdx = ["1. ", "2. ", "3. ", "4. ", "5. ", "6. "]
cart = []
quantities = [0, 0, 0, 0, 0, 0]
cartIdx = []
cartCnt = 0
start = True
subtotal = 0
#global variables/ lists

def viewProducts():
    choice1 = True #keeps us in a menu loop, until input
    while choice1:
        print("\n \n \n \n \n")
        for i in range(len(product)):
            print(product[i], " ", prices[i])
        print()
        print()
        choice1Ret = input("Type 'close' to return: ")
        if choice1Ret == "close":
            break
# viewing products function

def addProducts():
    choice2 = True
    print("\n \n \n \n \n")
    print("Which product would you like to add?")
    print()
    for i in range(len(product)): #list products and prices
        print(productIdx[i], product[i])
    print()
    addProd = int(input("Enter product number: "))
    print()
    cartCnt = 0
    while choice2: # menu loop
        tempSubtotal = 0
        cartCnt = len(cart)
        if addProd == 1 or addProd == 2 or addProd == 3 or addProd == 4 or addProd == 5 or addProd == 6:
            cartCnt += 1 #cart count starts at 1 for display, but indexes as 0
            if addProd == 1:
                if len(cart) == 0:                          #for each product, if the cart is empty
                    print("Chips were added to cart!")
                    cart.append(". Chips")                  #product is added
                    cartIdx.append(cartCnt)
                    tempSubtotal += 2                       #subtotal increases based on price
                    quantities[0] = 1                       #quantity matching product index is set to 1
                    return tempSubtotal
                else:                                       #if the cart is not empty,
                    hasChips = 0                            #we create a special variable for each product
                    for i in range(len(cart)):              #and check each index in our cart if the item is there
                        if cart[i] == ". Chips":
                            hasChips += 1                   #if it is in our cart, it will have increased over 0
                        else:
                            hasChips += 0
                    if hasChips > 0:                        #if we already have product, shown by our special variable
                        print("Chips were added to cart!")
                        quantities[0] += 1                  #we only increase quantity for product
                        tempSubtotal += 2                   #and increase subtotal by price
                    else:                                   #if not alr in our cart, we treat same as empty cart
                        print("Chips were added to cart!")
                        cart.append(". Chips")
                        cartIdx.append(cartCnt)
                        tempSubtotal += 2
                        quantities[0] = 1
                    return tempSubtotal                     #returning the price increase of our product
            elif addProd == 2:
                if len(cart) == 0:
                    print("Soda was added to cart!")
                    cart.append(". Soda")
                    cartIdx.append(cartCnt)
                    tempSubtotal += 1
                    quantities[1] = 1
                    return tempSubtotal
                else:
                    hasSoda = 0
                    for i in range(len(cart)):
                        if cart[i] == ". Soda":
                            hasSoda += 1
                        else:
                            hasSoda += 0
                    if hasSoda > 0:
                        print("Soda was added to cart!")
                        quantities[1] += 1
                        tempSubtotal += 2.5
                    else:
                        print("Soda was added to cart!")
                        cart.append(". Soda")
                        cartIdx.append(cartCnt)
                        tempSubtotal += 2.5
                        quantities[1] = 1
                    return tempSubtotal
            elif addProd == 3:
                if len(cart) == 0:
                    print("Candy was added to cart!")
                    cart.append(". Candy")
                    cartIdx.append(cartCnt)
                    tempSubtotal += 1
                    quantities[2] = 1
                    return tempSubtotal
                else:
                    hasCandy = 0
                    for i in range(len(cart)):
                        if cart[i] == ". Candy":
                            hasCandy += 1
                        else:
                            hasCandy += 0
                    if hasCandy > 0:
                        print("Candy was added to cart!")
                        quantities[2] += 1
                        tempSubtotal += 1.5
                    else:
                        print("Candy was added to cart!")
                        cart.append(". Candy")
                        cartIdx.append(cartCnt)
                        tempSubtotal += 1.5
                        quantities[2] = 1
                    return tempSubtotal
            elif addProd == 4:
                if len(cart) == 0:
                    print("Cookies was added to cart!")
                    cart.append(". Cookies")
                    cartIdx.append(cartCnt)
                    tempSubtotal += 1
                    quantities[3] = 1
                    return tempSubtotal
                else:
                    hasCookies = 0
                    for i in range(len(cart)):
                        if cart[i] == ". Cookies":
                            hasCookies += 1
                        else:
                            hasCookies += 0
                    if hasCookies > 0:
                        print("Cookies were added to cart!")
                        quantities[3] += 1
                        tempSubtotal += 3
                    else:
                        print("Cookies were added to cart!")
                        cart.append(". Cookies")
                        cartIdx.append(cartCnt)
                        tempSubtotal += 3
                        quantities[3] = 1
                    return tempSubtotal
            elif addProd == 5:
                if len(cart) == 0:
                    print("Water was added to cart!")
                    cart.append(". Water")
                    cartIdx.append(cartCnt)
                    tempSubtotal += 1
                    quantities[4] = 1
                    return tempSubtotal
                else:
                    hasWater = 0
                    for i in range(len(cart)):
                        if cart[i] == ". Water":
                            hasWater += 1
                        elif cart[i] == ". Chips" or cart[i] == ". Soda" or cart[i] == ". Candy" or cart[i] == ". Cookies" or cart[i] == ". Sandwich":
                            hasWater += 0
                    if hasWater > 0:
                        print("Water was added to cart!")
                        quantities[4] += 1
                        tempSubtotal += 1
                    else:
                        print("Water was added to cart!")
                        cart.append(". Water")
                        cartIdx.append(cartCnt)
                        tempSubtotal += 1
                        quantities[4] = 1
                    return tempSubtotal
            elif addProd == 6:
                if len(cart) == 0:
                    print("Sandwich was added to cart!")
                    cart.append(". Sandwich")
                    cartIdx.append(cartCnt)
                    tempSubtotal += 1
                    quantities[5] = 1
                    return tempSubtotal
                else:
                    hasSand = 0
                    for i in range(len(cart)):
                        if cart[i] == ". Sandwich":
                            hasSand += 1
                        else:
                            hasSand += 0
                    if hasSand > 0:
                        print("Sandwich was added to cart!")
                        quantities[5] += 1
                        tempSubtotal += 5
                    else:
                        print("Sandwich was added to cart!")
                        cart.append(". Sandwich")
                        cartIdx.append(cartCnt)
                        tempSubtotal += 5
                        quantities[5] = 1
                    return tempSubtotal
            break
        else:
            print()
            print("Please enter valid product number")
            addProd = int(input("Enter product number: "))

def removeItem():
    choice3 = True
    print("\n\n\n\n\n")
    print("~~~~~ YOUR SHOPPING CART ~~~~~")
    print()
    if len(cart) != 0:
        for i in range(len(cart)):
            print(cartIdx[i], cart[i])
        print()
        removeProd = (input("Enter # of product you \nwould like to remove: "))
        removeProdInt = int(removeProd) #set to false instead of using else statement below
        validRemove = False
        while choice3: #menu loop
            removeProdInt = int(removeProd)
            for i in range(len(cartIdx)):                       #for each index in our cart index
                if removeProdInt == cartIdx[i]:                 #if our chosen number matches a displayed number
                    if cart[removeProdInt - 1] == ". Chips":    #we check our cart's matching index for product
                        if quantities[0] <= 1:                  #if quantity at same index is 1 or less,
                            popT = True                         #we set to pop from cart
                        else:
                            popT = False                        #if not we set to only lower quantity by 1
                        quantities[0] -= 1
                    elif cart[removeProdInt - 1] == ". Soda":
                        if quantities[1] <= 1:
                            popT = True
                        else:
                            popT = False
                        quantities[1] -= 1
                    elif cart[removeProdInt - 1] == ". Candy":
                        if quantities[2] <= 1:
                            popT = True
                        else:
                            popT = False
                        quantities[2] -= 1
                    elif cart[removeProdInt - 1] == ". Cookies":
                        if quantities[3] <= 1:
                            popT = True
                        else:
                            popT = False
                        quantities[3] -= 1
                    elif cart[removeProdInt - 1] == ". Water":
                        if quantities[4] <= 1:
                            popT = True
                        else:
                            popT = False
                        quantities[4] -= 1
                    elif cart[removeProdInt - 1] == ". Sandwich":
                        if quantities[5] <= 1:
                            popT = True
                        else:
                            popT = False
                        quantities[5] -= 1
                    validRemove = True
                    if popT == True:
                        cart.pop(removeProdInt - 1)
                    print("Removing item ", removeProd, "...")
                    time.sleep(1.5)
                break
            
            if validRemove == False:                                    #if input number doesnt match displayed number
                print()
                print("Please enter valid product number")
                removeProd = (input("Enter # of product to remove: "))  #we are trapped in input loop
            else:
                choice3 = False

    elif len(cart) == 0:
        print("is empty!")
        print("You cannot remove what isn't there.")
        print("returning in 3 seconds...")
        time.sleep(3)

def viewCart():
    choice4 = True
    while choice4:
        print("\n\n\n\n\n")
        print("~~~~~ YOUR SHOPPING CART ~~~~~")
        print()
        totalitemsinCart = 0
        for i in range(len(cart)):
            
            if cart[i] == ". Chips":
                tempPrice = "$2.00"
                amount = quantities[0]
            elif cart[i] == ". Soda":
                tempPrice = "$2.50"
                amount = quantities[1]
            elif cart[i] == ". Candy":
                tempPrice = "$1.50"
                amount = quantities[2]
            elif cart[i] == ". Cookies":
                tempPrice = "$3.00"
                amount = quantities[3]
            elif cart[i] == ". Water":
                tempPrice = "$1.00"
                amount = quantities[4]
            elif cart[i] == ". Sandwich":
                tempPrice = "$5.00"
                amount = quantities[5]
            totalitemsinCart += amount
            print(cartIdx[i], cart[i], tempPrice, "X", amount)
        print("Items:", totalitemsinCart)
        choice4Ret = input("Type 'close' to return: ")
        if choice4Ret != "close":
            choice4Ret = input("Please Type 'close' To Return: ")
        else:
            break

def viewTotal():
    choice5 = True
    while choice5:
        print("\n\n\n\n\n")
        print("~~~~~ YOUR SHOPPING CART ~~~~~")
        print()
        subtotal = 0
        for i in range(len(cart)):
            if cart[i] == ". Chips":
                subtotal += 2 * quantities[0]
                amount = quantities[0]
            elif cart[i] == ". Soda":
                subtotal += 2.5 * quantities[1]
                amount = quantities[1]
            elif cart[i] == ". Candy":
                subtotal += 1.5 * quantities[2]
                amount = quantities[2]
            elif cart[i] == ". Cookies":
                subtotal += 3 * quantities[3]
                amount = quantities[3]
            elif cart[i] == ". Water":
                subtotal += 1 * quantities[4]
                amount = quantities[4]
            elif cart[i] == ". Sandwich":
                subtotal += 5 * quantities[5]
                amount = quantities[5]
            print(cartIdx[i], cart[i], "X", amount)
        print()
        print(f"Subtotal: ${subtotal:,.2f}")
        choice5Ret = input("Type 'close' to return: ")
        if choice5Ret != "close":
            choice5Ret = input("Please Type 'close' To Return: ")
        else:
            break

def checkoutCart():
    choice6 = True
    date = datetime.datetime.now()
    formattedDate = date.strftime("%Y-%m-%d")
    while choice6:
        subtotal = 0
        if len(cart) != 0:
            for i in range(len(cart)):
                if cart[i] == ". Chips":
                    subtotal += 2 * quantities[0]
                elif cart[i] == ". Soda":
                    subtotal += 2.5 * quantities[1]
                elif cart[i] == ". Candy":
                    subtotal += 1.5 * quantities[2]
                elif cart[i] == ". Cookies":
                    subtotal += 3 * quantities[3]
                elif cart[i] == ". Water":
                    subtotal += 1 * quantities[4]
                elif cart[i] == ". Sandwich":
                    subtotal += 5 * quantities[5]
        else:
            print("\n\n\n\n\n")
            print("Cart is empty!")
            print("returning to menu in 2 sec.")
            time.sleep(2)
            break

        print("\n\n\n\n\n")
        print("~~~~~ CHECKOUT ~~~~~")
        print("Date: ", formattedDate)
        print()
        print(f"Subtotal: ${subtotal:,.2f}")
        if subtotal >= 10:
            discount = 0.05
        elif subtotal >= 20:
            discount = 0.1
        elif subtotal >= 40:
            discount = 0.15
        else:
            discount = 0
        print(f"Discount: {discount:.2%}")
        amountSaved = subtotal * discount
        print(f"Saved: ${amountSaved:,.2f}")
        print()
        totalPrice = subtotal - amountSaved
        print(f"Total Price: ${totalPrice:,.2f}")
        choice6Ret = input("Type 'checkout' to complete order: ")
        if choice6Ret != "checkout":
            choice6Ret = input("Please Type 'checkout' To Complete Order: ")
        else:
            print()
            print("Thanks for Shopping!")
            time.sleep(1)
            start = False
        break

#program boot
while start:


    print("\n\n\n\n\n")
    print("~~~~~~~~~~ SMART SHOPPING CART ~~~~~~~~~~")
    print()
    print("1. View available products")
    print("2. Add product to cart")
    print("3. Remove product from cart")
    print("4. View shopping cart")
    print("5. View current total")
    print("6. Checkout")
    print()
    choice = input("Enter your choice: ")

    if choice == "1": #view products
        viewProducts()
    elif choice == "2": #add product
        subtotal += addProducts()
    elif choice == "3": #remove item from cart
        removeItem()
    elif choice == "4": #viewing shopping cart
        viewCart()
    elif choice == "5":
        viewTotal()
    elif choice == "6":
        checkoutCart()
        if len(cart) != 0:
            break
    else:
        print("Invalid Option")
        time.sleep(2)
        #choice = input("Enter valid choice: ")