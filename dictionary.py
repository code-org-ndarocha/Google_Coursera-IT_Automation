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