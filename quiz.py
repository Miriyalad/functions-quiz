def has_teen(a, b, c):

	if 13 <= a <=19:
		return True
	if 13 <= b <=19:
		return True
	if 13 <= c <=19:
		return True
	else: 
		return False


print has_teen(13, 15, 19)
print has_teen(11, 13, 17)
print has_teen(21, 23, 27)
print has_teen(17, 22, 25)

def not_string(str):
	if str[0:3] == "not":
		return str + "not"
	return "not" + str
print not_string("a joke")



def icy_hot(a, b):
	if a > 100 and b < 0:
		return True
	if a < 0 and b > 100:
		return True
	else: 
		return False
print icy_hot(100, 0)
print icy_hot(100, 0)
print icy_hot(101, -1)
print icy_hot(101, 12)
print icy_hot(10, 123)


def closer_to(a, b, c):
	guess1 = a - b
	guess2 = a - c
	if abs(guess1) > abs(guess2):
		return c
	if abs(guess1) < abs(guess2):
		return b
	if abs(guess1) == abs(guess2):
		return 0
print closer_to(321, 123, 234)
print closer_to(321, 323, 12)
print closer_to(321, 321, 321)
print closer_to(321, 319, 323)



def two_as_one(a, b, c):
	if a + b == c:
		return True
	if b + c == a:
		return True
	if a + c == b:
		return True
	else:
		return False
	
		
print two_as_one(1, 2, 3)
print two_as_one(1, 3, 2)
print two_as_one(3, 1, 2)
print two_as_one(3, 1, 56)


