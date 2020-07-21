"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    #Class attribute
    cache = {} #Dictionary to store all cupcake instances by name
    cls = "cupcake"

    def __init__(self, name, flavor, price):
        """Initialize an instance of the class Cupcake"""

        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0
        self.cache[name] = self #Adds new cupcake w/ key "name", value "object" 


    def add_stock(self, amount):
        """Add amount to self.qty"""

        self.qty = self.qty + amount


    def sell(self, amount):
        """Sell the amount and update self.qty"""

        
        if self.qty == 0:

            print(f"Sorry, these {self.cls}s are sold out")
            return

        if amount > self.qty: 
            #Sell all cupcakes that we have.
            self.qty = 0
            return

        self.qty = self.qty - amount
            

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    @staticmethod
    def scale_recipe(ingredients, amount):
        """Scale the list of ingerdients by the amount of cupcakes."""

        #print("ingredients:", ingredients)
        #print("amount:", amount)

        scaled_ingredients = [] #This is a list that will contain tuples
        for ingredient, qty in ingredients: #Loop through list of tupes 

            scaled_ingredients.append((ingredient, qty*amount)) #update quantity
            
        #print("ingredients:", ingredients)

        return scaled_ingredients #Returns list of tuples containing scaled amts 


    @classmethod
    def get(cls, name):
        """Return a cupcake from cls.cache"""

        if name in cls.cache:
            print(cls.cache[name]) #prints the dictionary value at the name key
        
        else:
            print("Sorry, that cupcake doesn't exist")


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')

#Specs or brownie are almost the same as for cupcake, but flavor is chocolate

class Brownie(Cupcake):
    
    cls = "brownie"

    def __init__(self, name, price): #Only need to pass in name and price
        """Initialize an instance of the class Cupcake"""

        super().__init__(name, "Chocolate", price) #Hard code "Chocolate"


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Brownie name="{self.name}" qty={self.qty}>'


