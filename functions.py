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