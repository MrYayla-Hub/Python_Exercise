num1 = 1
num2 = 1
fib = [num1,num2]

for i in range(28):
    num1,num2 = num2,num1+num2
    fib.append(num2)
print(fib)