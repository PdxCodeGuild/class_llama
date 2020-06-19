
def int_list(card_number):
	
	card_number = card_number.split()
	for i in range(len(card_number)):
		card_number[i] = int(card_number[i])
	return card_number

def double_number(card_number_list):
	
	for i in range(0,len(card_number_list),2):
		card_number_list[i] *= 2
	return card_number_list

def second_num(number):
	
	return int(list(str(number))[1])


def print_valid(x, y):
	
	if x == y:
		print('Valid number')
	else:
		print('Invalid number')

def card_validation(card_number):
	"""
	>>> card_validation('4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5')
	Valid number
	"""
	card_number = int_list(card_number)
	check_digit = card_number.pop()
	card_number.reverse()
	card_number = double_number(card_number)
	print_valid(second_num, check_digit)





















