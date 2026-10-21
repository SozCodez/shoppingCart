import time

product = ["chips", "soda", "candy", "cookies", "water", "sandwich"]
prices = ["$2.0", "$2.5", "$1.5", "$3.0", "$1.0", "$5.0"]
productIdx = ["1. ", "2. ", "3. ", "4. ", "5. ", "6. "]
cart = []
cartIdx = []
cartCnt = 0
start = True
#global variables/ lists


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
        choice1 = True
        while choice1:
            print("\n \n \n \n \n")
            for i in range(len(product)):
                print(product[i], " ", prices[i])
            print()
            print()
            choice1Ret = input("Type 'close' to return: ")
            if choice1Ret == "close":
                break
    elif choice == "2": #add product
        choice2 = True
        print("\n \n \n \n \n")
        print("Which product would you like to add?")
        print()
        for i in range(len(product)):
            print(productIdx[i], product[i])
        print()
        addProd = int(input("Enter product number: "))
        print()
        while choice2:
            if addProd == 1 or addProd == 2 or addProd == 3 or addProd == 4 or addProd == 5 or addProd == 6:
                cartCnt = cartCnt + 1
                strcartCnt = str(cartCnt)
                if addProd == 1:
                    print("Chips were added to cart!")
                    cart.append(". Chips")
                    cartIdx.append(cartCnt)
                elif addProd == 2:
                    print("Soda was added to cart!")
                    cart.append(". Soda")
                    cartIdx.append(cartCnt)
                elif addProd == 3:
                    print("Candy was added to cart!")
                    cart.append(". Candy")
                    cartIdx.append(cartCnt)
                elif addProd == 4:
                    print("Cookies were added to cart!")
                    cart.append(". Cookies")
                    cartIdx.append(cartCnt)
                elif addProd == 5:
                    print("Water was added to cart!")
                    cart.append(". Water")
                    cartIdx.append(cartCnt)
                elif addProd == 6:
                    print("Sandwich was added to cart!")
                    cart.append(". Sandwich")
                    cartIdx.append(cartCnt)
                break
            else:
                print()
                print("Please enter valid product number")
                addProd = int(input("Enter product number: "))
    elif choice == "3": #remove item from cart
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
            while choice3:
                for i in range(len(cart)):
                    #print(i)
                        # 2                   2            [1, 2]
                    if removeProdInt == cartIdx[i]:
                        validRemove = True
                        cart.pop(removeProdInt - 1)
                        print("Removing item ", removeProd, "...")
                        time.sleep(1.5)

                if validRemove == False:
                    print()
                    print("Please enter valid product number")
                    removeProd = (input("Enter # of product to remove: "))
                    print(cartIdx)
                break
        elif len(cart) == 0:
            print("is empty!")
            print("You cannot remove what isn't there.")
            print("returning in 3 seconds...")
            time.sleep(3)

    elif choice == "4": #viewing shopping cart
        choice4 = True
        while choice4:
            print("\n\n\n\n\n")
            print("~~~~~ YOUR SHOPPING CART ~~~~~")
            print()
            totalitemsinCart = 0
            for i in range(len(cart)):
                totalitemsinCart += 1
                if cart[i] == ". Chips":
                    tempPrice = "$2.00"
                elif cart[i] == ". Soda":
                    tempPrice = "$2.50"
                elif cart[i] == ". Candy":
                    tempPrice = "$1.50"
                elif cart[i] == ". Cookies":
                    tempPrice = "$3.00"
                elif cart[i] == ". Water":
                    tempPrice = "$1.00"
                elif cart[i] == ". Sandwich":
                    tempPrice = "$5.00"

                print(cartIdx[i], cart[i], tempPrice)
            print("Items:", totalitemsinCart)
            choice4Ret = input("Type 'close' to return: ")
            if choice4Ret != "close":
                choice4Ret = input("Please Type 'close' To Return: ")
            else:
                break
    elif choice == "5":
        choice5 = True
        while choice5:
            print("\n\n\n\n\n")
            print("~~~~~ YOUR SHOPPING CART ~~~~~")
            print()
            subtotal = 0
            for i in range(len(cart)):
                if cart[i] == ". Chips":
                    subtotal += 2
                elif cart[i] == ". Soda":
                    subtotal += 2.5
                elif cart[i] == ". Candy":
                    subtotal += 1.5
                elif cart[i] == ". Cookies":
                    subtotal += 3
                elif cart[i] == ". Water":
                    subtotal += 1
                elif cart[i] == ". Sandwich":
                    subtotal += 5
                print(cartIdx[i], cart[i])
            print()
            print(f"Subtotal: ${subtotal:,.2f}")
            choice5Ret = input("Type 'close' to return: ")
            if choice5Ret != "close":
                choice5Ret = input("Please Type 'close' To Return: ")
            else:
                break
        
