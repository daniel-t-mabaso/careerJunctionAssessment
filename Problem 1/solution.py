def solution(A, N):
   """Function to check whether a list index is an equilibrium index
   
       Parameters:
       A (list): list containing all the values
       N (int): the index to check

   
       Returns:
       int: Returns any equilibrium indices or -1 if none exists
   
      """
   def listSum(array, start, end):
      """ Calculates the sum of all elements in the list
   
       Parameters:
       array (list): list containing all the values
       start (int): start index for new partition
       end (int): end index for new partition. If end is -1, partition ends at the end of the given array.
   
       Returns:
       int: Returns sum of all the elements in the left or right list partition
   
      """     
      sum = 0;
      if(end == -1):
         end = len(array)
      for i in range(start, end):
         sum += array[i]
      return sum;
   
   count = 0;
   # loop through list determining if index 'count' is an equilibrium index
   while (count<N):
      
      # get the sum of the left partition of the list from the index
      left = listSum(A, 0, count)
      # get the sum of the right partition of the list from the index
      right =  listSum(A, count+1, -1)
      
      #check if current index is an equilibrium index
      if(left == right):
         return count
      
      #increment index because current index 0<= count < N
      count = count +1
      
   #no equilibrium index was found
   return -1
