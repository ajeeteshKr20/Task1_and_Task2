pos = int(input("Enter the position: "))

sequence = ""
num = 1

# Keep generating the sequence until it reaches the required position
while len(sequence) < pos:
    sequence += str(num)
    num += 1

# Find the digit at the given position
result = sequence[pos - 1]

print("Digit at position", pos, "is:", result)
