# Functions go here
def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """Checks that the users enter the full word
    or the 'n' letter(s) of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check the response is the entire word
            if response == item:
                return item

            # check the response is the first letter
            if response == item[:num_letters]:
                return item

        print(f"Please choose a valid answer from {valid_ans_list}")

def int_check(question):
    """Checks the user enters an integer above 0"""

    error = f"Oops - please enter an integer."

    while True:
        response = input(question)

        try:
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def not_blank(question):
    """Checks users don't respond with nothing"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


# Main routine goes here

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# Loop for testing purposes
while True:
    print()

    # Check users name (and check it's not blank)
    name = not_blank("Name: ")

    # Ask for users age (and check it's not blank)
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue

    elif 12 <= age < 16:
        print(f"{name} is a child")
        ticket_price = CHILD_PRICE

    elif 16 <= age < 65:
        print(f"{name} is an adult")
        ticket_price = ADULT_PRICE

    elif 65 <= age <= 120:
        print(f"{name} is a senior")
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    surcharge = 0

    if pay_method == "credit":
        surcharge = ticket_price * CREDIT_SURCHARGE

    # calculate total payable ...
    total_to_pay = ticket_price + surcharge

    print(f"\n{name}'s ticket cost ${ticket_price:.2f}, they paid by {pay_method} "
          f"so the surcharge is ${surcharge:.2f}\n"
          f"The total payable is ${total_to_pay:.2f}")