import time

# Create quiz UI (terminal)

def main_menu():
    print("\nWelcome to the Quiz Simulator!" \
    "\n[1] Instructions" \
    "\n[2] Create Quiz" \
    "\n[3] Take Quiz" \
    "\n[4] Exit Quiz Simulator")

def option_1():
    while True:
        print("\nQuiz Simulator: Simple, Easy, Fresh!!\n" \
        "\nTo create a quiz, select option 2 in the menu. Enter your desired quiz title and input your questions, answers, and the correct option. Press 0 to exit the quiz creator mode and your data will be stored as a .txt file in your files.\n" \
        "\nTo take a quiz, select option 3 in the menu. Type in the full file name of your quiz and start answering!\n" \
        "\nTo exit this program, select option 4 in the menu. Sad to see you go this early :((\n"
        "\nWithout further the ado (ooohh,,, the ado furthens), let's get our thinking caps on and start quizzing!!\n\n")
        time.sleep(10)
        print("I can hear them.")
        time.sleep(2)
        print("I haven't had food and water for 2 days.")
        time.sleep(2)
        print("I'm losing some feeling in my limbs.")
        time.sleep(2)
        print("But I must keep coding.")
        time.sleep(3)
        print("For them.")
        time.sleep(2)
        print("....")
        
        for idx in range(0, 20):
            time.sleep(0.3)
            print("THEY'RE COMING")


        repeat = input("\nReturn to main menu?\nYour selection (y/n): ")
        if repeat.lower() == 'y':
            time.sleep(0.8)
            print("save me save me save me save me save me")
            time.sleep(2)
            return
        elif repeat.lower() == 'n':
            continue

def option_2():
    while True:
        print("Loading Quiz Creator....\n")

        quiz_name = input("Enter the name of this quiz: ")
        quiz_filename = f"{quiz_name}.txt"

        quiz_questions = []

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
                        print("Please... enter a valid option. Please.")
            
            quiz_content = (
                f"{question}\n"
                f"a) {choice_a}\n"
                f"b) {choice_b}\n"
                f"c) {choice_c}\n"
                f"d) {choice_d}\n"
                f"Correct answer: {correct_answer}\n\n"
            )
            quiz_questions.append(quiz_content)

        with open(quiz_filename, "w") as file:
            file.write(f"Quiz name: {quiz_name}\n\n")
            for items in quiz_questions:
                file.write(items)
                file.write("\n\n")

        repeat = input("\nReturn to main menu?\nYour selection (y/n): ")
        if repeat.lower() == 'y':
            time.sleep(1)
            print("One step closer...")
            return
        elif repeat.lower() == 'n':
            time.sleep(1)
            print("And I'm about to break...")
            continue

# Read file and add into quiz simulator
def load_quiz(quiz_filename):
    with open(quiz_filename, 'r') as file:
        content = file.read()

    blocks = content.strip().split("\n\n")[1:]
    questions = []

    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 6:
            print(block)
            continue

        quiz_data = {}

        quiz_data['question'] = lines[0]
        quiz_data['a'] = lines[1][3:].strip()
        quiz_data['b'] = lines[2][3:].strip()
        quiz_data['c'] = lines[3][3:].strip()
        quiz_data['d'] = lines[4][3:].strip()
        try:
            quiz_data['answer'] = lines[5].split(": ")[1].strip()
        except IndexError:
            print("Malformed answer line! They're not gonna like this..." \
            "\nOhhh... they're not gonna like this AT ALL.")
            print(block)
            continue
        
        questions.append(quiz_data)
    return questions

def option_3():   
    while True:
        filename = input("Enter the file name of the quiz (e.g. 'quiz.txt'): ")
        try:
            questions = load_quiz(filename)
        except FileNotFoundError:
            print("Awww shucks, your file does not exist! Please check your spelling and try again :)" \
            "\nandagainandagainandagainandagain")
            continue
        
        print(f"\nStarting quiz '{filename}'....\n")
        score = 0

        # Add features like points system or time sensitivity if possible (Points system only for now)
        for idx, question in enumerate(questions, start=1):
            print(f"\nQuestion {idx}: {question['question']}\n" \
            f"a) {question['a']}\n" \
            f"b) {question['b']}\n" \
            f"c) {question['c']}\n" \
            f"d) {question['d']}\n")
            user_answer = input("Your answer (a/b/c/d): ").strip().lower()

            if user_answer == question['answer']:
                print("\nYIPPEEEEEE CORRECT!!!! Thank you so much for helping me.")
                score += 1 
                print(f"\t\tScore: {score}")
            else:
                print("No.... noooooooo no no no nO NO NO NO NO NO NO")
                print(f"\nThe correct answer is: {question['answer']}")
                print(f"\t\tScore: {score}")

        print(f"Quiz complete! Your total score: {score}/{len(questions)}")

        repeat = input("\nReturn to main menu?\nYour selection (y/n): ")
        if repeat.lower() == 'y':
            time.sleep(1)
            print("Something takes a part of me...")
            return
        elif repeat.lower() == 'n':
            time.sleep(1)
            print("Something lost and never seen...")
            continue

while True:
    main_menu()
    try:
        option = int(input("\nMain menu selection: "))
    except ValueError:
        print("Please enter a valid number from 1-4!! Only those numbers Please.")
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
        print("Loading Quiz homescreen....\n")
        time.sleep(2)
        option_3()
    elif option == 4:
        print("Exiting program.")
        time.sleep(5)
        print("I hope you come back for me soon...")
        break
    else:
        print("Invalid selection. Please pleasepleaseplease try again andagainandagain.")