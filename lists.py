def skip_elements(elements):
    new_list = []
    i = 0
    for i in elements:
        
        if elements.index(i)%2 == 0:
            new_list.append(i)
        
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
#print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
#print(skip_elements([])) # Should be []

multiples = []
for i in range(1,11):
    multiples.append(i*7)
    
print(multiples)


multiples = [i*7 for i in range(1,11)]
print(multiples)

languages = ["Python", "Go", "Java", "Ruby", "C", "Erlang"]
lengths = [len(language) for language in languages]
print(lengths)


z = [x for x in range(0,101) if x%3 == 0]
print(z)


def odd_numbers(n):
    	return [x for x in range(1,n+1) if x%2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []