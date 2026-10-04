# class methods and instance methods and static methods

class laptop:
    storage_type = "ssd" # class variable

    def __init__(self, ram, storage): # this is instance method because it has first variable self
        self.ram = ram
        self.storage = storage

    @classmethod # this is decorator which tells that this method is class method
    def show_data_class(cls): # cls will be the first parameter in class methods and can be called by both class and object
        print(cls.storage_type)

    def show_data(self): # this is also instance method only be called by object
        print(self.storage)
        print(self.ram)

    @staticmethod # decorator for static method
    def calulate_final_price(amount, discount): # this is static method where no self or cls required
        return (amount - ((discount/100) * amount))
    # these can be called by both class and object with required parameters

laptop1 = laptop("8gb", "1tb")
laptop1.show_data()
laptop.show_data_class()
print(laptop1.calulate_final_price(40_000, 5))   