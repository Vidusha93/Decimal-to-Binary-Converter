# Decimal to Binary Converter
# By Ishanga vidusha 201700124
decimal = int(input("Enter a Decimal number: "))
binary = [0]
while decimal >= 1:
    if decimal % 2 == 1:
        binary.insert(1,1)
        decimal = decimal // 2
    elif decimal % 2 == 0:
        binary.insert(1,0)
        decimal = decimal // 2
print("Binary: ", *binary)
#print("Decimal: ", decimal)

