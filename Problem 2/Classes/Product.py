class Product:
    def __init__(self, name):
        """Product constructor/initialiser. Called when creating a new Product object
    
            Parameters:
            self (Product): the calling object
            name (String): the name of the new product
            
           """ 
        self.name = name
    
    def get_name(self):
        """Function to get the product name
    
            Parameters:
            self (Product): the calling object
            
            Returns:
            String: returns the product name
           """         
        return self.name
    
    def set_name(self,name):
        """Function to set the product name
    
            Parameters:
            self (Product): the calling object
            name (String): the new product name
            
           """         
        self.name = name        
