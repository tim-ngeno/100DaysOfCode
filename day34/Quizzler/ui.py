import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """Creates the blueprint for the quizzler user interface."""

    def __init__(self, quiz_brain: QuizBrain):
        """Initializes the class"""
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score label
        self.score_label = tkinter.Label(
            text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(
            image=true_image, highlightthickness=0, command=self.click_true
        )
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(
            image=false_image, highlightthickness=0, command=self.click_false
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Gets the next question from quiz brain"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.canvas_text, fill=THEME_COLOR)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="The End!", fill=THEME_COLOR)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def click_true(self):
        """Checks if user clicked True and got answer right"""
        self.give_feedback(self.quiz.check_answer("True"))

    def click_false(self):
        """Checks if user clicked false button and output"""
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, answer):
        """Gives feedback to the user based on the correctness of their
        answer"""
        print(answer)
        if answer:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.canvas_text, fill="white")

        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.canvas_text, fill="white")
        self.window.after(1000, self.get_next_question)
