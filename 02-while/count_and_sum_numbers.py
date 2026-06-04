# Exercise: Count and sum numbers until zero is entered

count = 0
total = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    count += 1
    total += number

print(f"Quantity: {count}")
print(f"Sum: {total}")