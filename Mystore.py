import pickle
from Product import Product


class Mystore(object):

    def __init__(self):
        try:
            with open("ProductsData.pickle", 'rb') as file:
                self.plist = pickle.load(file)
        except FileNotFoundError:
            self.plist = []  # in the beginning, the product list is empty

    def read_products_from_file(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            plist = []  # product list
            for line in lines:
                parts = line.split(',')  # split line into parts
                pr = Product(int(parts[0]), parts[1], float(parts[2]), parts[3])
                self.plist.append(pr)

    def show_products(self):
        for pr in self.plist:
            print(pr, end='')  # end='' suppresses newline after each print

    def get_product(self, pid):
        for pr in self.plist:
            if pr.product_id == pid:
                return pr
        return None

    def add_product(self, id, name, price, category):
        product = Product(id, name, price, category)
        self.plist.append(product)
        with open("ProductsData.txt", mode="a") as file:
            file.write("\n" + f"{id},{name},{price},{category}")
        with open("ProductsData.pickle", "ab") as file:
            pickle.dump(product, file)
        print(f"The item {product.product_name} is added to store...")

    def remove_product(self, pid):
        removed_ele = None
        for product in self.plist:
            if product.product_id == pid:
                removed_ele = product
                if removed_ele is not None:
                    self.plist.remove(removed_ele)
                    print(f"The item {removed_ele.product_name} is removed from store...")
                    with open("ProductsData.txt", "w") as file:
                        for each in self.plist:
                            file.write(f"{each.product_id},{each.product_name},{each.price},{each.category}")
                    with open("ProductsData.pickle", "wb") as file:
                        pickle.dump(self.plist, file)
                else:
                    print(f"Please enter the pid that is being available in store...")
