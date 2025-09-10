distance_dict = {
    "mm": "millimetres",
    "cm": "centimetres",
    "m": "metres",
    "km": "kilometres",
    "mg": "milligrams",
    "g": "grams",
    "t": "tonnes",
    "ms": "milliseconds",
    "s": "seconds",
    "min": "minutes",
    "h": "hours",
    "days": "day",
    "week": "weeks",
    "months": "month",
    "year": "years"
}
to_find = input("unit? ")

#check if key
if to_find in distance_dict:
    print(f"{to_find} is a unit! ")

elif to_find in distance_dict.values():
    print(f"{to_find} is a unit! ")

else:
    print("Sorry - item not found, please input a valid answer")