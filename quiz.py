import random

# Load Quiz Questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "Berlin", "Madrid", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Who wrote the novel 'Pride and Prejudice'?",
        "answers": ["Jane Austen", "Charles Dickens", "Mark Twain", "J.K. Rowling"],
        "correct_answer": "Jane Austen"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["Jupiter", "Saturn", "Mars", "Earth"],
        "correct_answer": "Jupiter"
    },
    {
        "question": "What is the smallest country in the world?",
        "answers": ["Vatican City", "Monaco", "San Marino", "Liechtenstein"],
        "correct_answer": "Vatican City"
    }
]

# Display Welcome Message and Rules
print("Welcome to the Quiz Game!")
print("You will be asked a series of questions.")
print("Your goal is to select the correct answer for each question.")
print("You will receive points for each correct answer.")
print("Good luck!")

# Initialize Score
score = 0

# Present Quiz Questions
for question in quiz_questions:
    # Display each question and answer choice
    print("\nQuestion: " + question["question"])
    for i, answer in enumerate(question["answers"]):
        print(f"{i+1}. {answer}")
    
    # Prompt the user to select an answer
    user_answer = input("Select your answer (1-4): ")
    
    # Evaluate the User's Answer
    if user_answer.isdigit() and int(user_answer) > 0 and int(user_answer) <= len(question["answers"]):
        user_answer = question["answers"][int(user_answer) - 1]
        if user_answer == question["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question['correct_answer']}.")
    else:
        print("Invalid answer. Please select a number from 1 to 4.")

# Calculate the Final Score
final_score = score / len(quiz_questions) * 100

# Display Final Results
print(f"\nYour final score is {final_score}%.")
if final_score >= 80:
    print("Congratulations! You are a quiz master!")
elif final_score >= 60:
    print("Good job! You have a solid understanding of the subject.")
else:
    print("Keep practicing! You can do better next time.")

# Play Again
play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == "yes":
    # Reset Score and Play Again
    score = 0
    for question in quiz_questions:
        # Display each question and answer choice
        print("\nQuestion: " + question["question"])
        for i, answer in enumerate(question["answers"]):
            print(f"{i+1}. {answer}")
        
        # Prompt the user to select an answer
        user_answer = input("Select your answer (1-4): ")
        
        # Evaluate the User's Answer
        if user_answer.isdigit() and int(user_answer) > 0 and int(user_answer) <= len(question["answers"]):
            user_answer = question["answers"][int(user_answer) - 1]
            if user_answer == question["correct_answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {question['correct_answer']}.")
        else:
            print("Invalid answer. Please select a number from 1 to 4.")

    # Calculate the Final Score
    final_score = score / len(quiz_questions) * 100

    # Display Final Results
    print(f"\nYour final score is {final_score}%.")
    if final_score >= 80:
        print("Congratulations! You are a quiz master!")
    elif final_score >= 60:
        print("Good job! You have a solid understanding of the subject.")
    else:
        print("Keep practicing! You can do better next time.")