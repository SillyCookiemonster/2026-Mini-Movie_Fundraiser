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

# Main routine goes here

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("program continues...")
