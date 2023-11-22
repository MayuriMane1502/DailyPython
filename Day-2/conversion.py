# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
#print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
print('num_int', int(num_float))    #10

# str to list
first_name = 'Mayuri'
print(first_name)               # 'Mayuri'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['M', 'a', 'y', 'u', 'r', 'i']