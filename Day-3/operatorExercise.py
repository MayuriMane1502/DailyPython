#Declare your age as integer variable
age = 24

#Declare your height as a float variable
height = 5.2

#Declare a variable that store a complex number
complex_number = 1+3j

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
Base = int(input('Enter base: '))
Height =int(input('Enter height: '))
area = 0.5 * Base * Height
print('The Area of triangle is: ',int(area)) 

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

a= int(input('Side a: '))
b= int(input('Side b: '))
c= int(input('Side c: '))
perimeter = a+b+c
print('the perimeter of the triangle is: ',perimeter)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter length: '))
width = int(input('Enter width: '))
area = length * width
perimeter = 2*(length+width)
print('Area of rectangle is: ',area)
print('Perimeter of rectangle is: ',perimeter)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input('Enter the radius - '))
print('radius of circle - ', r)
pi= 3.14
area = pi * r * r
print('area is - ',area)
c = 2 * pi *r
print('circumference is- ',c)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

slope1 = 2 # Coefficients

x_intercept = 0 ## x-intercept (where y = 0)

y_intercept = -2 ## y-intercept (where x = 0)

print("Slope:", slope1)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Given points
x1, y1 = 2, 2
x2, y2 = 6, 10

slope2 = (y2 - y1) / (x2 - x1) # Calculate the slope

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 # Calculate the Euclidean distance

D = (x2 - x1) ^2 + ( y2 - y1) ^2 # ggl formula

print("Slope:", slope2)
print("Euclidean Distance:", distance)
print('D: ',D)

#Compare the slopes in tasks 8 and 9.
print(slope1 == slope2)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
a=(len('python'))
b=(len('dragon'))
print('compare result: ',a==b)
print('comparision of length of python & dragon:', len('python')==len('dragon'))

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
str1 = 'python'
str2 = 'dragon'

result = 'on' in str1 and 'on' in str2 # Check if 'on' is found in both strings
print(result)

result2 = 'on' in 'python' and 'on' in 'dragon' #other method
print(result2)

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon.'
result = 'jargon' in sentence
print(result)

#There is no 'on' in both dragon and python
str1 = 'python'
str2 = 'dragon'
result = 'on' not in str1 and 'on' not in str2
print(result)

result2 = not('on' in 'python' and 'on' in 'dragon') #other method
print(result2)

#Find the length of the text python and convert the value to float and convert it to string
length= len('python')
print('float length of python: ',float(length))
print('string length of python: ',str(length))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
a=int(input('enter no: '))
print('checking even no or not?: ', a%2==0)   # True

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_div=7/3
result = int(7//3)
print('floor_div:', floor_div)
print('int conversion:', result)
result2 = floor_div == result
print('floor division of 7 by 3 is equal to the int converted value: ', result2)


#Check if type of '10' is equal to type of 10
print('type of 10 is equal to type of 10: ',type(10) == type(10))

#Check if int('9.8') is equal to 10 
print('int 9.8 is equal to 10:', type(9.8)== type(10))

'''Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120'''
hours = int(input('Enter hours: '))
rate = int(input('Enter the rate per hour: '))
earning = hours * rate
print('Your weekly earning is: ', earning)
print(f'Your weekly earning is {earning}')

'''Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.'''
years = int(input('Enter the number of years you have lived: '))
calculate_sec = years * 24 * 60 * 60 * 365 #years lived * hours in day*minutes*seconds* days in year
print(f'You have lived for {calculate_sec} seconds')

'''Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125'''
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

#other method using loop
# Number of rows in the table
num_rows = 5

# Display the table
for i in range(1, num_rows + 1):
    print(f"{i} {1} {i} {i*i} {i*i*i}")
