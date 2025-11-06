count = 0
with open("emails.txt", "r") as file:
    for line in file:
        if "@gmail.com" in line:
            print(line.strip())
            count += 1

print(f"\nTotal Gmail addresses found: {count}")
