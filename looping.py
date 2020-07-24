x = 0

while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)


my_variable = 5

while my_variable < 10:
    print("Hello")
    my_variable += 1


x = 1
sum = 0

while x < 10:
    sum += 1
    x += 1
print("x is " +str(x) + " and sum is " + str(sum))

product = 1
while x < 10:
    product = product*x
    x += 1
print("x is " + str(x) + " and product is " + str(product))


def count_down(start_number):
    current = start_number
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")



count_down(3)

while x !=0 and x %2 ==0:
    x = x /2
    

def print_range(start, end):
    n = start -1
    while n < end:
        n += 1
        print(n)

print_range(1, 5) 

def print_prime_factors(number):
    factor = 2
    print ("Entering Prime Factors function")
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number = number / factor
        else:
            factor += 1
    return "Done"

print_prime_factors(100)


def is_power_of_two(n):
    print(" Entering power of two funtion")
    while n != 0 and n % 2 == 0:
        n = n / 2
    if n == 1:
        return True
    return False
  
print(is_power_of_two(0))

print("Entering sum of divisors")
def sum_divisors(n):
    div = 1
    sum = 0
    while div < n:
        if n % div == 0:
             sum = sum + div
        
        div += 1
        
    return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

def multiplication_table(number):
    	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number*multiplier 
		# What is the additional condition to exit out of the loop?
		if result >25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	


print ("For loop stuff ")

for x in range(5):
    print(x)
    
    
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum = sum + square(n)
    return sum
print(sum_squares(10))

values = [ 23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
    
print("Total sum: " + str(sum) + " - Average: " + str(sum/length))


product = 1
for n in range(1,10):
    product = product * n

print(product)


def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(4)) # should sreturn 24
print(factorial(5))

def to_celsius(x):
    return (x-32)*5/9

for i in range(0,101,10):
    print(x,to_celsius(x))
    