print("Podaj x = ")
x = input()
print("Podaj y = ")
y = input()

if x > y:
    print(f"{x} jest większe od {y}")
elif x == y:
    print(f"{x} jest rowne {y}")
else:
    print(f"{x} jest mniejsze od {y}")