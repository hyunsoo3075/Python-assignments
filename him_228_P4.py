#-------------------------------------------------------------------------------
# Name: Hyunsoo Im
# Project 4
# Due Date: 04/01/2019
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
# Hyunsoo Im
#-------------------------------------------------------------------------------
# References: (list resources used - remember, projects are individual effort!)
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

def init_empty_cells(width, height):
	lists = []
	if width <= 0 or height <= 0: #if its 0 and neg (cannot happen) just return an empty bracket
		return lists
	for nums in range(height): #add a nested list in lists
		lists.append([])
	index = 0
	while index < height: #adds a nested element into the nested list
		for num in range(width):
			lists[index].append(0)
		index += 1
	return lists

#init_empty_cells(0,0)
def copy(cells):
	copy = cells
	new_copy = []
	for elements in copy:
		new_copy.append([])  #adds a new nested list in the new copy for every nested loop in cells
	index = 0
	while index < len(copy):
		for element in copy[index]:
			new_copy[index].append(element) #same for here but elements in the nested list appended
		index += 1
	return new_copy

#copy([[0,0,1], [1,1,0]])
def is_valid(row, column, cells):
	if row < 0 or column < 0:
		result = False
	elif row >= len(cells) or column >= len(cells[0]): #using the first elemenet as a parameter bc all rows have the same num of cols
		result = False
	else:
		result = True
	
	
	#rint(result)
	return result
#is_valid(0,0,[[0,0,0], [0,0,0]])
#is_valid(3,3,[[0,0,0], [0,0,0]])
#is_valid(-1,0,[[0,0,0], [0,0,0]])
#is_valid(3, 5, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

def toggle_cell(row, column, cells):
	if is_valid(row, column ,cells) == False:
		result = False
	else:

		cells_copy = copy(cells) #calling my previous function to later check if its been altered or not
		dead = 0 #checking if its a 0 or 1
		alive = 1
		if row < 0 or column < 0:
			result = False
		elif len(cells[0]) <= row or len(cells[0]) <= column:
			result = False
		elif row < 0 or column < 0:
			result = False
		else:
			if cells[row][column] == dead: #check if its alive or dead in that specific given row, col
				cells[row][column] = alive
				if cells == cells_copy:
					result = False #if its not changed, return false
				elif cells != cells_copy:#else return true
					result = True
			elif cells[row][column] == alive: 
				cells[row][column] = dead
				if cells == cells_copy:
					result = False
				elif cells != cells_copy:
					result = True


	#print(result)
	#print(cells)
	return result


#toggle_cell(1, 4, [[1,1,1,1],[1,1,1,1]])
#toggle_cell(-1,0, [[1,1],[1,1]])
def set_pattern(shape, row, column, cells): 
	#check if its a valid row/col first
	if is_valid(row, column, cells) == False:
		return False
	else:
		#assign shapes into different given examples in the beginning so the program can shift each 
		#elements by num of row/col in the given 'cells'
		if shape == 'block':
			shapes = [[1, 1, 0],[1, 1, 0],[0, 0, 0]]
		elif shape == 'blinker':
			shapes = [[0, 1, 0],[0, 1, 0],[0, 1, 0]]
		elif shape == 'glider':
			shapes = [[0, 1, 0],[0, 0, 1],[1, 1, 1]] 
		elif shape == 'bigblock':
			shapes = [[1, 1, 1],[1, 1, 1],[1, 1, 1]]
		else:
			shapes = [[0, 1, 1],[1, 1, 0],[0, 1, 0]]
		indexes = 0
		#Im checking rows first (because col is a 2d list)
		while indexes < len(shapes):
			extra_row = 0 #reset it every time it goes through the loop
			if indexes + row >= len(cells): #if it goes out of bound, it will go back to the remainder (modulo)
				extra_row = (indexes + row) % (len(cells))
			else: #if that cell in the shapes is not out of bound, it will just shift
				extra_row = indexes + row
			for c in range(len(shapes[0])):
				extra_col = 0 #same algorithm for column
				if c + column >= len(cells[row]):
					extra_col = (c + column) % (len(cells[row]))
				else:
					extra_col = c + column
				cells[extra_row][extra_col] = shapes[indexes][c]
				#print(extra_row)
				#print(extra_col)
				#print(indexes)
				#print(c)
			indexes += 1

	return cells

#set_pattern('bigblock', 3, 3, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

#set_pattern("block",0,0,[[0,0,0], [0,0,0], [0,0,0]])

#neighbors is a bit confusing one where i cannot figure out the algorithm in a way where i use loops to check neighbors
#because there are many ways a neighbor's index can be out of limit. for examples, there are neighbors that have the indexes
#less than 0 and neighbors that have indexes over max rows. These two will not have the same conflict of neighbors going over
#bound in same directions so i just decided to do it one by one
def count_neighbors(cells, row, col):
	neighbor_count = 0
	if is_valid(row, col, cells) == False:
		return -1
	else:
		neighbor_count = 0
		if (row + 1 >= len(cells)) and (col + 1) >= len(cells[0]): #bottom right
			if cells[row - 1][col - 1] == 1: #left top neighbor
				neighbor_count += 1
			if cells[row - 1][col] == 1:     #up neighbor
				neighbor_count += 1
			if cells[row - 1][0] == 1:		 #right top neighbor
				neighbor_count += 1
			if cells[row][col - 1] == 1:	 #left neighbor
				neighbor_count += 1
			#skip the actual given point
			if cells[row][0] == 1:			 #right neighbor
				neighbor_count += 1
			if cells[0][col - 1] == 1:		 #bottom left neighbor
				neighbor_count += 1
			if cells[0][col] == 1:			 #bottom neighbor
				neighbor_count += 1
			if cells[0][0] == 1:			 #bottom right neighbor
				neighbor_count += 1
		elif (row - 1 < 0) and (col - 1 < 0): #top left
			if cells[len(cells) - 1][len(cells[0]) - 1] == 1:
				neighbor_count += 1
			if cells[len(cells) - 1][col] == 1:
				neighbor_count += 1
			if cells[len(cells) - 1][col + 1] == 1:
				neighbor_count += 1
			if cells[row][len(cells[0]) - 1] == 1:
				neighbor_count += 1
			#skip the actual given point
			if cells[row][col + 1] == 1:
				neighbor_count += 1
			if cells[row + 1][len(cells[0]) - 1] == 1:
				neighbor_count += 1
			if cells[row + 1][col] == 1:
				neighbor_count += 1
			if cells[row + 1][col + 1] == 1:
				neighbor_count += 1			
		elif (row + 1 < len(cells)) and (col + 1) >= len(cells[0]): #right 
			if cells[row - 1][col - 1] == 1:
				neighbor_count += 1
			if cells[row - 1][col] == 1:
				neighbor_count += 1
			if cells[row - 1][0] == 1:
				neighbor_count += 1
			if cells[row][col - 1] == 1:
				neighbor_count += 1
			#skip the actual given point
			if cells[row][0] == 1:
				neighbor_count += 1
			if cells[row + 1][col - 1] == 1:
				neighbor_count += 1
			if cells[row + 1][col] == 1:
				neighbor_count += 1
			if cells[row + 1][0] == 1:
				neighbor_count += 1
			#only col overloads
		elif (row + 1 >= len(cells)) and (col + 1 < len(cells[0])): #bottom
			if cells[row - 1][col - 1] == 1:
				neighbor_count += 1
			if cells[row - 1][col] == 1:
				neighbor_count += 1
			if cells[row - 1][col + 1] == 1:
				neighbor_count += 1
			if cells[row][col - 1] == 1:
				neighbor_count += 1
			#skip the actual given point
			if cells[row][col + 1] == 1:
				neighbor_count += 1
			if cells[0][col - 1] == 1:
				neighbor_count += 1
			if cells[0][col] == 1:
				neighbor_count += 1
			if cells[0][col + 1] == 1:
				neighbor_count += 1
			#only row overloads
		elif (row - 1 >= 0) and (col - 1 < 0): #left
			if cells[row - 1][len(cells[0]) - 1] == 1:
				neighbor_count += 1
			if cells[row - 1][col] == 1:
				neighbor_count += 1
			if cells[row - 1][col + 1] == 1:
				neighbor_count += 1
			if cells[row][len(cells[0]) - 1] == 1:
				neighbor_count += 1
			#skip the actual given point
			if cells[row][col + 1] == 1:
				neighbor_count += 1
			if cells[row + 1][len(cells[0]) - 1] == 1:
				neighbor_count += 1
			if cells[row + 1][col] == 1:
				neighbor_count += 1
			if cells[row + 1][col + 1] == 1:
				neighbor_count += 1
		elif (row - 1 < 0) and (col - 1 >= 0): #top
			if cells[len(cells) - 1][col - 1] == 1:
				neighbor_count += 1
			if cells[len(cells) - 1][col] == 1:
				neighbor_count += 1
			if cells[len(cells) - 1][col + 1] == 1:
				neighbor_count += 1
			if cells[row][col - 1] == 1:
				neighbor_count += 1
			#skip the actual given point
			if cells[row][col + 1] == 1:
				neighbor_count += 1
			if cells[row + 1][col - 1] == 1:
				neighbor_count += 1
			if cells[row + 1][col] == 1:
				neighbor_count += 1
			if cells[row + 1][col + 1] == 1:
				neighbor_count += 1
		else: #theres no overlapping going on
			if cells[row - 1][col - 1] == 1:
				neighbor_count += 1
			if cells[row - 1][col] == 1:
				neighbor_count += 1
			if cells[row - 1][col + 1] == 1:
				neighbor_count += 1
			if cells[row][col - 1] == 1:
				neighbor_count += 1
			#skip the actual given point
			if cells[row][col + 1] == 1:
				neighbor_count += 1
			if cells[row + 1][col - 1] == 1:
				neighbor_count += 1
			if cells[row + 1][col] == 1:
				neighbor_count += 1
			if cells[row + 1][col + 1] == 1:
				neighbor_count += 1
		return neighbor_count
		#print(neighbor_count)

#count_neighbors([[0,1,0,0],[0,1,0,1],[1,1,0,1]],2,1)
#count_neighbors([[0,0,0],[0,1,0],[0,0,0]],2,2)
#count_neighbors([[0,0,0],[0,1,0],[0,0,0]],-1,1)

def reflect(cells, axis):
	new_list = [] #i have to return a new list
	if axis == 'y': #ONLY CHANGING THE COLUMN 
		index = 0
		while index < len(cells): #since no .index() is allowed, this is how i go through each element
			inverse_num = len(cells[0]) - 1	 #i ned to go inside the nested list and find the index 
			new_list.append([])		#add nested loop every time after the amount
			for col in range(len(cells[0])): #i need to know the num of indexes in cells[0] (as an example) to append that amount into 
											 #the nested list
				new_list[index].append(cells[index][inverse_num]) #the 'index' will be valid bc im adding a new list every time before this line 
																  #approaches
				#print(new_list)


				inverse_num -= 1
			index += 1	
	else:
		index = 0
		inverse_num = len(cells) - 1 #now this is going to be the 'row' so it needs to be outside the while loop
		while index < len(cells):
			new_list.append([])		
			for row in range(len(cells[0])):
				new_list[index].append(cells[inverse_num][row]) #row will be 0,1,2,3... and 
																#reset until num of elements in nested index is reached
				#print(new_list)
			inverse_num -= 1
			index += 1
	return new_list
	#print(new_list)		

#reflect([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]], 'x')

def invert(cells):
	#no need to return anything
	#but use the same nested loops from before to approach each elements
	index = 0
	while index < len(cells):
		for elements in range(len(cells[index])):
			if cells[index][elements] == 0: #check if the cell is alive or dead
				cells[index][elements] = 1
			else:
				cells[index][elements] = 0
			#print(cells)



		index += 1
	#return cells
	# i dont need to return or print anything bc it should automatically change the cells
	#print(cells)

#invert([[0,1,0,1,1],[1,1,0,1,0],[1,1,0,0,1],[0,0,1,0,1],[0,0,1,1,1],[1,1,1,1,1]])


def translate(cells, direction):
	new_list = []
	if direction == 'right' or direction == 'left':
		if direction == 'right': #get the previous col
			index = 0
			while index < len(cells):
				new_list.append([])

				for col in range(len(cells[0])): 
					#if col + 1 >= len(cells[0]) - 1: #plus one for col because we are moving right by 1
					#	new_list[index][0:0] = cells[index][col - 1]
					#else:
					new_list[index].append(cells[index][col - 1]) #i dont have to do any if statement bc if the index is -1, 
																  #then it will automatically go to the end of the list
				index += 1
		else: #left GET THE NEXT COLUMN AND ADD IT ON TO THE NEW LIST 
			index = 0
			while index < len(cells):
				new_list.append([])
				for col in range(len(cells[0])):
					if col + 1 >= len(cells[0]): #IF it overlaps the limit, then get the next one(which would be 0)
						new_list[index].append(cells[index][0]) 
					else:
						new_list[index].append(cells[index][col + 1]) #getting next list
				index += 1
	else:
		if direction == 'down':
			index = 0
			while index < len(cells):
				new_list.append([])
				for col in range(len(cells[0])):
					new_list[index].append(cells[index - 1][col]) #same as 'right' since im getting the previous row,
																  #i can just do -1 and it will automatically go at the end of list
				index += 1
		else:
			index = 0
			while index < len(cells):
				new_list.append([])
				for col in range(len(cells[0])):
					if index + 1 >= len(cells):
						new_list[index].append(cells[0][col]) #append cells[0][#] just like 'left'
					else:
						new_list[index].append(cells[index + 1][col])


				index += 1







	return new_list
	#print(new_list)
	#print(cells)
#translate([[0,0,0,0,0],[1,2,3,4,5],[0,0,0,0,0]], "down") 


def update(cells):
	new_list = []
	row = 0
	while row < len(cells):

		new_list.append([])
		for col in range(len(cells[0])):
			if cells[row][col] == 0: #checks if it's alive or not
				if int(count_neighbors(cells, row, col)) == 3:
					new_list[row].append(1)
				else:
					new_list[row].append(0) #if it doesnt, then it continues to be dead
			else: #alive
				if int(count_neighbors(cells, row, col)) < 2: #underpopulation
					new_list[row].append(0)
				elif int(count_neighbors(cells, row, col)) > 3: #overpopulation
					new_list[row].append(0)
				else:
					new_list[row].append(1) #it's gon have 2 or 3 neighbors

		row += 1
	#print(new_list)
	return new_list

#update([[0,0,0,0],[0,1,1,0],[0,0,0,0],[1,0,0,0]])








		

