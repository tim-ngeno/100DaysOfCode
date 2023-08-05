"""Create question objects from question data"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = [
    Question(q["question"], q["correct_answer"]) for q in question_data
]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    quiz.question_number += 1

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
