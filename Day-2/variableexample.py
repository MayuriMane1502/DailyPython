print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument
####################################################
#Day 2: 30 Days of python programming 

# Variables in Python
first_name = 'Johnny'
last_name = 'Depp'
country = 'Finland'
city = 'Helsinki'
age = 25
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Johnny',
   'lastname':'Depp',
   'country':'Finland',
   'city':'Helsinki'
   }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# declaring multiple variable in a line

first_name, last_name, country, age, is_married = 'Mayuri', 'Mane', 'Helsink', 24, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#taking input from user
first_name = input('what is your name? ')
last_name = input('what is your last name? ')

print(first_name + last_name)