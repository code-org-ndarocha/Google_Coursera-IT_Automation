def greeting(name, department):
    print("Welcome " +name)
    print("You are part of " + department)
    
greeting("Kay", "CS")

def print_seconds(hours, minutes, seconds):
    print(60*60*hours+60*minutes+seconds)

print_seconds(1,2,3)


def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(6,7)

sum = area_a + area_b

print("The sum of the area is: " + str(sum))


def get_seconds(hours, minutes, seconds):
      return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    remaining_seconds = seconds - hours*3600 - minutes*60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)


def greet(name):
    print("Welcome" +name)
    
res = greet("Chris")

print(res)

def lucky_number(name):
    number = len(name)*9
    print("Hello " + name + " You're lucky number is " +str(number))
    
lucky_number("kay")
lucky_number("Cameroon")

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)
    
circle_area(10)

def rectangle_area(base,height):
      area = base*height
  print("The area is " + str(area))
  
rectangle_area(5,6)

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km*2))


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

def lucky_number(name):
      number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))