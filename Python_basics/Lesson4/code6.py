# Today we will talk about encapsulation
# encapsulation will be used wrap up data members as variables and behaviours as methods into one unit that is class
# we can also do data hiding here by making variables public, private and protected
# public variables are accessible from inside and outside of the class
# protected variables can be accessed inside of the class and classes it is inherited to
# private variables are accessed only from inside of the class only

class bank_account:
    def __init__(self, name, balance):
        self._name = name # so if you want to create a protected variable you have to put single underscore before it

        self.__balance = balance # for the private variable you have to use 2 underscores to make it private

    def display_balance(self):
        print(f"The balance for {self._name} is {self.__balance}")
        # this function is nothing but getter, meaning we are not able to access the balance outside so to access it outside 
        # we can use inside methods to display it.

    def set_balance(self, new_balance):
        self.__balance = new_balance
        # this method is nothing but setter again to update the private variables we can use setter functions
        # remember getter and setter are just type of functions that can be used for this purpose and can be named anything

p1 = bank_account("Ashish", 1500_000)
p1.display_balance()
p1.set_balance(200_0000)
p1.display_balance()
# now here we have seen public, private, protected variables but there are ways from which you still can access the variables

# for protected variables
print(p1._name) # this is an proted variable but still can be accessed outside the class
# because protected here is just a convention which asks programmers to follow that this is a protected variable
# and make the program in a fashion so that you should not access the protected variable and maintain its dignity

#for private variables
#print(p1.__balance) # this line will give you an error so you can not access it directly

print(f"The balance is {p1._bank_account__balance}") # this is the way to do it, after .write class name after the single underscore
# and then write private variable name as it is created without . or self, just __varName

# so in python it is actually no true safety but if while making program we do not follow the convention we are 
# not using the concept of encapsulation in python and program just ignored one pillar of oops, which is not good so follow them
