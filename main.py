
# ******************************
# Make your Code
# ******************************
numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

sum_num = 0
for j in numbers:
    sum_num += j

avg = sum_num / len(numbers)

# getting the differences
for k in numbers:
    print(f"{abs(avg - k):.2f}", end=" ")

# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')
