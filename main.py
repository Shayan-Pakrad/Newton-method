a = int(input("enter the number : "))
x = 10

while True:
    y = (x + a/x) / 2
    if y == x:
        print(f"The root of {a} is {y}")
        break
    x = y
