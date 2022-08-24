"""example memory diagram."""

age: int = int(input("how old are you? "))
year: int = int(input("what year is it? "))
age_in_2041: int = 2041 - year + age
print("in 2041, you'll be " + str(age_in_2041))

age = age + 1
year = year + 1
print("in " + str(year) + ", you'll be " + str(age))