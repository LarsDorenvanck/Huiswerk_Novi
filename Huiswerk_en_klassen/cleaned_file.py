





















for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")








total = 0
for j in range(0, 5):
    j += 1
    total += j
    print(f"{j} +")

print(f"= {total}")











for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



















length = int(input("Hoeveel Fibonacci-getallen wil je zien? "))

a = 0
b = 1

for _ in range(length):
    prev = a
    a = b
    b = prev + b
    print(a)












exit()