#Using the len() built-in function, find the length of your first name
#Compare the length of your first name and your last name

first_name = 'Mayuri'
last_name = 'Mane'
print(first_name +" "+last_name)
print('length of first_name-', len(first_name))
print('length of last_name-', len(last_name))
print('comparing len of first & last name- ', len(first_name) == len(last_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
print('num_one & num_two - ', num_one,num_two)
#Add num_one and num_two and assign the value to a variable total
total = (num_one+num_two)
print('total- ',total)

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one- num_two
print('diff- ', diff)

#Multiply num_two and num_one and assign the value to a variable product
product = num_one*num_two
print('product- ',product)

#Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two
print('division- ', division)

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder= num_one % num_two
print('remainder- ', remainder)

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print('exponential- ', exp)

#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print('floor division- ', floor_division)

#The radius of a circle is 30 meters.
radius =30

import math # for pi value or assign pi = 3.14

#Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = math.pi * radius ** 2
print('area of circle - ', area_of_circle)

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius
print('circumferance of circle - ', circum_of_circle)

#Take radius as user input and calculate the area.
radius = int(input('Enter the radius - '))
print('radius of circle - ', radius)
pi= 3.14
area = pi * radius **2
print('area is - ',area)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('enter your first name?- ')
last_name = input('enter your last name?- ')
country = input('enter country name?- ')
age = input('how old are you?- ')

print('User Info- ', first_name , last_name, country, age)

person_info = {
   'firstname':'Mayuri',
   'lastname':'Mane',
   'country':'Finland',
   'age':'24'
   }

print('personal info- ', person_info)
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
#shell
'''>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
'''