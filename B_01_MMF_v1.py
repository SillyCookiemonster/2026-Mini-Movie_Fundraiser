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

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration*3} {statement} {decoration*3}")

def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
    
For each ticket holder enter ...
- their name
- Their age
- Their payment method (cash / credit)

The program will record the ticket sale and calculate the
ticket cost (and the profit).

Once you have either sold all of the tickets or entered the
exit code ('xxx'), the program will display the ticket
sales information and write data to a text file.

It will also choose one lucky ticket holder who wins the
draw (their ticket is free).
    ''')

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

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()


while tickets_sold < MAX_TICKETS:
    print()

    # Check users name (and check it's not blank)
    name = not_blank("Name: ")

    # If name is the exit code, break out of the loop
    if name == "xxx":
        break

    # Ask for users age (and check it's not blank)
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket ({pay_method})")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You sold all tickets available! ({MAX_TICKETS})")
else:
    print(f"You have sold {tickets_sold}/{MAX_TICKETS} tickets.")
