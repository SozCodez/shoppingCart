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
        for i in range(len(cart)):
            print(cartIdx[i], cart[i])
        print()
        removeProd = (input("Enter # of product you \nwould like to remove: "))
        removeProdInt = int(removeProd)
        validRemove = False
        while choice3:
            for i in range(len(cart)):
                print(i)
                    # 2                   2            [1, 2]
                if removeProdInt == cartIdx[i]:
                    print("SKJHKJDSHKJDHKSJ")
                    validRemove = True
                    print("TEST:",removeProdInt)
                    print("Cart", cart)
                    cart.pop(removeProdInt - 1)


            if validRemove == False:
                print()
                print("Please enter valid product number")
                removeProd = (input("Enter # of product to remove: "))
                print(cartIdx)

            break

        
        

