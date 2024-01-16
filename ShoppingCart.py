import pickle


class ShoppingItem(object):
    def __init__(self, prod, qty):
        self.product = prod
        self.quantity = qty


class ShoppingCart(object):
    def __init__(self):
        try:
            with open("ShoppingCart.pickle", "rb") as my_file:
                self.items = pickle.load(my_file)
                for i in self.items:
                    print(i)
        except FileNotFoundError:
            self.items = []  # in the beginning, the shopping cart is empty

    def add_item(self, product, qty):
        sitem = ShoppingItem(product, qty)
        self.items.append(sitem)
        with open("ShoppingCart.pickle", "wb") as file:
            pickle.dump(self.items, file)
        print(f"{product.product_name} of {qty} is added to cart...")

    def remove_item(self, pid):  # remove item from cart
        item_to_remove = None
        for item in self.items:
            if item.product.product_id == pid:
                item_to_remove = item
        if item_to_remove is not None:
            self.items.remove(item_to_remove)
            print(f"{pid} of id is removed...")
        else:
            print(f"No item with pid {pid} found in the cart...")

    def compute_total(self):  # total price of items in shopping cart
        total = sum(item.product.price * item.quantity for item in self.items)
        return total

    def apply_discount(self, total):
        if 100 < total < 500:
            total = total - (total * 5 / 100)
        elif 500 < total < 1000:
            total = total - (total * 10 / 100)
        else:
            total = total - (total * 15 / 100)
        return total

    def show_cart(self):
        if (len(self.items) == 0):
            print("No items in the cart")
            return
        for item in self.items:
            print('\t\t' + item.product.__str__().replace('\n', '') +
                  '\tqty=' + str(item.quantity))

    def clear_cart(self):
        self.items.clear()
        print("Cart is Cleared...")
        with open("ShoppingCart.pickle", "wb") as file:
            pickle.dump(self.items, file)
