"""Calculate area of triangle
Semi perimeter (s) = (a + b + c) / 2
Area = square root of (s * (s - a) * (s - b) * (s - c))"""

"""a = float(input("Enter the First side: "))
b = float(input("Enter the Second side: "))
c = float(input("Enter the Third side: "))

s = (a + b + c) / 2
print(s)

Area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of the Triangle:",round(Area, 2))"""

"""Calculate Simple Interest
Formula = (P*R*T)/100
P = Principle Amount, R = Rate of Interest, T = Time Duration"""

"""principle = float(input("Enter Principle Amount: "))
roi = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time Duration: "))

Simple_Interest = (principle * roi * time) / 100
print("Calculated Simple Interest",Simple_Interest)"""

"""Calculate Compound Interest
P = Principle Amount, R = Rate of Interest, T = Time Duration
Amount(A) = P(1 + (R/100)) ** T
Compound Interest = A - P"""

p = float(input("Enter Principle Amount: "))
roi = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time Duration: "))
Amount = p * (1 + roi/100) ** t
print("Total Amount:", round(Amount, 2))
compound_interest = Amount - p
print("Compound Interest: ", round(compound_interest, 2))