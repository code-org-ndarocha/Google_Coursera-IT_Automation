x = {}
print(type(x))

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23 }
print(file_counts)

print(file_counts["txt"])

print("jpg" in file_counts)

print("html" in file_counts)

file_counts["cfg"] = 8
print(file_counts)

file_counts["csv"] = 17
print(file_counts)

del file_counts["cfg"]
print(file_counts)


toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}

toc["Epilogue"] = 39
toc["Chapter 3"] =24
print(toc)
print("Chapter 5" in toc)


file_nos = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_nos:
    print(extension)


for ext, amount in file_nos.items():
    print("There are {} files with the .{} extension".format(amount,ext))
    
    
print(file_nos.keys())
print(file_nos.values())

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for keys, values in cool_beasts.items():
    print("{} have {}".format(keys, values))
    
    
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
        
    return result

print(count_letters("aaaaa"))


wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item, values in wardrobe.items():
    #print(values, item)
    for i in values:
        print(i , item)
        
        

print("Set!")


def email_list(domains):
    emails = []
    for keys, values in domains.items():
        for i  in values:
            emails.append(i + "@" + keys)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


def groups_per_user(group_dictionary):
    user_groups = {}
    for keys, values in group_dictionary.items():
        for i in values:
            if i in user_groups:
                user_groups[i].append(keys)
            else:
                user_groups[i] = [keys]
             
print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)



def add_prices(basket):
    	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for keys, values in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += values
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44