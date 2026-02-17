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


# Main routine goes here
payment_list = ('cash', 'credit')

want_instructions = string_check("Do you want to see the instructions? ")
print(f"You chose {want_instructions}")

pay_method = string_check("Payment method: ", payment_list, 2)
print(f"You chose {pay_method}")
