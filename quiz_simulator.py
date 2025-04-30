import time

# Create quiz UI (terminal)

def main_menu():
    print("Welcome to the Quiz Simulator!" \
    "\n[1] Instructions" \
    "\n[2] Create Quiz" \
    "\n[3] View Quizzes" \
    "\n[4] Exit Quiz Simulator")

def option_1():
    print("[Put instructions here]")

def option_2():
    print("[Put option 2 here]")

def option_3():
    print("[Put option 3 here]")

main_menu()
option = int(input("\nMain Menu Selection: "))

while option != 0:
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
        option(3)
    else:
        exit()
# Read file and add into quiz simulator
# Add features like points system or time sensitivity if possible