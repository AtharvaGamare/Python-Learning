name = "John"
age = 20
language = "Python"
hours = 3

# John is 20 years old. He studies Python 3 hours a day.
#print(name,"is", age, "years old. He studies",language,hours,"hours a day.")

# using f-string
print(f"{name} is {age} years old. He studies {language} {hours} hours a day.")

sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))
sub4 = int(input("Enter marks for Subject 4: "))

#print(f"{name} scored {sub1 + sub2 + sub3 + sub4}  marks in total out of 400. That is")

total = sub1 + sub2 + sub3 + sub4
percentage = total / 400 * 100
#print(percentage)
print(f"{name} scored {sub1 + sub2 + sub3 + sub4}  marks in total out of 400. That is {percentage} %.")
