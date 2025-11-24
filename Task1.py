n = int(input("Enter the required string length: "))

sequence = ""
num = 1

while len(sequence) < n:
    sequence += str(num)
    num += 1

print("Generated sequence:", sequence)
