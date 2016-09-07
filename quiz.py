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




def icy_hot(a, b, c):
	if a < 0:
		return True
	if b > 100:
		return True
	if c > 100 or c < 0:
		return True
	else:
		return False
print icy_hot(1, 2, 3)
print icy_hot(100, 200, 300)


def closer_to(a):
	
	if a > 5:
		return True
	if a < 5:
		return False
	
print closer_to(5)
print closer_to(9)
print closer_to(15)



def two_as_one(a, b, c):
	if a + b > c:
		return True
	if a + c > b:
		return True
	if b + c > a:
		return False
	
		
print two_as_one(1, 2, 3)
print two_as_one(2, 4, 6)
print two_as_one(1, 3, 7)
print two_as_one(1, 2, 4)


