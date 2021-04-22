# Strings 


string1 = 'abc'
string2 = "ABCDE"
string3 = "12345"

print(string1)
print(len(string1))		# prints the length of the string 

number = 654321
print(type(number))		# integer 
# convert number into string 
number = str(number)	
print(len(number))			
print(type(number))		# type string 

print("A" > "B")
print("a" < "b")		# alphabetically ... 
print("a" > "A")		# lower cases are larger in value 

print("abc" + "def")
print("abc" * 3)

print("ab" in string1)		# true because 'ab' is inside 'abcde'
print("AB" in string1)		# false because 'AB' is NOT inside 'abcde'
print("ring" in "string")
print("ac" in string1)		# order matters... 

print("---------------------------------------------------------")
# indexing 
print(string1)			# abcde
print(string1[0])		# a 
print(string1[1])		# b
print(string1[2])		# c 
print(string1[4])		# e 
#print(string1[5])		# IndexError: string index out of range 

print(string1[-1])		# e ---> first index from the right 

print(string1[0:3])		# from 0th to 3rd (excluded) index --> abc 
print(string1[1:4])		# bcd 

print(string1[2: ])		# from the 2nd index ~ till the end 
print(string1[ :4])		# abcd
print(string1[ : ])		# prints everything

print(string1[::2])		# increments by 2 
print(string1[::3])		# increments by 3 
print(string1[::-1])	# reverse .... --> edcba 


########################################################################3
s = "abcde"	
s2 = "12345"
s3 = "ABCDE"
s4 = "ab3de"
s5 = "                abcde           "

print(s.isalpha())		 # composed of only alphabets.. True 
print(s4.isalpha())		# false, because of 3 
print(s2.isdigit())		# composed of only digits? 
print(s3.isupper())		# uppercase only? 
print(s.islower())		# lowercase only? 

print(s.replace('c', "z"))		# abzde

s6 = "I am a boy!"

print(s6.count('a'))		# counts a 
print(s6.find('a'))			# returns the index # of the character a. Only cares about the first occurence 






print("=========================================")
string = "I am a b        oy"














