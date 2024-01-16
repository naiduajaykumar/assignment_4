from Product import Product
from ShoppingCart import ShoppingCart
from Mystore import Mystore

def main():
    fname = 'ProductsData.txt'
    store = Mystore()
    plist = store.read_products_from_file(fname)
    scart = ShoppingCart()  # empty shopping cart

    main_menu = (
        '1: View Products\n'
        '2: Shop\n'
        '3: Checkout\n'
        '4: Add Product\n'
        '5: Remove Product\n'
        '0: Exit'
    )

    shopping_menu = (
        '\t1: Add Product to Cart\n'
        '\t2: Remove Product From Cart\n'
        '\t3: Show Cart\n'
        '\t4: Clear Cart\n'
        '\t0: Back to Main'
    )

    menu_option = 1

    while menu_option > 0:
        print('\n' + main_menu)
        menu_option = int(input('Please enter an option: '))

        if menu_option == 0:
            print('Quitting application...')
            break  # exit main loop

        if menu_option == 1:
            store.show_products()

        if menu_option == 2:
            shopping_menu_option = 1

            while shopping_menu_option > 0:
                print('\n' + shopping_menu)
                soption = input('\tPlease enter a shopping option: ')
                shopping_menu_option = int(soption)

                if shopping_menu_option == 1:  # add to cart
                    pid_qty = input('\tPlease enter productid,qty to buy (ex: 1001, 3): ')

                    if ',' not in pid_qty:
                        print('Invalid productid,qty specified...')
                    else:
                        parts = pid_qty.split(',')
                        pid = int(parts[0])
                        qty = int(parts[1])
                        pr = store.get_product(pid)

                        if pr is not None:
                            scart.add_item(pr, qty)

                if shopping_menu_option == 2:  # remove from cart
                    pid = int(input('\tPlease enter productid to remove from cart: '))
                    scart.remove_item(pid)

                if shopping_menu_option == 3:  # view cart
                    scart.show_cart()

                if shopping_menu_option == 4:  # clear cart
                    scart.clear_cart()

        if menu_option == 3:  # checkout
            total = scart.compute_total()
            print(total)
            total_after_discount = scart.apply_discount(total)
            print('\n------checkout info---------')
            print('Total Amount = ', total, ' Total Amount after discount = ', total_after_discount)

        if menu_option == 4:
            new_pr = input("Enter New Product (ex: pid,pname,price,category): ")

            if ',' not in new_pr:
                print('Invalid product details specified...')
            else:
                parts = new_pr.split(',')
                pid = int(parts[0])
                pname = parts[1]
                price = float(parts[2])
                category = parts[3]
                store.add_product(pid, pname, price, category)

        if menu_option == 5:
            pid = int(input('\tPlease enter productid to remove from store: '))
            store.remove_product(pid)


if __name__ == "__main__":
    main()
