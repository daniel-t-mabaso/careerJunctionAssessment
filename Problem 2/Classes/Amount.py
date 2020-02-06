class Amount:
    def __init__(self, value, currency):
        """Amount constructor/initialiser. Called when creating a new Amount object
    
            Parameters:
            self (Amount): the calling object
            value (float): amount value
            currency (String): the currency for the amount
            
           """ 
        self.value = value
        self.currency = currency
    
    #getters
    def get_value(self):
        """Function to get the amount value
    
            Parameters:
            self (Amount): the calling object
            
            Returns:
            String: returns the amount value
           """         
        return self.value
    def get_currency(self):
        """Function to get the amount currency
    
            Parameters:
            self (Amount): the calling object
            
            Returns:
            String: returns the amount currency
           """         
        return self.currency
    
    #Setters
    def set_value(self, value):
        """Function to set the amount value
    
            Parameters:
            self (Amount): the calling object
            value (float): the new amount value
            
           """         
        self.value = value
    def set_currency(self, currency):
        """Function to set the amount currency
    
            Parameters:
            self (Amount): the calling object
            currency (String): the new amount currency
            
           """         
        self.currency = currency
