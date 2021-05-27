# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#random password generator
"""
In this day and age people are struggling to find a unique password to keep them safe.
so I created this random unique passwords for your use.
you can start your day by changing all your passwords with this unique one and change them at the end of day.
"""
import random
import string

Numbers = 15 #Number of passwords for your reference
Char = string.punctuation #this is for random punctuations
Str1 = string.ascii_lowercase #this is for random lowercase
Str2 = string.ascii_uppercase # this is for random uppercase

def main():
	for i in range(Numbers):
		rand_part = pad(random.randint(0, 99999) , 5) #random 5 digit number
		unique_part = pad(i, 2) #unique 2 numbers
		rand_str1 = (random.choice(Str1)) #for one random lower letter word
		rand_str2 = (random.choice(Str2)) # for one random upper letter word
		rand_char = (random.choice(Char)) # for one random punctuation
		id = rand_part + str(rand_char) + str(rand_str1) + unique_part + str(rand_str2) # this is done to stragerically place them in a unique way
		print(id) # to get your unique passwords for the day

def pad(num, length):   # this is to make sure numbers are padded to meet the 5 digit criteria

	num_string = str(num)
	while len(num_string) < length:
		# insert a 0 at the start of the string, to make sure it's padded
		num_string = "0" + num_string
	return num_string


#A Program by Gobalakrishnan














if __name__ == "__main__":
	main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
