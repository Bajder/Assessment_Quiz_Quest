import random
# Date: 13/05/2025
# Program Name: Quiz Quest
# Author: Brooke Jackson
# Program Use: Mathematics-Based Quiz for Students

# Functions
def int_check(question):
    """Checks users enter an integer that is 1 or more."""
    # User input
    while True:
        # Error message
        error = f"Please enter an integer that is 1 or more.."

        to_check = input(question)

        # Check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)
            if response < 1:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response is the same as the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

# Initialise Variables
question_types = ["triangle", "line", "square", "xxx"]
questions_answered = 0
correct_answers = 0
incorrect_answers = 0
question_number = 1
game_history = []
# Check how many questions the user would like
print("Welcome to Quiz Quest - Angles Edition!")
number_of_questions = int_check("How many rounds would you like? Press <enter> to start infinite mode ")
if number_of_questions == "infinite":
    print("infinite mode")
    mode = "infinite"
    number_of_questions = 2
else:
    mode = "regular"
while questions_answered < number_of_questions:
    print(f"Question {question_number}")
    # Ask for type of question - Triangle, straight line, square
    type_of_question = string_checker("Choose a question type! (Triangle (T), Straight Line (L), or Square (S)): ", question_types)
    print(type_of_question)
    questions_answered += 1
    if mode == "infinite":
        number_of_questions += 1
    # Stop the question process if the user enters the exit code
    if type_of_question == "xxx":
        break
    if type_of_question == "triangle":
        # Defines the angles in the question so they do not get changed if the value error is triggered and the code runs again
        angle_one = random.randint(1, 90)
        angle_two = random.randint(1, 90)
        while True:
            try:
                user_answer = int(input(f'If a triangles internal angles add up to 180 degrees, and the first to degrees are {angle_one} and {angle_two}, what is the value of the third angle? '))
                answer_triangle = 180 - angle_one - angle_two
                if user_answer == answer_triangle:
                    print("Congratulations! You answered correctly")
                    correct_answers += 1

                else:
                    # Tells the user they were wrong and displays the correct answer so that they may be able to see what went wrong in their process and so that they may better understand how to answer correctly
                    print(f"Unfortunately, that is not the right answer. The right answer was {answer_triangle}")
                    incorrect_answers += 1
            except ValueError:
                print("Please enter a valid integer as your answer")
            question_number += 1
    if type_of_question == "line":
        angle_one = random.randint(1, 90)
        user_answer = int(input(f'If the angles around straight lines add up to 180 degrees, and you know one angle is {angle_one}, what is the value of the adjacent angle?'))
        answer_line = 180 - angle_one
        if user_answer == answer_line:
            print("Congratulations! You answered correctly")
            correct_answers += 1
        else:
            print(f"Unfortunately, that is not the right answer. The right answer was {answer_line}")
            incorrect_answers += 1
        question_number += 1
    if type_of_question == "square":
        angle_one = random.randint(1, 90)
        angle_two = random.randint(1, 90)
        angle_three = random.randint(1, 90)
        user_answer = int(input(f'You have a quadrilateral sitting in front of you. You know three of the angles: {angle_one}, {angle_two}, {angle_three}, and also that all four angles should add up to 360 degrees total. What is the value of the missing angle? '))
        answer_square = 360 - angle_one - angle_two - angle_three
        if user_answer == answer_square:
            print("Congratulations! You answered correctly")
            correct_answers += 1
        else:
            print(f"Unfortunately, that is not the right answer. The right answer was {answer_square}")
            incorrect_answers += 1
    # Collect game history?

# Triangle - random int, random int 180 - both these = answer
# Straight line 180 - random int
# Square - 360 - 3 random ints

# Display question, ask for answer, check if the answer is correct or not - add this to the quiz results

# Create percentages for results summary
