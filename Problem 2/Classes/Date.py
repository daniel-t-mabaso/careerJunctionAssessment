class Date:
    
    def __init__(self, day, month, year):
        """Date constructor/initialiser. Called when creating a new Date object
    
            Parameters:
            self (Date): the calling object
            day (String): day of the month
            month (String): day of the month
            year (String): year of date
            
           """         
        self.day = day
        self.month = month
        self.year = year
        
    #Getters
    def get_day(self):
        """Function to get the day
    
            Parameters:
            self (Date): the calling object
            
            Returns:
            String: returns the day
           """         
        return self.day
    
    def get_month(self):
        """Function to get the month
    
            Parameters:
            self (Date): the calling object
            
            Returns:
            String: returns the month
           """         
        return self.month
    
    def get_year(self):
        """Function to get the year
    
            Parameters:
            self (Date): the calling object
            
            Returns:
            String: returns the year
           """         
        return self.year

    #Setters
    def set_day(self,day):
        """Function to set the day
    
            Parameters:
            self (Date): the calling object
            day (String): the new day
            
           """         
        self.day = day
        
    def set_month(self,month):
        """Function to set the month
    
            Parameters:
            self (Date): the calling object
            month (String): the new month
            
           """         
        self.month = month
        
    def get_year(self,year):
        """Function to set the year
    
            Parameters:
            self (Date): the calling object
            year (String): the new year
            
           """         
        self.year = year