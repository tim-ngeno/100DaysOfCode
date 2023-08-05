"""Create the QuizBrain class"""
import html


class QuizBrain:
    """Defines the quizbrain class"""

    def __init__(self, q_list):
        """Initializes the QuizBrain class"""
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Checks if questions list still has questions
        Returns:
            True: if there are still questions
            False: if there are no more questions
        """
        return self.question_number + 1 <= len(self.question_list)

    def next_question(self):
        """Retrieves next question from list and asks for answer"""
        current_q = self.question_list[self.question_number]
        user_answer = input(
            f"Q.{self.question_number + 1}: {html.unescape(current_q.text)} (True/False)\n")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        """Compares the user answer and the correct answer"""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer was {correct_answer}")
        print(
            f"Your current score is: {self.score}/{self.question_number + 1}")
        print()
