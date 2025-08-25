# Generates headings (eg:----- Heading -----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instructions", "-")

    print("""
Instructions go here.
- [instruction]
- [instruction]
-To exit the program, please type 'xxx'. """)

# Main Routine Goes Here

statement_generator("The Ultimate Conversion Calculator","-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue ")
if want_instructions == "":
    instructions()