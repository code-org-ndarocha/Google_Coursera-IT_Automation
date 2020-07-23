def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be atleast 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be atmost 15 characters long.")
    else:
        print("Valid username")
        
hint_username("mc")
hint_username("test")

def is_positive(number):
    if number > 0:
        return True
    else:
        return False
   
    
is_positive(3)

def is_even(number):
    if number % 2 == 0:
        return True
    return False

def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    
number_group(45)


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks =  block_size // filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size % filesize
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size*2
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"
    else:
        return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))