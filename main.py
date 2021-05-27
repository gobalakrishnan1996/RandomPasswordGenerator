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
Str = string.ascii_letters #this is for random words both caps & small

def main():
	for i in range(Numbers):
		rand_part = pad(random.randint(0, 99999) , 5) # this is for a random 5 numbers which are paded
		unique_part = pad(i, 2) # this is for a unique 2 numbers which are paded
		rand_str = (random.choice(Str))
		rand_char = (random.choice(Char))
		id = rand_part + str(rand_str) + str(rand_char) + unique_part # this is for a summation of them all
		print(id) #to get your unique passwords for the day

def pad(num, length): # this is to make sure numbers are padded to meet the 5 digit criteria

	num_string = str(num)
	while len(num_string) < length:
		# insert a 0 at the start of the string, increasing its length by one
		num_string = "0" + num_string
	return num_string

















if __name__ == "__main__":
	main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
