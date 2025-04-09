quiz_name = input("Enter the name of this quiz: ")
quiz_filename = f"{quiz_name}.txt"

quiz_questions = []

def question_creator():
    while True:
        question = input(f"\nPress 0 to exit\nEnter question: ")
        if question == "0":
            print("Stopping Quiz Creator....")
            break
        else: 
            options = choices()
            qna = {
                "question": question,
                "choices": options,
            }
            quiz_questions.append(qna)

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

        
        return {
            "a": choice_a,
            "b": choice_b,
            "c": choice_c,
            "d": choice_d
        }

# Store input into text file (file.write)

def write_as_file():
    with open(f"{quiz_name}.txt", "w") as file:
        for item in quiz_questions:
            file.write(f"Question {item}: {item['question']}\n")
            for key in item["choices"].items():
                file.write(f"{key}\n")
            file.write("\n")
            
question_creator()
write_as_file()