#1
strings = ["Thirty", "Days", "Of", "Python"]
print(" ".join(strings))

#2
strings = ["Coding", "For", "All"]
print(" ".join(strings))

company = " ".join(strings)

print(company.lower())

print(company.swapcase())
print(company.capitalize())
print(company.title())
print(company[0:6])
print(company.find("Coding"))
print(company.index("Coding"))
print(company.replace("All", "Python"))
string = "Python for Everyone"
print(string.replace("Everyone", "All"))
print(string.split())
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle Amazon"
print(string.split(", "))
print(len("Coding For All.") - 1)
print(string[10])
string = "Coding For All"
print(string.index("C"))
print(string.index("F"))
print(string.index("l"))
print(string.rfind("l"))
string = "You cannot end a sentence with because because because is a conjunction"
print(string.index("because"))
print(string.find("because"))
print(string.rindex("because"))
#25
print(string.split(" because because because "))
#26
print(string.index("because"))
#28 Does ''Coding For All' start with a substring Coding?
print("Conding Frr All".startswith("Conding"))
#29 Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith("coding"))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("    Conding For All    ".strip(" "))

#31 Which one of the following variables return True when we use the method isidentifier(): 
# 30DaysOfPython 
# thirty_days_of_python

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
string = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(string))

print("You\t cannot end a sentence with\t because is a conjunction")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a cirvle with radius {radius} is {area} meters square")