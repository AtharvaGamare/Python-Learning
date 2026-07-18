"Strings as we know so far"

s1 = "Hello World"
print(s1)
"""
# length of the string
print(len(s1))

# Indexing
print("First Char", s1[0])
print("Last Char", s1[-1]) """

#Slicing in Strings - technique that programmers use to access a part of a string
"""
Syntax of Indexing - string[index]
Syntax of Slicing - string[start:end:step]
- start :- starting index at which the slicing operation starts
- end :- ending index at which the slicing stops(excluded)
- step :- integer that specifies the step for slicing
"""
print(s1[2:7:1])
print(s1[2:9:2])
print(s1[1:15:3])
s1_slice = s1[1:15:3]
print(s1_slice)
print(type(s1_slice))