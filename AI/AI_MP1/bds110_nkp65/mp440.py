
'''
GCD algorithm
'''
def gcd(a, b):
    if a<b:
        c = a
        x = b
        y = c
    else:
        x = a
        y = b

    while y!=0:
        r = x%y
        x = y
        y = r
    return x

'''
Rectangles on a rubik's cube
'''
def rubiks(n):
    if n <= 0:
        return None
    sideCount = (n*(n+1)*n*(n+1))/4
    cubeCount = sideCount*6
    return cubeCount


'''
Guessing a number
'''
def guess_unlimited(n, is_this_it):
    # The code here is only for illustrating how is_this_it() may be used 
    guess = 1
    while(is_this_it(guess)!= True):
        guess=guess+1
    return guess
        
'''
Guessing a number where you can only make two guesses that are larger
'''
def guess_limited(n, is_this_smaller):
	larger = 0
	min = 1
	max = n
	answer = 0
	while(larger<1 and max-min>1):
		guess = (min+max)/2
		if(is_this_smaller(guess)!=True):
			larger = larger+1
			max = guess
		else:
			min = guess
	if(max-min<=1):
		if(is_this_smaller(min)):
			answer=max
		else:
			answer=min
	else:
		while(larger<2 and min!=max):
			guess=min
			if(is_this_smaller(guess)!=True):
				larger = larger+1
				answer = guess
			else:
				min = min+1
				answer = min
	return answer
        
'''
Guessing a number, bonus problem
'''
def guess_limited_plus(n, is_this_smaller):
	min=1
	max=n
	answer=0
	while(max-min>1):
		guess = (min+max)/2
		if(is_this_smaller(guess)!=True):
			max = guess
		else:
			min = guess
	if(is_this_smaller(min)):
		answer=max
	else:
		answer=min
	return answer