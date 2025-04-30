import time

# Create quiz UI (terminal)

def main_menu():
    print("Welcome to the Quiz Simulator!" \
    "\n[1] Instructions" \
    "\n[2] Create Quiz" \
    "\n[3] Take Quiz" \
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
        print("Loading Quiz Creator....\n")

        quiz_name = input("Enter the name of this quiz: ")
        quiz_filename = f"{quiz_name}.txt"

        quiz_questions = []

        # Create quiz by asking user to input questions, options, and correct answer
        while True:
            question = input(f"\nPress 0 to exit\nEnter question: ")
            if question == "0":
                print("Stopping Quiz Creator....")
                break

            else:
                choice_a = input("Option a: ")
                choice_b = input("Option b: ")
                choice_c = input("Option c: ")
                choice_d = input("Option d: ")

                while True:
                    correct_answer = input("Enter the correct option (a/b/c/d): ")
                    if correct_answer in ["a", "b", "c", "d"]:
                        break
                    else:
                        print("Please enter a valid option")
            
            # Format quiz content before writing into .txt file
            quiz_content = (
                f"{question}\n"
                f"a) {choice_a}\n"
                f"b) {choice_b}\n"
                f"c) {choice_c}\n"
                f"d) {choice_d}\n"
                f"Correct answer: {correct_answer}\n\n"
            )
            quiz_questions.append(quiz_content)

        # Store input into text file (file.write)
        with open(quiz_filename, "w") as file:
            file.write(f"Quiz name: {quiz_name}\n\n")
            for items in quiz_questions:
                file.write(items)
                file.write("\n\n")

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
        print("Loading Quiz Creator homescreen....\n")
        time.sleep(2)
        option_2()
    elif option == 3:
        print("Loading Quiz....\n")
        time.sleep(2)
        option_3()
    elif option == 4:
        print("Exiting program. Bye-bye!!")
        break
    else:
        print("Invalid selection. Please try again.")


# Read file and add into quiz simulator
# Add features like points system or time sensitivity if possible