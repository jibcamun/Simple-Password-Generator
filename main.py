import random

try:
	num_chars = int(input("Please enter number of characters that must be present (default 4): "))

	if num_chars < 4:
		print("Number of characters must be at least 4. Setting to default value of 4.")
		num_chars = 4
	else:
		print(f"Number of characters set to {num_chars}.")
except:
	print("Setting number of characters to default value of 4.")
	num_chars = 4

def pick_char(chars):
	return random.choice(chars)

alphabets_caps = ['A', 'B', 'C', 'D', 'E',
				'F', 'G', 'H', 'I', 'J',
				'K', 'L', 'M', 'N', 'O',
				'P', 'Q', 'R', 'S', 'T',
				'U', 'V', 'W', 'X', 'Y', 'Z']

alphabets_low = ['a', 'b', 'c', 'd', 'e',
				'f', 'g', 'h', 'i', 'j',
				'k', 'l', 'm', 'n', 'o',
				'p', 'q', 'r', 's', 't', 
				'u', 'v', 'w', 'x', 'y', 'z']

special_chars = ['!', '@', '#', '$', '%'
				'^', '&', '*', '(', ')',
				'-', '_', '=', '+', '{',
				'}', '[', ']', ':', ';',
				'"', "'", '<', '>', '?',
				'/', '|', '~']

numbers = ['0', '1', '2', '3', '4',
		   '5', '6', '7', '8', '9']

password = ""

for i in range(num_chars):
		if i % 4 == 0:
			password += pick_char(alphabets_caps)
		elif i % 4 == 1:
			password += pick_char(alphabets_low)
		elif i % 4 == 2:
			password += pick_char(special_chars)
		else:
			password += pick_char(numbers)


print(f"Password: {password}")