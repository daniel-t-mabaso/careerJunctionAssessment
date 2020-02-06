from Classes import Client
from Classes import Date
from Classes import Amount
from Classes import Product
from Classes import Sale


def writeToOutput(line, file):
    """Function to append a line to a specified file. If file doesn't already exist, a new one is created

        Parameters:
        line (String): the line to be written to file
        file (String): Name of file to be written to

       """
    
    f = open("output.csv", "a+")
    f.write(line)
    f.close()  

def get_data(file):
    """Function to get the contents of a file
    
        Parameters:
        file (String): Name of file from which the data must be retrieved
 
    
        Returns:
        String: Returns the contents of the file
    
       """
    
    contents = ""
    
    try:
        #try to open the file
        f= open(file,"r")
    except FileNotFoundError:
        #Catch no file found error and print an error message
        print("Error: "+file+" not found!")
        return
    #store file contents, close file and return the contents
    contents = f.readlines()
    f.close()    
    return contents

def aggregate_data(contents):
    """Function to aggregate sales data and write the results to a file called output.csv
    
        Parameters:
        contents (String): data to be aggregated
 
       """    
    # create result string that will be outputed to the CSV file
    writeToOutput("Client,Product,Month,total amount,count\n", "output.csv")
    
    # Used to check if the first line with column names hasn't be read yet
    firstLineRead = False
    #dictionary of all unique clients in CSV file. The key is the client name and the value is the associated client object
    clients = {}
    for line in contents:
        if(not firstLineRead):
            #skip first line of file and continue to the next one
            firstLineRead = True
            continue
        #remove single quotes and turn comma separated string into list
        line = line.replace("'","")
        lineArray = line.split(",")
        
        #client name is on the second index of the list (index 1 on zero rated indicice)
        if lineArray[1] in clients:
            #if client name is already in local clients dictionary, get the client object from the dictionary
            client = clients[lineArray[1]]
        else:
            #client is not in dictionary, so create a new Client object with the data (client name) from the CSV file
            client = Client.Client(lineArray[1])
         
        #create Product and Date objects with data from CSV file   
        product = Product.Product(lineArray[3])
        date = Date.Date(lineArray[2].split("-")[0], lineArray[2].split("-")[1], lineArray[2].split("-")[2])
        
        #get the amount an currency
        amountString=float(lineArray[4]);
        amountValue = 0
        currency = "ZAR"
        if(str(amountString).replace('.','',1).isdigit()):
            amountValue = amountString
        else:
            for i, character in enumerate(amountString):
                if character.isdigit():
                    currency = amountString[0:i]
                    amountValue = amountString[i:]
                    break
            
        amount = Amount.Amount(amountValue, currency)
        #create sale with newly created product and date objects. Get sale amount from CSV file and store as a float in sale object
        sale = Sale.Sale(product, date,amount)
        
        #associate sale with client to whom the sale was made
        client.buy(sale)
        #update client object in client dictionary
        clients[client.get_name()] = client

    #for all clients, aggregate the sales by the tuple (client, product, month)
    for client in clients:
        #get all products bought by this client
        product_names = clients[client].get_unique_products()
        #get all months on which a sale was made to the client
        sale_months = clients[client].get_unique_months()
        
        #for each product, get the aggregates for each month
        for product_name in product_names:
            for sale_month in sale_months:
                #write result to file
                writeToOutput(clients[client].aggregate_sale_by_month(product_name, sale_month), "output.csv")
    print("Data successfully aggregated and saved to output.csv in the current directory")

def main():
    """Main Function to get sales data, aggregate it and write the results to a file called output.csv
    
        Parameters:
        contents (String): data to be aggregated
 
       """     
    file_name = input("What file name contains the data?\n")
    #fetch data from CSV file
    data = get_data(file_name)
    #aggregate data and output to output.CSV
    if(data):
        print("aggregating data...")
        aggregate_data(data)

if __name__ == '__main__':
    main()  