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


