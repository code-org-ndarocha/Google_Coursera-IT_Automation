#Tuples are sequences of elements of any type that are immmutable

fullname = ('Grace', 'M', 'Hopper')
print(fullname)

#positions of elements used in a tuple have meaning

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours*3600 -minutes*60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
print(result)
print(type(result))
hours, minutes, seconds = result
print(hours, minutes, seconds)

hours, minutes, seconds = convert_seconds(4000)
print(hours, minutes, seconds)

def file_size(file_info):
    name, file_type, size= file_info
    return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


#Iteration over lists and tuples
print("Iteration over lists and tuples")

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:    
    chars += len(animal)
    
    
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

winners = ["Ashley", "Dylan", "Reese"]

for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


def skip_elements(elements):
    new_list = []
    for index, alphabet in enumerate(elements):
        if index%2 == 0:
            new_list.append(alphabet)
    return new_list
    

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@example.com","Alex Diego"), ("shay@example.com", "Shay Brandt")]))
    
