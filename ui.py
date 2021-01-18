from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Interface:
    def __init__(self, quize_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quize_brain
        self.window.title("Quizzy")
        self.SCORE = 0
        self.window.config(padx=20, pady=20, width=600, height=500, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.t = self.canvas.create_text(150, 125, text="Quizzler!", font=("Arial", 17, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.label = Label(text=f"Score: {self.quiz.score}", pady=20, bg=THEME_COLOR, fg="white",
                           font=("Cursive", 12, "bold"))
        self.label.grid(column=1, row=0)
        self.PIC = PhotoImage(file="images/true.png")
        self.PIC2 = PhotoImage(file="images/false.png")
        self.space = Label(bg=THEME_COLOR)
        self.space.grid(column=0, row=2)
        self.button = Button(image=self.PIC, pady=50, bg=THEME_COLOR, command=self.getnexttrue)
        self.button.grid(column=0, row=3)
        self.button2 = Button(image=self.PIC2, pady=50, bg=THEME_COLOR, command=self.getnextfalse)
        self.button2.grid(column=1, row=3)
        self.getnexttrue()
        self.window.mainloop()

    def getnexttrue(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.t, text=question)
            if self.quiz.check_answer("True"):
                self.label.config(text=f"Score: {self.quiz.score}")
            else:
                self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.t, text=f"You got {self.quiz.score}/{self.quiz.question_number}")

    def getnextfalse(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.t, text=question)
            if self.quiz.check_answer("False"):
                self.label.config(text=f"Score: {self.quiz.score}")
            else:
                self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.t, text=f"You got {self.quiz.score}/{self.quiz.question_number}")

