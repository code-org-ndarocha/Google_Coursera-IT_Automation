name = "Sasha"
color = 'gold'
pet = ""
colornew = color*3
len(colornew)

def double_word(word):
    return(str(word*2)+str(len(word*2)))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))


name = "Jaylen"
print(name[1])

def first_and_last(message):
    if message == "":
        return True
    elif message[0] == message[-1]:
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

color = "Orange"
print(color[1:4])

fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])

#strings in python are immutable

message = "A kong string with a typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

pets = "Cats & Dogs"
print(pets.index("&"))


print("Dragons" in pets)
print("Cats" in pets)


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + new_domain
        return new_email
    print(email)
    return email


#replace_domain(@gmail.com, gmail.com, yahoo.com)

print("Mountains".upper())
print("Mountains".lower())

answer = 'YES'
if answer.lower() == 'yes':
    print("User said yes")


print(" yes ".strip())
print(" yes ".lstrip())
print(" yes ".rstrip())

print("The number of times e occurs in this string is 4".count("e"))

print("Forest".endswith("rest"))

print("Forest".isnumeric())
print("12345".isnumeric())

print(int("12345") + int("12345"))

print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))

print("This is another example".split())

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result +=word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


#Formatting Strings

name = "Manny"
number = len(name)*3
print("Hello {}, your lucky number is {}".format(name,number))


test= "Nikhil Da Rocha".split()
res = ""
for i in test:
    print(i[0])
    


print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))


def student_grade(name, grade):
    	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


price = 7.5
with_tax = price*1.09
print(price, with_tax)

print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price,with_tax))

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:6.2F} C".format(x, to_celsius(x)))