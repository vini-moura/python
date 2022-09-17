from tkinter import *
from tkinter import PhotoImage
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

class Interface:
    def __init__(self,quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Vini's Quizz")
        self.window.config()
        self.window.config(pady=20,padx=20,bg=THEME_COLOR, highlightthickness=0)

        self.score = Label(text= 'Score:', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0,column=1)

        trueImage = PhotoImage(file='./images/true.png')
        self.trueButton = Button(
            command = self.answerTrue,
            image=trueImage,
            bd=0,
            highlightthickness=0,
            activebackground=THEME_COLOR)
        self.trueButton.grid(row=2, column=0)

        falseImage = PhotoImage(file='./images/false.png')
        self.falseButton = Button(
            command= self.ansewerFalse,
            image=falseImage,
            bd=0,
            highlightthickness=0,
            activebackground=THEME_COLOR)
        self.falseButton.grid(row=2,column=1)
        self.canvas = Canvas(width=300,height=250, bg='white')
        self.question = self.canvas.create_text(
            150,
            125,
            text='',
            fill=THEME_COLOR,
            font= FONT,
            width= 280
        )

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
           q = self.quiz.next_question()
           self.score.config(text = f'Score {self.quiz.score}')
           self.canvas.itemconfig(self.question, text = q)
        else:
            self.canvas.itemconfig(self.question,text='The End')
            self.trueButton.config(state='disabled')
            self.falseButton.config(state='disabled')

    def answerTrue(self):
       self.feedback(self.quiz.check_answer('True'))

    def ansewerFalse(self,):
        correct = self.quiz.check_answer('False')
        self.feedback(correct)

    def feedback(self, correct):
        if correct:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)