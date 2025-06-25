num = int(input("Enter the first number: "))
print(num)
second = int(input("Enter the second number: "))
print(second)
result = num * second
equatuion = f"{num} x {second} = {result}"
print(equatuion)
if result > 0 :
    print("The result is positive.")
elif result < 0 :
    print("The result is negative.")
elif result == 0 :
    print("The result is positive and negative.")