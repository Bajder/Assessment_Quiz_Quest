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
question_types = ["triangle", "line", "square"]
questions_answered = 0
# Check how many questions the user would like
print("Welcome to Quiz Quest - Angles Edition!")
number_of_questions = int_check("How many rounds would you like? Press <enter> to start infinite mode ")
# Checks the number of rounds prints correctly - for testing purposes
print(number_of_questions)
if number_of_questions == "infinite":
    print("infinite mode")
    mode = "infinite"
    number_of_questions = 2
while questions_answered < number_of_questions:
    # Ask for type of question - Triangle, straight line, square
    type_of_question = string_checker("Choose a question type! (Triangle (T), Straight Line (L), or Square (S)): ", question_types)
    print(type_of_question)
    questions_answered += 1
    if mode == "infinite":
        number_of_questions += 1
    if type_of_question == "triangle":
        # makes the question
        print("ya da ya da")
# Triangle - random int, random int 180 - both these = answer
# Straight line 180 - random int
# Square - 360 - 3 random ints

# Display question, ask for answer, check if the answer is correct or not - add this to the quiz results

# Create percentages for results summary
