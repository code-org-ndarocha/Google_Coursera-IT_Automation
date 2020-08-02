def group_list(group, users):
    members = []    
    for index, name in enumerate(users):
        members.append(name)
    # for name in users:
    #     members = name.append(group)
    #     print(members)
    print("{}: {}".format(group,members))

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"


def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    
    for i in [int(n) for n in str(octal)]:
        print(i)
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result += '-'
                
    print(result)    
print(octal_to_string(755)) # Should be rwxr-xr-x
#print(octal_to_string(644)) # Should be rw-r--r--
#print(octal_to_string(750)) # Should be rwxr-x---
#print(octal_to_string(600)) # Should be rw-------

def pig_latin(text):
    say = ""    
    words = text.split()
    for word in words:
        say += word[1:len(word)]+word[0] + "ay "
        
        
    return(say)
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def email_list(domains):
    emails = []
    for keys, values in domains.items():
     for i  in values:
         print(values, keys)
         emails.append(keys)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
