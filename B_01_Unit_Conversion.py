# Generates headings (eg:----- Heading -----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instructions", "-")

    print("""
- The following can be converted:
Mass, Length, Time
- All units work in abbreviations apart from 'day','week' and 'year'
- You cannot cross convert e.g. 'mm' to 'week'
-To exit the program, please type 'xxx'. 
""")

# Main Routine Goes Here

statement_generator("The Ultimate Conversion Calculator","-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue ")
if want_instructions == "":
    instructions()
def num_check(question):
    error = "You chose to continue, huzzah!\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)
        except ValueError:
            print(error)

        distance_dict = {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1,
            "km": 1000,
        }
        time_dict = {
            "ms": 0.001,
            "s": 1,
            "min": 60,
            "h": 3600,
            "day": 86400,
            "week": 604800,
            "year": 31557600,
        }
        mass_dict = {
            "mg": 0.000001,
            "g": 0.001,
            "kg": 1,
            "t": 1000,
        }
        # combine all for checking
        all_units = {**distance_dict,**time_dict,**mass_dict}

        #Helper function to get the unit category
        def get_category(unit):
            if unit in distance_dict:
                return "distance"
            elif unit in mass_dict:
                return"mass"
            elif unit in time_dict:
                return"time"
            else:
                return None
        # Get user input
        amount = float(input("how much? "))
        from_unit = input("From unit? ")
        to_unit = input("To unit? ")

        # Multiply to get to our standard value...
        multiply_by = all_units[from_unit]
        standard = amount * multiply_by

        # Divide to get our desired value
        divide_by = all_units[to_unit]
        answer = standard / divide_by
        if (from_unit in time_dict and to_unit in time_dict or from_unit in mass_dict and to_unit in mass_dict or from_unit in distance_dict and to_unit
                in distance_dict):
            print(f"There are {answer} {to_unit} in {amount} {from_unit}")
            print()

        #Check if both units are valid
        if from_unit not in all_units or to_unit not in all_units:
            print("Cannot convert, enter a valid answer ")
        else:
            from_cat = get_category(from_unit)
            to_cat = get_category(to_unit)
            if from_cat != to_cat:
                print(f"Cannot convert from {from_unit}({from_cat}) to {to_unit}({to_cat}).")
                print()


while True:
     to_convert = num_check("End?: ")
     print("You chose to end, bye bye! :)")

     if to_convert == "xxx":
         break