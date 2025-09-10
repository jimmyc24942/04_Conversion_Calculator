# Ask user for an integer between 1 and 200.
def num_check(question):
    error = "Please enter a number that is between 1 and 1000 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is between 1 and 200
            if 1 <= response <= 1000:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here
while True:
     to_convert = num_check("To convert: ")
     print("You chose", to_convert)

     if to_convert == "xxx":
         break

