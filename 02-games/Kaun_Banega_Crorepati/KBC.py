
"""
KBC (Kaun Banega Crorepati) - Quiz Game
Uses: list, loop, conditionals
Rules:
- 10 questions, each with 4 options (A, B, C, D)
- Correct answer -> money added to winnings (amount increases per question)
- Wrong answer -> game ends, but user keeps money won up to previous question
- User can quit anytime by typing 'quit' (loses current question's prize but keeps earlier winnings)
"""

# List of questions -> each question is a dictionary
# 'q' = question text, 'options' = list of 4 choices, 'answer' = correct option letter, 'prize' = money for this question
questions = [
    {"q": "What is the capital of India?",
     "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
     "answer": "B", "prize": 1000},

    {"q": "Which planet is known as the Red Planet?",
     "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
     "answer": "C", "prize": 2000},

    {"q": "Who wrote the Indian National Anthem?",
     "options": ["A. Rabindranath Tagore", "B. Bankim Chandra", "C. Sarojini Naidu", "D. Mahatma Gandhi"],
     "answer": "A", "prize": 5000},

    {"q": "What is the chemical symbol for Gold?",
     "options": ["A. Go", "B. Gd", "C. Au", "D. Ag"],
     "answer": "C", "prize": 10000},

    {"q": "How many players are there in a cricket team?",
     "options": ["A. 9", "B. 10", "C. 12", "D. 11"],
     "answer": "D", "prize": 20000},

    {"q": "Which is the largest ocean in the world?",
     "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
     "answer": "C", "prize": 40000},

    {"q": "Who is known as the Father of Computers?",
     "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
     "answer": "A", "prize": 80000},

    {"q": "Which is the smallest prime number?",
     "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
     "answer": "C", "prize": 160000},

    {"q": "In which year did India gain independence?",
     "options": ["A. 1945", "B. 1946", "C. 1947", "D. 1950"],
     "answer": "C", "prize": 320000},

    {"q": "What is the currency of Japan?",
     "options": ["A. Won", "B. Yuan", "C. Ringgit", "D. Yen"],
     "answer": "D", "prize": 640000},
]

def play_game():
    print("=" * 50)
    print("   WELCOME TO KAUN BANEGA CROREPATI (KBC)")
    print("=" * 50)
    print("Answer correctly to win money!")
    print("Type A, B, C or D to answer, or 'quit' to leave with your current winnings.\n")

    total_winnings = 0
    question_number = 1

    # Loop through each question in the list
    for question in questions:
        print(f"\nQuestion {question_number} for Rs. {question['prize']}:")
        print(question["q"])

        # Loop through the list of 4 options and print them
        for option in question["options"]:
            print(option)

        # Get user's answer, keep asking until valid input given
        user_answer = ""
        while user_answer not in ["A", "B", "C", "D", "QUIT"]:
            user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if user_answer == "QUIT":
                print(f"\nYou chose to quit. You take home Rs. {total_winnings}!")
                return
            if user_answer not in ["A", "B", "C", "D"]:
                print("Invalid input. Please enter A, B, C, D or 'quit'.")

        # Check the answer
        if user_answer == question["answer"]:
            total_winnings = question["prize"]
            print(f"Correct! Your total winnings: Rs. {total_winnings}")
        else:
            print(f"\nWrong answer! The correct answer was {question['answer']}.")
            print(f"Game Over! You take home Rs. {total_winnings}")
            return

        question_number += 1

    # If all questions answered correctly
    print("\n" + "=" * 50)
    print("CONGRATULATIONS! You answered all questions correctly!")
    print(f"You are the CROREPATI! Total winnings: Rs. {total_winnings}")
    print("=" * 50)


# Run the game
if __name__ == "__main__":
    play_game()