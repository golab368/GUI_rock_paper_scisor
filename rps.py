from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Rock Paper Scissors')
root.geometry("400x700")
txt = 'Rock Paper Scissors'

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

def game():
    game = {1:"Stone",2:"Paper",3:"Scisors"}
    random_result = random.choice(list(game.values()))
    return random_result

def button_b1(b):
    global txt
    random_result = game()
    if b1["text"] == random_result :
        tie = messagebox.showinfo(txt,f"Its Tie Try Again!\n\n{b['text']} tie with {random_result}")
        disable_all_buttons()
    elif b1["text"] and random_result == "Scisors":
        win = messagebox.showinfo(txt,f"You won\n\n{b['text']} won with {random_result}")
        disable_all_buttons()
    elif b1["text"] and random_result == "Paper":
        lost = messagebox.showinfo(txt,f"You lost\n\n{random_result} won with {b['text']}")
        disable_all_buttons()

def button_b2(b):
    global txt
    random_result = game()
    if b2["text"] == random_result:
        tie = messagebox.showinfo(txt,f"Its Tie Try Again!\n\n{b['text']} tie with {random_result}")
        disable_all_buttons()
    elif b2["text"] and random_result == "Stone":
        win = messagebox.showinfo(txt,f"You won\n\n{b['text']} won with {random_result}")
        disable_all_buttons()
    elif b2["text"] and random_result == "Scisors":
        lost = messagebox.showinfo(txt,f"You lost\n\n{random_result} won with {b['text']}")
        disable_all_buttons()
   
def button_b3(b):
    global txt
    random_result = game()
    if b3["text"] == random_result:
        tie = messagebox.showinfo(txt,f"Its Tie Try Again!\n\n{b['text']} tie with {random_result}")
        disable_all_buttons()
    elif b3["text"] and random_result == "Paper":
        win = messagebox.showinfo(txt,f"You won\n\n{b['text']} won with {random_result}")
        disable_all_buttons()
    elif b3["text"] and random_result == "Stone":
        lost = messagebox.showinfo(txt,f"You lost\n\n{random_result} won with {b['text']}")
        disable_all_buttons()


stone = PhotoImage(file = r"stone.png")
paper = PhotoImage(file = r"paper.png")
scisors = PhotoImage(file = r"scissors.png")
reset_icon = PhotoImage(file = r"arrows-circle.png")

def reset():
    global b1,b2,b3
    b1 = Button(root, text="Stone",  image = stone, command=lambda: button_b1(b1))
    b2 = Button(root, text="Paper", image = paper,  command=lambda: button_b2(b2))
    b3 = Button(root, text="Scisors", image = scisors, command=lambda: button_b3(b3))

    b1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')
    b2.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.2, anchor='n')
    b3.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.2, anchor='n')

    button_to_reset = Button(root, image=reset_icon, command=reset)
    button_to_reset.place(relx=0.5, rely=0.75, relwidth=0.35, relheight=0.2, anchor='n')

reset()

root.mainloop()