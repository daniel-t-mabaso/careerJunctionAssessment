class Sale:
    
    def __init__(self, product, date, amount):
        """Sale constructor/initialiser. Called when creating a new Sale object
    
            Parameters:
            self (Sale): the calling object
            product (Product): the name of the product being bought
            amount (Amount): cost of sale
            
           """ 
        self.product = product
        self.date = date
        self.amount = amount
        
    def get_product(self):
        """Function to get the product being sold
    
            Parameters:
            self (Sale): the calling object
            
            Returns:
            Product: returns the product being sold
           """         
        return self.product
    
    def get_date(self):
        """Function to get the date of sale
    
            Parameters:
            self (Sale): the calling object
            
            Returns:
            Date: returns the date of sale
           """         
        return self.date
    
    def get_amount(self):
        """Function to get the amount of sale
    
            Parameters:
            self (Sale): the calling object
            
            Returns:
            Amount: returns the amount of sale
           """         
        return self.amount

    def set_product(self,product):
        """Function to set the product being sold
    
            Parameters:
            self (Sale): the calling object
            product (Product): the new product
            
           """         
        self.product = product
        
    def set_date(self,date):
        """Function to set the date of sale
    
            Parameters:
            self (Sale): the calling object
            product (Date): the new date
            
           """  
        self.date = date
        
    def set_amount(self,amount):
        """Function to set the amount of the sale
    
            Parameters:
            self (Sale): the calling object
            product (Amount): the new product
            
           """  
        self.amount = amount
