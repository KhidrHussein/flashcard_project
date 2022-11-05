from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

# Opening the French words file
try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")

current_card = {}


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    print(len(data))
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

# UI
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
right_button_image = PhotoImage(file="./images/right.png")
wrong_button_image = PhotoImage(file="./images/wrong.png")

card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="")
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="")
canvas.grid(column=0, row=0, columnspan=2)

known_button = Button(image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
known_button.grid(column=1, row=1)
unknown_button = Button(image=wrong_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
