class Client:
    
    def __init__(self, name):
        """Client constructor/initialiser. Called when creating a new Client object
    
            Parameters:
            self (Client): the calling object
            name (String): the name of the new client
            
           """         
        #client name is a private variable
        self.name = name
        self.sales = []
        
    #Setters
    def set_name(self, name):
        """Function to set the client's name
    
            Parameters:
            self (Client): the calling object
            name (String): the new client name
            
           """         
        self.name = name
        
    #Getters
    def get_name(self):
        """Function to get the client name
    
            Parameters:
            self (Client): the calling object
            
            Returns:
            String: returns the client name
           """         
        return self.name
        
    def get_sales(self):
        """Function to associate a sale with the client to which the sale was made. It adds the sale to the client's list of sales
    
            Parameters:
            self (Client): the calling object
            
            Returns:
            list: returns a list of the sales made to this client
           """        
        return self.sales
        
    def buy(self, sale):
        """Function to associate a sale with the client to which the sale was made. It adds the sale to the client's list of sales
    
            Parameters:
            self (Client): the calling object
            sale (Sale): the sale that was made to the client
            
           """
        #append this sale to the client's sales list
        self.sales.append(sale)

    def get_unique_products(self):
        """Function to get all unique product names that this client has bought
    
            Parameters:
            self (Client): the calling object
            
            Returns:
            list: Returns a list of product names unique to client purchases
    
           """          
        #create a new list that will store the results
        result = []
        for x in self.sales:
            #for each sale get the product name. If it is already in the result, continue to the next sale otherwise add it to the result list
            name = x.get_product().get_name();
            if name in result:
                continue
            else:
                result.append(name)
                
        #return the result
        return result
    
    
    def get_unique_months(self):
        """Function to get all unique months that this client has made sales
    
            Parameters:
            self (Client): the calling object
            
            Returns:
            list: Returns a list of months unique to client sales
    
           """        
        #create a new list that will store the results
        result = []
        for x in self.sales:
            #for each sale get the month. If it is already in the result, continue to the next sale otherwise add it to the result list
            name = x.get_date().get_month();
            if name in result:
                continue
            else:
                result.append(name)
        #return the result
        return result
    
    def aggregate_sale_by_month(self, product, month):
        """Function to aggregate this sale based on the specified product and month
    
            Parameters:
            self (Client): the calling object
            product (String): product name
            month (String): month
            
            Returns:
            String: Returns the results of the aggregation as a comma separated string
    
           """
        
        #count and sum up the amounts for the sales that matched the criteria in set in the tuple
        count = 0
        amount = 0
        
        for sale in self.get_sales():
            #for all the sales that were made to this client
            if(sale.get_product().get_name() == product and sale.get_date().get_month() == month):
                #if the sale matches the query tuple, increase count and add sale amount to the amount sum
                count +=1
                amount += sale.get_amount().get_value()
        if(count!=0):
            #if at least one sale that matched the criteria in set in the tuple, return the aggregated results
            return str("'" + self.get_name() + "','" + product + "','" + month + "'," + str("%.2f" % amount) + "," + str(count)+"\n")
        #no aggregated data is available, so return an empty string
        return ""