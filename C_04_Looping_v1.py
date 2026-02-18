
# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

while tickets_sold != MAX_TICKETS:
    name = input("What is your name? ")

    # If name is the exit code, break out of the loop
    if name == "xxx":
        break

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You sold all tickets available! ({MAX_TICKETS})")
else:
    print(f"You have sold {tickets_sold}/{MAX_TICKETS} tickets.")
