
list = []
total = int(input('Total numbers in List: '))

for num in range(total):
    num = int(input('Enter number '))
    list.append(num)

print("Sum of elements in given list is :", sum(list))