# Using float() for the base price to safely handle decimal inputs
bp = float(input("Enter Base Price: "))
dis = float(input("Enter Discount percentage: "))

# Printing the types to verify the input typecasting worked
print(type(bp))
print(type(dis))

discount = bp * (dis / 100)
total = bp - discount

print(f"Final price is {total}")