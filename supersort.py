import time

class MyArray:
  def __init__(self, array):
    self.sorted = self.supersort(array,0, len(array))

  def merge(self, M , N):
      merged_list = []

      len_M = len(M) if M else 0
      len_N = len(N) if N else 0
      i, j = 0,0

      while (i+j) < (len_M + len_N):
          if i == len_M:      		#if list M is empty, append entire list N to merged_list
              merged_list.append(N[j])
              j = j+1
          elif j == len_N:    		#if list N is empty, append entire list M to merged_list
              merged_list.append(M[i])
              i = i+1
          elif M[i] <= N[j]:  		#head of M is smaller, append element from M
              merged_list.append(M[i])
              i = i+1
          elif M[i] > N[j]:   		#head of N is smaller, append element from N
              merged_list.append(N[j])
              j = j+1
      return(merged_list)    		#return the merged list


  #Sorting function
  def supersort(self, my_list, left, right):
      if len(my_list) == 0:  	
          return

      sorted_forward_list = [] 
      sorted_backward_list = [] 

      # Filtering out values to the FORWARD SORTED ARRAY
      current_highest = my_list[0]  	
      sorted_forward_list.append(current_highest)

      for i in range(left+1, right):  				
          if my_list[i] >= current_highest: 			 
              current_highest = my_list[i]  		 
              sorted_forward_list.append(current_highest) 	

      for number in sorted_forward_list:      	  
          if number in my_list: 				
              my_list.remove(number)				

    
      # Filtering out values to the BACKWARD SORTED ARRAY
      if len(my_list) > 1:

          current_highest = my_list[-1] 			
          sorted_backward_list.append(current_highest)  

          for i in range(-2, -(len(my_list)+1), -1):
              if my_list[i] >= current_highest:
                  current_highest = my_list[i]  		
                  sorted_backward_list.append(current_highest) 

          for number in sorted_backward_list:    		
              if number in my_list: 			
                  my_list.remove(number)			

      merge_1 = self.merge(sorted_forward_list, sorted_backward_list)

      mid = len(my_list)//2     				
      Left_sublist = my_list[ : mid]  			
      Right_sublist = my_list[mid : ]  				
      left_sorted_list = self.supersort(Left_sublist, 0, len(Left_sublist))   
      right_sorted_list = self.supersort(Right_sublist, 0, len(Right_sublist))	

      marge_2 = self.merge(left_sorted_list, right_sorted_list)

      return(self.merge(merge_1, marge_2))



def main():
  my_list = [2,7,4,19,45,16,9,13,8,69,55,11,23,98,14,5,1,3,107,200, 2]

  # print("Add elements: ")
  # my_list = list(map(int, input().split()))

  print("\n\nThe input list is:  ", my_list)
  t0 = time.time()
  input_arr = MyArray(my_list)
  t1 = time.time()


  print("\nThe sorted list is: ", input_arr.sorted)
  print("Time taken: ", t1-t0, "seconds")

if __name__ == "__main__":
    main()
