def question_creator():
    while True:
        question = input(f"\nPress 0 to exit\nEnter question: ")
        if question == "0":
            print("Stopping Quiz Creator....")
            break
        else: 
            choices()

def choices():
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
                

question_creator()

# Store input into text file (file.write)