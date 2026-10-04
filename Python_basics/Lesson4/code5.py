


class product:
    product_count = 0
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount
        product.product_count += 1

    def show_data(self):
        print(f"The name of product is {self.name}, price is {self.price} at a discount {self.discount}%.")

    @classmethod
    def show_count(cls):
         print(f"The count of total product is {cls.product_count}")

    @staticmethod
    def calculate_discount(price, discount):
        final_price = price - ((discount/100) * price)
        return final_price

laptop = product("Apple", 40000, 15)
laptop.show_data()
phone = product("samsung", 80000, 25)
phone.show_data()
result = laptop.calculate_discount(laptop.price, laptop.discount)
print(f"Final Discount on {laptop.name} is {result}")
result = laptop.calculate_discount(phone.price, phone.discount)
print(f"Final Discount on {phone.name} is {result}")
product.show_count()