#-------------------------------------------------------------------------------
# Name: Hyunsoo Im
# Project 3
# Due Date: 3/5/2019
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
# e-signed: Hyunsoo Im
#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

#have a counter start at 0 and add whenever theres a matching letter
def tally(letter, text):
	counter = 0
	for alphabets in text:
		if alphabets == letter:
			counter += 1
	return counter
#tally('z', 'sspoghdnskfugh')






def frequency(text): 
	alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	counter = 0
	empty = []
	for alph in alphabets: #has to go through the abc first because i have to return 26 things
		for letters in text: #checks if the alphabet in the abc matches the letter in text
			if alph == letters:
				counter += 1

		empty.append(counter) 
		counter = 0 #counter is set to 0 to reset the counter for each alphabets in the abc
		#this also will let me add the '0's in the empty list if it does not match the letter in the text

	return empty

#frequency('zoosarecool')





def common(frequencies):
	alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
	             'n','o','p','q','r','s','t','u','v','w','x','y','z']
	total = sum(frequencies) #my lab instructor said I could use 'sum' for this ***lab 228***	
	#if sum were not allowed,
	#total = 0
	#for nums in frequencies:
		#total = total + nums
	index = 0 #cant use .index so I'm making my own by starting at 0 and adding by 1 for each time it goes through the loop
	index_num_ten = []
	for num in frequencies:
		if num / total >= .1:
			index_num_ten.append(index) #now 'index_num_ten' should have the indexes of
		index += 1                      #frequencies where the letters occurs more than 10 percent of the total
	lis = []
	for indexes in index_num_ten:
		lis.append(alphabets[indexes])
	return tuple(lis)


#==================================section 2========================================

#def atbash_cipher(plaintext):
#	string = ''
#	for letters in plaintext:
#		if letters == 'a':
#			string += 'z'
#		elif letters == 'b':
#			string += 'y'
#		elif letters == 'c':
#			string += 'x'
#		elif letters == 'd':
#			string += 'w'
#		elif letters == 'e':
#			string += 'v'
#		elif letters == 'f':
#			string += 'u'
#		elif letters == 'g':
#			string += 't'
#		elif letters == 'h':
#			string += 's'
#		elif letters == 'i':
#			string += 'r'
#		elif letters == 'j':
#			string += 'q'
#		elif letters == 'k':
#			string += 'p'
#		elif letters == 'l':
#			string += 'o'
#		elif letters == 'm':
#			string += 'n'
#		elif letters == 'n':
#			string += 'm'
#		elif letters == 'o':
#			string += 'l'
#		elif letters == 'p':
#			string += 'k'
#		elif letters == 'q':
#			string += 'j'
#		elif letters == 'r':
#			string += 'i'
#		elif letters == 's':
#			string += 'h'
#		elif letters == 't':
#			string += 'g'
#		elif letters == 'u':
#			string += 'f'
#		elif letters == 'v':
#			string += 'e'
#		elif letters == 'w':
#			string += 'd'
#		elif letters == 'x':
#			string += 'c'		
#		elif letters == 'y':
#			string += 'b'
#		else:
#			string += 'a'
#	return string
#THIS DOESNT LOOK LIKE A HEALTHY CODE SO IMA TRY AGAIN********************8
def atbash_cipher(plaintext):
	string = ''
	alph =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	reverse_alph = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
	index = 0
	for letters in plaintext:
		index = 0
		for alphabets in alph:
			if letters == alphabets:
				string += reverse_alph[index]
			index += 1


	return string
#atbash_cipher('mynameisjeff')
#atbash_cipher('holamellamohyunsoo')
def caesar_cipher(plaintext, shift):
	string = ''
	empty_list = []
	alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for alphabets in plaintext:
		index = 0
		for letters in alph: #these will put the indexes of each letters in the alphabet in the list
			if alphabets == letters:
				empty_list.append(index)
			index += 1
	for indexes in empty_list: 
		while (indexes + abs(shift)) >= len(alph): #must be '>=' because the length of alphabet list is 26 while the max index in the alph is 25
			alph += alph  #if the shift plus the index of the letter is over 25, then it adds itself to itself
		string += alph[indexes + shift]       
	return string


#caesar_cipher("azbycx", -1) testing

def backwards_cipher(plaintext, key):
	index = 0
	new_string = ''
	string = ''
	#final = '' testing realized later i dont need this
	
	while index <= len(plaintext):
		string = string + plaintext[index:index + key]
		#print(string)
		my_index = 0 #reset my_index after it's gone through the nested loops
		for letter in string:
			new_string += string[my_index - 1]
			my_index -= 1



		#I tried doing this method but I didn't know how to reset my_index number
		#to 0 without giving me an error of being out of range..

		#while abs(my_index) <= key: 
		#	new_string += string[my_index]
		#	#print(new_string)
		#	my_index -= 1	
		#final += new_string
		#new_string = ''







		index = index + key
		string = '' #after it is added to the new_string, reset the 'string' 
		#print(string)
	return new_string
#backwards_cipher('lastweekisawafilm', 5)
	

#backwards_cipher('Hyunsooisacodinggodhahahahha', 5) self reminder :D jk testing
#backwards_cipher('abcdefghijklmnopqrs', 1) testingggggggg

def fence_cipher(plaintext):
	even = '' #just like the homework, i can create a string where only even number of indexes in that string goes in to and vice verse
	odd = ''
	final = ''
	index = 0 #my index counter
	for letters in plaintext:
		if index % 2 == 0:
			even += plaintext[index]
		else:
			odd += plaintext[index]
		index += 1
	final = even + odd #read from left to right
	#print(even)
	#print(odd)
	#print(final)
	return final

#fence_cipher('vivalavieboheme')

def column_cipher(plaintext):
	string = ''
	#make separate columns
	column_one = ''
	column_two = ''
	column_three = ''
	column_four = ''
	column_five = ''
	final = ''
	index = 0
	while index <= len(plaintext):
		string += plaintext[index: index + 5] #this will go through each string of 5 char and then 
											  #the next 5 characters
		
		#print()
		#print(string)
		if len(string) == 5:
			column_one += string[0]
			column_two += string[1]
			column_three += string[2]
			column_four += string[3]
			column_five += string[4]
		#print(len(string))
		#the remaining letters still has to be in on of the columns
		else:
			if len(string) == 4:
				column_one += string[0]
				column_two += string[1]
				column_three += string[2]
				column_four += string[3]
			elif len(string) == 3:
				column_one += string[0]
				column_two += string[1]
				column_three += string[2]
			elif len(string) == 2:
				column_one += string[0]
				column_two += string[1]
			elif len(string) == 1: #for some reason when i do 'else:', it gives me an error 
				column_one += string[0] #but this works 




		#add the index to move on to the next string of the next 5 characters in the text
		index += 5
		string = '' #reset to an empty string
	final = column_one + column_two + column_three + column_four + column_five
	return final
	#print()
	#print(column_one)
	#print(column_two)
	#print(column_three)
	#print(column_four)
	#print(column_five)
	#print(final)	



#column_cipher('hellomynameishyunsoopleasesubscribety')









