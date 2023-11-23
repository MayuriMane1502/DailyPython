# creating a string
greeting = 'Hello World!'
print(len(greeting))        #12

#mutli line sentence
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

print("######################################################")
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

print("######################################################")
#escape sequence
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

print("######################################################")
#old style string formatting
first_name = 'Mayuri'
last_name = 'Depp'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
print("----------------------------------------------------")
# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
print(formated_string)
print("----------------------------------------------------")
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
print("######################################################")
#New style string formatting

first_name = 'Mayuri'
last_name = 'Mane'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

'''# output
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64'''

print("-------------------------------------------------------------")
# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)
print("######################################################")
#string interpolation or f-strings
a= 4
b=5
print(f'{a}+{b} ={a+b}') # 4+5=9

print("######################################################")
#Python Strings as Sequences of Characters

word = "python"
a,b,c,d,e,f = word #unpacking sequence character into variable
print(a)    #p
print(b)    #y
print(c)    #t
print(d)    #h
print(e)    #o
print(f)    #n

print("###################Accessing Characters in Strings by Index#######################")
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

print("######################Slicing Python Strings################################")
language = 'Python'
first_three = language[0:3] # or language [:3] = starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

print("######################Reversing a String################################")
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH #start:end:-1 [to reverse and start from rightmost character to left]
#The [::-1] part specifies the slicing with a step of -1, so it starts from the end and goes towards the beginning of the string.
print("######################Skipping Characters While Slicing################################")
#It is possible to skip characters while slicing by passing step argument to slice method.
word = 'python'
print(word[0:6:2]) #pto

print("######################################################")
print("######################################################")