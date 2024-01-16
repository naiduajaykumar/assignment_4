class Product(object):
    def __init__(self, pid, pname, price, cat):
        # Constructor
        self.product_id = pid
        self.product_name = pname
        self.price = price
        self.category = cat

    def __str__(self):
        return f"{self.product_id}\t{self.product_name}\t\t{self.price}\t{self.category}"

    def __repr__(self):
        return f"{self.product_id}\t{self.product_name}\t{self.price}\t{self.category}"
