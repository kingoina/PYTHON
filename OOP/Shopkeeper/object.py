class Shopkeeper:
    
    def __init__(self):
        self.items = {"flour":150, "sugar": 170, "rice":190, "cake": 250}
        
    def displayItems(self, customerName):
        """Displays the items being sold"""
        print(f"Hello {customerName}, Welcome to our store.\n\nHere are the available item:")
        
        for item in self.items:
            print(f"{item}  : {self.items[item]}")
    
    def calculatePrice(self, products):
        productList = products.split(",")

        productList = [item.strip().lower() for item in productList]

            
            
        print(f"Your selected items are: {productList}")  
        total = 0
        for item in productList:
            if item in self.items:
                total +=  self.items[item]
                print(f"The price of {item} is {self.items[item]}. ")
        print(f"- - - - - - - - - - - - - - - - - - - - - - - - - - -\nTotal to pay: KES {total}\n\nThanks for buying from us.see you next time.\n- - - - - - - - - - - - - - - - - - - - - - - - - - -")