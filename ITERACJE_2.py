n = 0
print("Before the loop")
while n < 5:
    n += 1
    if n == 4:
        print("Just before break")
        break
    if n == 1:
        print("Just before continue")
        continue
    print(n)
print("After the loop")