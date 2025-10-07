distance_dict = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
}

# Get amount and units (assume they are valid)
amount = float(input("how much? "))
from_unit = input("From unit? ")
to_unit = input("To unit? ")

# Multiply to get to our standard value...
multiply_by = distance_dict[from_unit]
standard = amount * multiply_by

# Divide to get our desired value
divide_by = distance_dict[to_unit]
answer = standard / divide_by

print(f"There are {answer} {to_unit} in {amount} {from_unit}")