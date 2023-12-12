#shopping cart

# items are needed :check:
#price of items :check:
#add items to cart :check:
#del items from cart
#look at cart
#recipet
# cart


def shop():
    cart = []
    prices= []
    while True:
        choice = input("Welcome to wacky mart, what can i do for you? add to shop, del, to chuck stuff,view to view, quit to checkout!")
        if choice =="add":
            item = input("what would you like to buy?").lower()
            price = float(input("how many monies?"))
            cart.append(item)
            prices.append(price)
        elif choice =="del":
            item_to_del = input("what would you like to chuck?").lower()
            if item_to_del in cart:
                index_looking= cart.index(item_to_del)
                cart.remove(item_to_del)
                prices.pop(index_looking)
            else:
                print("hey crazy, you dont even have that in here!")

        elif choice =="view":
            for item in cart:
                print(item)
        elif choice =="quit":
            print(cart,sum(prices))
            break
        else:
            print("not valid, please try again")

print(shop())