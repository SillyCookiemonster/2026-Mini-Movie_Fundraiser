import pandas
import random

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

    return f"{decoration*3} {statement} {decoration*3}"

def instructions():
    print(make_statement("Instructions", "ℹ️"))

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

def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)

# Main routine goes here

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# Lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name' : all_names,
    'Ticket Price' : all_ticket_costs,
    'Surcharge' : all_surcharges
}

# Program main heading
print(make_statement("Mini-Movie Fundraiser Program", "🍿"))

# Ask user if they want to see the instructions and display accordingly
print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

# loop to get name, age, and payment details
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

    elif age < 16:
        print(f"{name} is a child")
        ticket_price = CHILD_PRICE

    elif age < 65:
        print(f"{name} is an adult")
        ticket_price = ADULT_PRICE

    elif age <= 120:
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
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate the total payable for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# work out the total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# Choose random winner
winner = random.choice(all_names)

# Find index of winner
winner_index = all_names.index(winner)

# retrieve winner ticket and profit (so we can adjust
# profit numbers so that the winning ticket is excluded)
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

# Currency formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

mini_movie_string = mini_movie_frame.to_string(index=False)

total_paid_string = f"Total paid: ${total_paid:.2f}"
total_profit_string = f"Total profit: ${total_profit:.2f}"

# winner announcement
lucky_winner_string = (f"The lucky winner is {winner}.   "
                       f"Their ticket worth ${ticket_won:.2f} is free!")
final_total_paid_string = f"Total Paid is now ${total_paid - ticket_won:.2f}"
final_total_profit_string = f"Total Profit is now ${total_profit - profit_won:.2f}"

if tickets_sold == MAX_TICKETS:
    num_sold_string = make_statement(f"You sold all tickets available! "
                                     f"({MAX_TICKETS})", "-")
else:
    num_sold_string = make_statement(f"You sold {tickets_sold}/"
                                     f"{MAX_TICKETS} tickets.", "-")

# Additional strings / Headings
heading_string = make_statement("Mini Movie Fundraiser", "=")
ticket_details_heading = make_statement("Ticket Details", "-")
raffle_heading = make_statement("--- Raffle Winner ---", "-")
adjusted_sales_heading = make_statement("Adjusted Sales & Profit", "-")
adjusted_explanation = (f"We have given away a ticket worth ${ticket_won:.2f} which means \nour "
                        f"sales have decreased by ${ticket_won:.2f} and our profit \n"
                        f"decreased by ${profit_won:.2f}")

# List of strings to be outputted / written to file
to_write = [heading_string, "\n",
            ticket_details_heading,
            mini_movie_string, "\n",
            total_paid_string,
            total_profit_string, "\n",
            raffle_heading,
            lucky_winner_string, "\n",
            adjusted_sales_heading,
            adjusted_explanation, "\n",
            final_total_paid_string,
            final_total_profit_string, "\n",
            num_sold_string]

# print area
print()
for item in to_write:
    print(item)

# Create file to hold data (add .txt extension)
file_name = "MMF_ticket_details"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")
