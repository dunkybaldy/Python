x = input("What bread do you feel like today?\r\n\n")

print ("So you feel like " + x + "?")

validEntries = ["Y", "y", "N", "n"]

validEntry = False
i = 0
while not validEntry:
    doThey = input("Are you sure? ... Y/N\r\n\n")
    for entry in validEntries:
        if doThey == entry:
            validEntry = True

    if not validEntry:
        print("Please copy the instructions on screen.\r\n\n")
        i += 1

    if i > 5:
        print("I give up...")
        break


if doThey.lower() == 'y':
    print("Ace!")
else:
    print("Seriously...")