def main():
    global events

    choice = "Continue"

    events = {}




    while choice.lower() != "end":
        selection = input("What would you like to do? \n Add event \n Remove event \n Update status")

        if selection.lower() == "add event":
            add_event()
        elif selection.lower() == "remove event":
            remove_event()
        elif selection.lower() == "update status":
            update_status()
        else:
            print("Invalid input.")

        choice = input("Would you like to continue? \n Input 'end' to end.")

    print("------------")
    print(events)


def add_event():
    event = input("Input your event: ")

    events[event] = "Upcoming"


    print(events)

def remove_event():
    if len(events) == 0:
        print("There are no events to remove.")
    else:
        event = input("Input your event: ")

        del events[event]
        print(events)


def update_status():
    if len(events) == 0:
        print("There are no events to update.")
    else:
        event = input("Input your event name: ")
        status = input("What is your status: \n Upcoming \n Over \n Cancelled")

        events[event] = status
        print(events)





main()