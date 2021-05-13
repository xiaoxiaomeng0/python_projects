from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
rand_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    new_data = data.to_dict(orient="records")


def word_gen():
    global rand_card, flip_timer
    window.after_cancel(flip_timer)
    rand_card = random.choice(new_data)
    canvas.itemconfig(image_bg, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=rand_card["French"], fill="black")
    flip_timer = window.after(3000, switch)


def right_answer():
    new_data.remove(rand_card)
    data_frame = pandas.DataFrame(new_data)
    data_frame.to_csv("data/words_to_learn.csv", index=False)
    word_gen()


def switch():
    canvas.itemconfig(image_bg, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=rand_card["English"], fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, switch)


# The example did it with converting the dataframe into map.

# def word_gen():
#     global rand_index, flip_timer
#     window.after_cancel(flip_timer)
#     rand_index = random.randint(0, len(data.index)-1)
#     canvas.itemconfig(image_bg, image=card_front)
#     canvas.itemconfig(title, text="French", fill="black")
#     canvas.itemconfig(word, text=data.iloc[rand_index].French, fill="black")
#     flip_timer = window.after(3000, switch)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
image_bg = canvas.create_image(400, 263)

title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file="./images/wrong.png")
button_x = Button(image=x_image, highlightthickness=0, command=word_gen)
button_x.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=right_answer)
button_right.grid(row=1, column=1)

word_gen()

window.mainloop()
