# talkpython.fm
# the idea is to create ShoppingCart class, which is iterable; you can iterate over the list of items in a for loop
# later, you create ShoppingCartSorted class, which is iterable but sorted based on the price property of CartItem.

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    def __iter__(self):
        return iter(self.items)


class ShoppingCartSorted(ShoppingCart):
    def __iter__(self):
        sorted_items = sorted(self.items, key=lambda i: -i.price)
        # return iter(sorted_items)
        for i in sorted_items:
            yield i


class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name


# iterate over a ShoppingCart object
cart = ShoppingCart()
cart.add_item(CartItem("guitar", 799))
cart.add_item(CartItem("cd", 19))
cart.add_item(CartItem("iPhone", 699))

print('ShoppingCart printed')
for item in cart:
    print(item.name, item.price)

# iterate over a ShoppingCartSorted object
cart_sorted = ShoppingCartSorted()
cart_sorted.add_item(CartItem("guitar", 799))
cart_sorted.add_item(CartItem("cd", 19))
cart_sorted.add_item(CartItem("iPhone", 699))

print('-'*len('ShoppingCartSorted printed'))
print('ShoppingCartSorted printed')
for item in cart_sorted:
    print(item.name, item.price)


# Can we for-in the cart?
# what if it was to be sorted?

# print("Items in your cart.")
# for item in cart:
#     print(" * {} ${}".format(item.name, item.price))