import math

first_name = 'Duy'
last_name = 'Nguyen'
full_name = 'Nguyen Van Duy'
country = 'HCM'
city = 'Di An'
age = 23
year = 2023
is_married = False
is_true = True
is_light_on = True
skill = ['C3', 'java', 'python', 'html']
person_info = {
    'firts_name':'Duy',
    'last_name':'Nguyen',
}

print('first_name', first_name)
print('last_name', last_name)
print('full_name', full_name)
print(person_info)

print(type(first_name))
print(type(skill))
print(type(person_info))

print('Lenght: ', len(first_name))

print(len(last_name) < len(first_name))

num_two = 5
num_one = 4

total = num_two + num_one
print(total)

sub = num_two - num_one
print(sub)

mul =num_two * num_one
print(mul)

div = num_two / num_one
print(div)

rema = num_two % num_one
print(rema)


# value = float(input())
# print(math.pi * (value ** 2) )

print(input("Hay nhap ten: "))
print(input('Hay nhap ho: '))
print(input('hay nhap nam sinh: '))