class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_product(self, price, quantity):
        self.price = price
        self.quantity = quantity
        print("Product updated successfully!")

    def display_product(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print()


class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_item_to_cart(self, product, quantity):
        if product.quantity >= quantity:
            self.cart_items.append((product, quantity))
            print("Item added to cart successfully!")
        else:
            print("Requested quantity is not available for the selected product!")

    def remove_item_from_cart(self, product):
        for item in self.cart_items:
            if item[0].name == product.name:
                self.cart_items.remove(item)
                print("Item removed from cart successfully!")
                return
        print("Item not found in the cart!")

    def update_item_in_cart(self, product, new_quantity):
        for item in self.cart_items:
            if item[0].name == product.name:
                if product.quantity >= new_quantity:
                    item = (item[0], new_quantity)
                    print("Item updated in cart successfully!")
                else:
                    print("Requested quantity is not available for the selected product!")
                return
        print("Item not found in the cart!")

    def display_cart(self):
        print("Items in the cart:")
        for product, quantity in self.cart_items:
            print("Product Name:", product.name)
            print("Price per item:", product.price)
            print("Quantity in cart:", quantity)
            total = product.price * quantity
            print("Total:", total)
            print()

    def calculate_total_cost(self):
        total_cost = 0
        for product, quantity in self.cart_items:
            total_cost += product.price * quantity
        return total_cost

    def apply_discount(self, discount_percentage):
        total_cost = self.calculate_total_cost()
        if total_cost > 10000:
            discount_amount = int(total_cost * discount_percentage)
            total_cost -= discount_amount
            print("Discount applied:", discount_amount)

        # Apply Kenyan VAT (Value Added Tax) of 16%
        vat_percentage = 0.16
        vat_amount = int(total_cost * vat_percentage)
        total_cost += vat_amount
        print("VAT applied:", vat_amount)

        print("Total Cost (after discount and taxes):", total_cost)


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added successfully!")

    def update_product(self, product_name, new_price, new_quantity):
        for product in self.products:
            if product.name == product_name:
                product.update_product(new_price, new_quantity)
                return
        print("Product not found!")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print("Product removed successfully!")
                return
        print("Product not found!")

    def display_all_products(self):
        if not self.products:
            print("No products available.")
            return

        total_price = 0
        print("Available Products:")
        for product in self.products:
            product.display_product()
            total_price += product.price * product.quantity
        print("Total Price of all products:", total_price)


def get_product_by_name(products, product_name):
    for product in products:
        if product.name == product_name:
            return product
    return None


if __name__ == "__main__":
    shop = Shop()
    cart = ShoppingCart()  # Create the cart object

    while True:
        print("\nSelect an option:")
        print("1. Add product")
        print("2. Update product")
        print("3. Remove product")
        print("4. Display all products")
        print("5. Add item to cart")
        print("6. Update item in cart")
        print("7. Remove item from cart")
        print("8. Display cart")
        print("9. Apply discount and calculate total cost")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter product name: ")
            price = int(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            shop.add_product(Product(name, price, quantity))
        elif choice == 2:
            name = input("Enter product name to update: ")
            new_price = int(input("Enter new price: "))
            new_quantity = int(input("Enter new quantity: "))
            shop.update_product(name, new_price, new_quantity)
        elif choice == 3:
            name = input("Enter product name to remove: ")
            shop.remove_product(name)
        elif choice == 4:
            shop.display_all_products()
        elif choice == 5:
            product_name = input("Enter product name to add to cart: ")
            quantity = int(input("Enter quantity to add to cart: "))
            product = get_product_by_name(shop.products, product_name)
            if product:
                cart.add_item_to_cart(product, quantity)
        elif choice == 6:
            product_name = input("Enter product name to update in cart: ")
            new_quantity = int(input("Enter new quantity in cart: "))
            product = get_product_by_name(shop.products, product_name)
            if product:
                cart.update_item_in_cart(product, new_quantity)
        elif choice == 7:
            product_name = input("Enter product name to remove from cart: ")
            product = get_product_by_name(shop.products, product_name)
            if product:
                cart.remove_item_from_cart(product)
        elif choice == 8:
            cart.display_cart()
        elif choice == 9:
            cart.apply_discount(0.05)  # Apply 5% discount if the total cost is above 10000
        elif choice == 0:
            break
        else:
            print("Invalid choice! Please try again.")
