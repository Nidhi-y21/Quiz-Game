import random
import threading


def input_with_timeout(prompt, timeout):
    """Function to get user input with a timeout."""
    answer = [None]

    def get_input():
        answer[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        print("\nTime's up!")
        thread.join()  # Ensure the thread finishes
    return answer[0]


print("----WELCOME IN MY QUIZ GAME----")
ans = input("Do you want to play the quiz? (yes/no): ").lower()
if ans == "yes":
    print("Let's start the quiz!")
    score = 0
    questions = int(input("How many questions do you want to answer? (1-5): "))
    if questions < 1 or questions > 5:
        print("Please enter a number between 1 and 5.")
        exit()
    print("You have selected", questions, "questions.")
    print("Let's begin!")

    # List of questions and answers
    quiz = [
        {"question": "What is the color of the sky?", "answer": "Skyblue"},
        {"question": "What is the color of grass?", "answer": "Green"},
        {"question": "What is the color of blood?", "answer": "Red"},
        {"question": "What is the color of a banana?", "answer": "Yellow"},
        {"question": "What is the color of an orange?", "answer": "Orange"}
    ]

    # Shuffle the questions
    random.shuffle(quiz)

    for i in range(questions):
        print(f"Question {i + 1}: {quiz[i]['question']}")
        user_answer = input_with_timeout("Your answer (10 seconds): ", 10)
        if user_answer is None:
            print("You didn't answer in time!")
        elif user_answer.lower() == quiz[i]['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is:", quiz[i]['answer'])

    print("Your final score is:", score)
else:
    print("Okay, maybe next time!")
    exit()