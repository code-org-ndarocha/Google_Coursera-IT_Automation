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
___ # Epilogue starts on page 39
___ # Chapter 3 now starts on page 24
___ # What are the current contents of the dictionary?
___ # Is there a Chapter 5?
toc["Epilogue"] = 39
toc["Chapter 3"] =24
print(toc)
print("Chapter 5" in toc)
