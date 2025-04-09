def question_creator():
    idx = 0
    while True:
        question = input(f"\nPress 0 or any key to exit\nEnter question number {idx + 1}: ")
        choices = [choice_a, choice_b, choice_c, choice_d]
        choice_a = input("Option a: ")
        choice_b = input("Option b: ")
        choice_c = input("Option c: ")
        choice_d = input("Option d: ")
# Input the correct answer
# Repeat until user inputs 'No'
# Store input into text file (file.write)