def main():
    global events
    global statuses

    choice = "Continue"

    events = {}
    statuses = {}



    selection = input("What would you like to do? \n Add event \n Remove event \n Update status")
    while choice.lower() != "end":
        if selection.lower() == "add event":
            add_event()
        elif selection.lower() == "remove event":
            remove_event()
        elif selection.lower() == "update status":
            update_status()

        choice = "Would you like to continue: \n Continue \n End"


def add_event():
    event = input("Input your event: ")
    date = input("input the event date: ") #I'll work on data validation later.

    events[event] = date
    statuses[event] = "Upcoming"

    print(events)
    print(statuses)

def remove_event():
    event = input("Input your event: ")

    del events[event]
    print(events)

def update_status():
    event = input("Input your event: ")
    status = input("What is your status: \n Upcoming \n Over \n Cancelled")

    statuses[event] = status
    print(statuses)



main()