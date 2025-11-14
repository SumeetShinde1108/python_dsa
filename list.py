x = [9, 12, 7, 4, 11]
x.append(8)
x.sort()
print(x)

#algorithm to find lowest value in list:

my_array = [12, 34, 7, 11, 13, 4]
min_value = my_array[0]

for i in my_array:
    if i < min_value:
        min_value = i

print('Lowest Value :', min_value)