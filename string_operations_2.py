#Counting substring from a string
#count()
#string.count(string)
s1 = "We are learning Python. Python is fun"
s2 = "Python"
print(s1.count(s2))
print(f"Occurances of {s2} is {s1.count(s2)}")

#Changing case of a string
#upper(), lower(), title(), captialize()

s3= "We are learning Python. Python is fun"
print(s3.upper())
print(s3.lower())
print(s3.title())
print(s3.capitalize())

# Starting and ending of a string

s4 = "We are learning Python"

# startswith()
# string.startswith(substring)

print(s4.startswith("W"))
print(s4.startswith("w"))
print(s4.endswith("Python"))
print(s4.endswith("n"))
