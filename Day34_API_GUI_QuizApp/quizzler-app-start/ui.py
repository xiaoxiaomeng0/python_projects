from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score:0/10")
        self.score_label.grid(row=0, column=1)
        self.score_label.config(bg=THEME_COLOR, fg="white")

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Questions Here", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=40)

        photo_right = PhotoImage(file="images/true.png")
        self.button_right = Button(image=photo_right, highlightthickness=0, command=self.right_icon_click)
        self.button_right.grid(row=2, column=0)

        photo_wrong = PhotoImage(file="images/false.png")
        self.button_wrong = Button(image=photo_wrong, highlightthickness=0, command=self.wrong_icon_click)
        self.button_wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def right_icon_click(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)
        self.window.after(1000, self.get_next_question)

    def wrong_icon_click(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)
        self.window.after(1000, self.get_next_question)

    def give_feedback(self, feedback):
        if feedback:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}/10")
