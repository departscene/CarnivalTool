import cardClass
import re

def newCard():
    print("---New Card---")
    card = cardClass.Card()
    command = input("Enter the revealed square and value (e.g '41' for a 4 in square 4). Enter 'new' to start again, CTRL+C to exit: ")

    while command != "new":
        if not re.match(r"^[1-9]{2}$", command):
            print("Invalid command")
        else:
            try:
                card.reveal(int(command[0])-1, int(command[1]))
            except ValueError as e:
                print(e)
        command = input("Enter the revealed square and value (e.g '41' for a 4 in square 4). Enter 'new' to start again, CTRL+C to exit: ")

    newCard()

if __name__ == "__main__":
    print(f"{'-'*20}\n{'Carnival Tool':^20}\n{'-'*20}")
    newCard()
