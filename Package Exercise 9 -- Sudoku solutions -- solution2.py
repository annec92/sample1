#Solution 2 -- program to check whether a given Sudoku solution is valid

board_list = [[" " for x in range(9)] for y in range(9)]
value_list1 = [1,2,3,4,5,6,7,8,9]

board_index_map = {1:[(0,0), (0,1), (0,2),
                      (1,0), (1,1), (1,2),
                      (2,0), (2,1), (2,2)],
                   2: [(0,3), (0,4), (0,5),
                       (1,3), (1,4), (1,5),
                       (2,3), (2,4), (2,5)],
                   3: [(0,6), (0,7), (0,8),
                       (1,6), (1,7), (1,8),
                       (2,6), (2,7), (2,8)],
                   4: [(3,0), (3,1), (3,2),
                       (4,0), (4,1), (4,2),
                       (5,0), (5,1), (5,2)],
                   5: [(3,3), (3,4), (3,5),
                       (4,3), (4,4), (4,5),
                       (5,3), (5,4), (5,5)],
                   6: [(3,6), (3,7), (3,8),
                       (4,6), (4,7), (4,8),
                       (5,6), (5,7), (5,8)],
                   7: [(6,0), (6,1), (6,2),
                       (7,0), (7,1), (7,2),
                       (8,0), (8,1), (8,2)],
                   8: [(6,3), (6,4), (6,5),
                       (7,3), (7,4), (7,5),
                       (8,3), (8,4), (8,5)],
                   9: [(6,6), (6,7), (6,8),
                       (7,6), (7,7), (7,8),
                       (8,6), (8,7), (8,8)]}

def rows_complete(): #iterates through each list in the grid (the grid is an array of lists arranged in rows). iterates through values in a list enumerating numbers 1 to 9, check that the number exists in the list
    for x in range(0,9): #iterates through the rows in the board, checks for each row that all the values from the value list are in them
        for check_val in value_list1:
            #print("In the rows_complete() function, checking row 2, the selected row is: ", board_list[x])
            #print("The current value being checked is ", check_val)
            if(check_val not in board_list[x]):
                return False
    return True

def columns_complete(): #collects values in each column into a list. iterates through values in a list enumerating numbers 1 to 9, check that the number exists in among the collected values
    column_incomplete = False
    #collected_values1 = [board_list[x][y] for x in range(9)]

    for y in range(0,9):
        #collected_values1 = []
        #for x in range(9):
        #    collected_values1.append(board_list[x][y])
        collected_values1 = [board_list[x][y] for x in range(9)]
        
        for check_val in value_list1:
            if (check_val not in collected_values1):
                return False
    return True

def check_element_unique_to_board(board_index): #given the index of the board, collects values in the mapped indices, iterates through each value, and checks that it is unique to the list
    board_indices = board_index_map[board_index]
    list1 = [board_list[x][y] for x,y in board_indices] 
    #for x, y in board_indices:
    #    list1.append(board_list[x][y])
    #from list of collected elements, check that each element does not occur more than once
    for element1 in list1:
        count_list = ["x" for temp in list1 if temp == element1]
        if len(count_list) > 1:
            return False
    return True

def check_element_unique_to_row(x,y):#can be modified so it accepts x and y coordinates of each element, and checks if it is unique to its row
   list1 = board_list[x] #accesses the xth row in the grid
   #print("The returned list is ", list1)
   element1 = board_list[x][y]      
   count_list = ["x" for temp in list1 if temp == element1] 
   if(len(count_list)>1):
      return False
   return True

def check_element_unqiue_to_column(x,y):#needs to be written so it returns a value only after all the columns are checked
   list1 = [board_list[i][y] for i in range(9)] #collects all the values in the column the element belongs to
   element1 = board_list[x][y]
   count_list = ["x" for temp in list1 if temp==element1]
   print("The returned list is ", list1)
   if(len(count_list) > 1):
      return False
   return True

def populate_grid():
#295743861
#431865927
#876192543
#387459216
#612387495
#549216738
#763524189
#928671354
#154938672

#195743862
#431865927
#876192543
#387459216
#612387495
#549216738
#763524189
#928671354
#254938671

  # list1 = [[2,9,5,7,4,3,8,6,1],
  #          [4,3,1,8,6,5,9,2,7],
  #          [8,7,6,1,9,2,5,4,3],
  #          [3,8,7,4,5,9,2,1,6],
  #          [6,1,2,3,8,7,4,9,5],
  #          [5,4,9,2,1,6,7,3,8],
  #          [7,6,3,5,2,4,1,8,9],
  #          [9,2,8,6,7,1,3,5,4],
  #          [1,5,4,9,3,8,6,7,2]]
   list1 = [[1,9,5,7,4,3,8,6,2],
            [4,3,1,8,6,5,9,2,7],
            [8,7,6,1,9,2,5,4,3],
            [3,8,7,4,5,9,2,1,6],
            [6,1,2,3,8,7,4,9,5],
            [5,4,9,2,1,6,7,3,8],
            [7,6,3,5,2,4,1,8,9],
            [9,2,8,6,7,1,3,5,4],
            [2,5,4,9,3,8,6,7,1]
            ]
   #for x in range(9):
      #print("Currently accepting values for row ", x)
   for y in range(9):
         #int1 = int(input("Please enter a value: "))
         board_list[y] = list1[y]
      

def run_check():
   #rows_complete() # check 1: the rows in the given solution are complete
   bool_rows_complete = rows_complete()
   print("Rows complete run successfully, and returned ", bool_rows_complete)
   bool_columns_complete = columns_complete()
   print ("Columns complete run successfully and returned ", bool_columns_complete) # check 2: the columns in the given solution are complete
   elements_unique_to_board = True 
   for i in range(1, 10):
      elements_unique_to_board = check_element_unique_to_board(i)
      if (elements_unique_to_board == False):
         break #iterates through the indices for each board, gets the corresponding coordinates for values in the grid, and checks that that element is unqiue to the board
   
   print("Elements unique board run successfully and returned ", elements_unique_to_board)
   elements_unique_to_row = True 

   for x in range(0,9):
      if(elements_unique_to_row == False):
         break
      for y in range(0, 9):
         elements_unique_to_row = check_element_unique_to_row(x,y) # iterates through elements in the grid, checks that each element is unique to its row
         if(elements_unique_to_row == False):
            break
   print ("Elements unique to row run successfully and returned ", elements_unique_to_row)
  
   elements_unique_to_column = True

   for x in range(0,9):
      if (elements_unique_to_column == False):
         break 
      for y in range(0,9):
         elements_unique_to_column = check_element_unqiue_to_column(x,y) # iterates through the elements in the grid, checks that each element is unique to its column        
         if(elements_unique_to_column == False):
            break
   print("Elements unique to column run successfully and returned ", elements_unique_to_column)
   if(columns_complete and rows_complete and elements_unique_to_board and elements_unique_to_row and elements_unique_to_column):
      return True
   return False

def print_grid():
  for i in range(9):
      print(board_list[i])

populate_grid()
print_grid()
if (run_check()):
   print("The provieded solution is valid")
else:
   print("The solution provided is not valid")

