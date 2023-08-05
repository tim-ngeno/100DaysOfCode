"""The questions module"""


class Question:
    """Defines a question class"""

    def __init__(self, text, answer):
        """
        Initializes the Question class
        Attributes:
            text (str): represents the question
            answer (str): represents an answer to the question
        """
        self.text = text
        self.answer = answer
