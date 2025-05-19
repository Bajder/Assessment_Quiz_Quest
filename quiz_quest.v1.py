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

def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response is the same as the first letter of an item in the list
            # So that they need only type the first letter to make a selection
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

def the_instructions():
    """ Prints the instructions for the user """
    print("""
*** Instructions ****

To begin, choose the number of questions you would like to answer

Then you will be asked to select a question type
This is out of Triangle, Point, or Quadrilateral 
And try to answer. If you answer incorrectly, you will be told the correct answer before you move on
Remember -
A triangles internal angles always add up to 180 degrees
Angles around a point will also always add up to 180 degrees
And a Quadrilaterals internal angles will always add to 360 degrees.
You can enter the exit code of xxx at any time when selecting a question type if you would like to end the quiz
And to only type your answer without a unit!

Good luck, and if you get stuck, don't be afraid to look at the question from a different angle 😉
    """)

# Initialise Variables
question_types = ["triangle", "point", "quadrilateral", "xxx"]
questions_answered = 0
correct_answers = 0
incorrect_answers = 0
question_number = 1
quiz_history = []
user_answer = ""

# Welcome statement, check if they would like to see the instructions
print("Welcome to Quiz Quest - 📐 Angles Edition! 📐")
# Asks the user for their name in order to personalise the program
user_name = input("Please enter your name to proceed: ")
wants_instructions = string_checker(f"{user_name}, would you like to see the instructions before you begin? ")
if wants_instructions == "yes":
    the_instructions()
# Check how many questions the user would like
number_of_questions = int_check(f"How many questions would you like, {user_name}? Press <enter> to start infinite mode ")
if number_of_questions == "infinite":
    print(" ∞ infinite mode initiated! ∞ ")
    mode = "infinite"
    number_of_questions = 1
else:
    mode = "regular"
while questions_answered < number_of_questions:
    print(f"Question {question_number}")
    # Ask for type of question - Triangle, point, quadrilateral
    type_of_question = string_checker("Choose a question type! (Triangle (T), Point (P), or Quadrilateral (Q)): ", question_types)
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
                # Triangle - 180 - random int - random int = answer
                answer_triangle = 180 - angle_one - angle_two
                if user_answer == answer_triangle:
                    print(f"Congratulations, {user_name}! You answered correctly")
                    correct_answers += 1
                    answer = "correct 👍. Great Job!"
                    break
                else:
                    # Tells the user they were wrong and displays the correct answer so that they may be able to see what went wrong in their process and so that they may better understand how to answer correctly
                    print(f"Unfortunately, that is not the right answer. The right answer was {answer_triangle}")
                    incorrect_answers += 1
                    answer = "incorrect 😔. Keep Working On It!"
                    break
            except ValueError:
                print("Please enter a valid integer as your answer.")
                print("If you wish to skip this question, enter 0 to move on. This way you may see the correct answer")
        # Game History
        question = f"The Question was: If a triangles internal angles add up to 180 degrees, and the first to degrees are {angle_one} and {angle_two}, what is the value of the third angle?"
        answer_input = f"and you answered: {user_answer}"
        answer_correct_or_incorrect = f"This was {answer}"
        # Defines the variable to only be used if the user was incorrect - left blank if they were correct
        actual_answer = f""
        if answer == "incorrect 😔. Keep Working On It!":
            actual_answer = f"The Correct answer was: {answer_triangle}"
        history_item = f"Question {question_number} - {question}, {answer_input}. {answer_correct_or_incorrect}. {actual_answer}"
        quiz_history.append(history_item)
    if type_of_question == "point":
        angle_one = random.randint(1, 175)
        while True:
            try:
                user_answer = int(input(f'If the angles around a point add up to 180 degrees, and you know one angle is {angle_one}, what is the value of the adjacent angle? '))
                # Point 180 - random int = answer
                answer_point = 180 - angle_one
                if user_answer == answer_point:
                    print(f"Congratulations, {user_name}! You answered correctly")
                    correct_answers += 1
                    answer = "correct 👍. Great Job!"
                    break
                else:
                    print(f"Unfortunately, that is not the right answer. The right answer was {answer_point}")
                    incorrect_answers += 1
                    answer = "incorrect 😔. Keep Working On It!"
                    break
            except ValueError:
                print("Please enter a valid integer as your answer")
                print("If you wish to skip this question, enter 0 to move on. This way you may see the correct answer")
        # Game History
        question = f"The Question was: If the angles around a point add up to 180 degrees, and you know one angle is {angle_one}, what is the value of the adjacent angle?"
        answer_input = f"and you answered: {user_answer}"
        answer_correct_or_incorrect = f"This was {answer}"
        # Defines the variable to only be used if the user was incorrect - left blank if they were correct
        actual_answer = f""
        if answer == "incorrect 😔. Keep Working On It!":
            correct_answer_needed = "true"
            actual_answer = f"The Correct answer was: {answer_point}"
        history_item = f"Question {question_number} - {question}, {answer_input}. {answer_correct_or_incorrect}. {actual_answer}"
        quiz_history.append(history_item)
    if type_of_question == "quadrilateral":
        angle_one = random.randint(1, 90)
        angle_two = random.randint(1, 90)
        angle_three = random.randint(1, 90)
        while True:
            try:
                user_answer = int(input(f'You have a quadrilateral sitting in front of you. You know three of the angles: {angle_one}, {angle_two}, {angle_three}, \t'
                                        f'and also that all four angles should add up to 360 degrees total. What is the value of the missing angle? '))
                # Square - 360 - 3 random ints = answer
                answer_quad = 360 - angle_one - angle_two - angle_three
                if user_answer == answer_quad:
                    print(f"Congratulations, {user_name}! You answered correctly")
                    correct_answers += 1
                    answer = "correct 👍. Great Job!"
                    break
                else:
                    print(f"Unfortunately, that is not the right answer. The right answer was {answer_quad}")
                    incorrect_answers += 1
                    answer = "incorrect 😔. Keep Working On It!"
                    break
            except ValueError:
                print("Please enter a valid integer as your answer")
                print("If you wish to skip this question, enter 0 to move on. This way you may see the correct answer")
        # Game History
        question_p1 = f'The Question was: You have a quadrilateral sitting in front of you. You know three of the angles: {angle_one}, {angle_two}, {angle_three},'
        question_p2 = f'and also that all four angles should add up to 360 degrees total. What is the value of the missing angle?'
        answer_input = f"and you answered: {user_answer}"
        answer_correct_or_incorrect = f"This was {answer}"
        # Defines the variable to only be used if the user was incorrect - left blank if they were correct
        actual_answer = f""
        if answer == "incorrect 😔. Keep Working On It!":
            correct_answer_needed = "true"
            actual_answer = f"The Correct answer was: {answer_quad}"
        history_item = f"Question {question_number} - {question_p1} {question_p2}, {answer_input}. {answer_correct_or_incorrect} {actual_answer}"
        quiz_history.append(history_item)
    question_number += 1
    questions_answered += 1
# Only displays statistics and asks if you would like to see game history if you answer at least one question
if questions_answered > 0:
    # Tabulating Statistics as percentages for results summary
    percent_correct = correct_answers / questions_answered * 100
    percent_incorrect = incorrect_answers / questions_answered * 100

    print()
    print("📊📊📊 Quiz Statistics 📊📊📊")
    print(f"👍 Correct Answers: {percent_correct:.2f} \t"
          f"😔 Incorrect Answers: {percent_incorrect:.2f}")
    if percent_incorrect > 50:
      print(f"You might need a new angle to go about these questions with, {user_name}!")
    else:
        print(f"Excellent Job, {user_name}! When it comes to angles, you seem to be acute-ly aware.")
    # Game History
    see_history = string_checker("Do you want to see your game history? ")
    if see_history == "yes":
      print("Game History: ")
      for item in quiz_history:
        print(item)
    print()
    print("thanks for playing.")
# otherwise, roast
else:
    print(f"Sorry, {user_name}, it seems you've been obtuse, and ended before answering any questions!")

