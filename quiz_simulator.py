import time

# Create quiz UI (terminal)

def main_menu():
    print("Welcome to the Quiz Simulator!" \
    "\n[1] Instructions" \
    "\n[2] Create Quiz" \
    "\n[3] View Quizzes" \
    "\n[4] Exit Quiz Simulator")

def option_1():
    while True:
        print("[Put instructions here]")

        repeat = input("\nReturn to main menu?\nYour selection (y/n): ")
        if repeat.lower() == 'y':
            return
        elif repeat.lower() == 'n':
            continue

def option_2():
    while True:
        print("[Put option 2 here]")

        repeat = input("\nReturn to main menu?\nYour selection (y/n): ")
        if repeat.lower() == 'y':
            return
        elif repeat.lower() == 'n':
            continue

def option_3():
    while True:
        print("[Put option 3 here]")

        repeat = input("\nReturn to main menu?\nYour selection (y/n): ")
        if repeat.lower() == 'y':
            return
        elif repeat.lower() == 'n':
            continue

while True:
    main_menu()
    try:
        option = int(input("\nMain menu selection: "))
    except ValueError:
        print("Please enter a valid number from 1-4!!")
        continue

    if option == 1:
        print("Loading instructions....\n")
        time.sleep(2)
        option_1()
    elif option == 2:
        print("Loading [quiztxtfilename]....\n")
        time.sleep(2)
        option_2()
    elif option == 3:
        print("Loading Quiz Maker homescreen....\n")
        time.sleep(2)
        option_3()
    elif option == 4:
        print("Exiting program. Bye-bye!!")
        break
    else:
        print("Invalid selection. Please try again.")
# Read file and add into quiz simulator
# Add features like points system or time sensitivity if possible