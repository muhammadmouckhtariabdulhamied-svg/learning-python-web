numbers = [23,4,5,6,7,50,21,]
max = numbers[0]
for number in numbers:
    if number >max:
        max = number
print (max)
numbers = [12,3,4,0.5,98,21,]
min =numbers[0]
for number in numbers:
    if number<min:
        min =number
print(min)
numbers = [12,3,4,0.5,98,32,54]
for number in numbers:
    average =sum(numbers)/len(numbers)
    print(average)