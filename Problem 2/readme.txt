The Solution:
- This solution finds all the possible aggregations of the total amount and number of sales for a specific product for all the sales made to a specific client. It retrieves data from a file called sales.csv and outputs all these aggregations into a file called output.csv.


Running the solution:
- To run the solution for specific data, add the file containing the data into the Problem 2 main directory and run 'solution.py'. When prompted to provide a file name, enter the name of the file and the program will aggregate the data and create the output file. If an 'output.csv' file already exists, it will append the new aggregations to the already existing file. To ensure that the data is output to a new file, ensure that there is no file named 'output.csv' (not case sensitive) in the working directory.

- A sample sales.csv file is included

Plugins and 3rd Party Libraries
- No plugins or 3rd party libraries used

Assumptions:
The assumptions made when creating the programme were:
- The program is not meant to keep track of users through whom the sales were made.
- The client to whom the sale is made, logically, would know of all the sales that were made to them and the relevant details of said sales. This impacted how the classes were created and how they function
- the data is all required to be output into a single file, 'output.csv'.
- the name of the file containing the data will be sent/entered as input to the program
- The data provided will only contain sales made within a single year. If not, then the assumption is the aggregation is not concerned with the year of the sale and thus multiple sales from the same months in different years can be aggregated.

Scaling Considerations:
- In the event that the program has to be scaled, the different elements involved in the sale are all represented as objects that can be expanded upon. E.g. Amount, though only contained as a value in the input file, is made into an object in the program to allow for easier scaling if currencies and any other attributes of the amount are to be a factor to be considered.
- If the tuple is to be changed later on, e.g. to aggregate by year instead, a new aggregate function in the client class can be created and nothing else would need to be changed.
