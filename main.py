import time

product = ["chips", "soda", "candy", "cookies", "water", "sandwich"]
prices = ["$2.0", "$2.5", "$1.5", "$3.0", "$1.0", "$5.0"]
productIdx = ["1. ", "2. ", "3. ", "4. ", "5. ", "6. "]
cart = []
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

    if choice == "1":
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
    elif choice == "2":
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
                if addProd == 1:
                    print("Chips were added to cart!")
                elif addProd == 2:
                    print("Soda was added to cart!")
                elif addProd == 3:
                    print("Candy was added to cart!")
                elif addProd == 4:
                    print("Cookies were added to cart!")
                elif addProd == 5:
                    print("Water was added to cart!")
                elif addProd == 6:
                    print("Sandwich was added to cart!")
                break
            else:
                print()
                print("Please enter valid product number")
                addProd = int(input("Enter product number: "))
    elif choice == "3":
        choice3 = True
        

