from tkinter import *
import pandas
import random

window = Tk()
canvas = Canvas(width=800, height=526)

with open('dados flashcards.csv', newline='') as f:
    dados = pandas.read_csv(f, delimiter=';')

dados = dados.to_dict(orient='records')

cartao = {}
# Functions ----------------------------------------------
def next_card():
    global cartao
    cartao = random.choice(dados)
    canvas.itemconfig(canvasImage, image=frontImage)
    canvas.itemconfig(t1, text='French')
    canvas.itemconfig(t2, text=cartao['word'])


def wrong_action():
    canvas.itemconfig(canvasImage, image=backImage)
    canvas.itemconfig(t1, text='Português')
    canvas.itemconfig(t2, text=cartao['Translation'])
    window.after(3000, next_card)


# Variables ------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
frontImage = PhotoImage(file="card_front.png")
backImage = PhotoImage(file='card_back.png')
rightImage = PhotoImage(file='right.png')
wrongImage = PhotoImage(file='wrong.png')

# GUI items ----------------------------------------------
canvasImage = canvas.create_image(400, 263, image=frontImage)
t1 = canvas.create_text(400, 150, text='Language', font=("Ariel", 40, "italic"))
t2 = canvas.create_text(400, 263, text='Word', font=("Ariel", 40, "bold"))
rightButton = Button(image=rightImage, highlightthickness=0, command=next_card)
wrongButton = Button(image=wrongImage, highlightthickness=0, command=wrong_action)

# GUI configs --------------------------------------------
window.title('flashy')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
rightButton.config(pady=50, padx=50)
wrongButton.config(pady=50, padx=50)

canvas.grid(column=1, row=1, columnspan=2)
wrongButton.grid(column=1, row=2)
rightButton.grid(column=2, row=2)

# Calling functions -------------------------------------
next_card()

window.mainloop()