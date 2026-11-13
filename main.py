
import tkinter
from PIL import Image, ImageTk

notes = tkinter.Tk()
notes.title("Puffy-notes")
notes.geometry("340x400")
notes.configure(bg="#FC824E")

blossom_img = ImageTk.PhotoImage(Image.open("blossom.png").resize((100, 100)))
buttercup_img = ImageTk.PhotoImage(Image.open("buttercup.png").resize((95, 95)))
bubbles_img = ImageTk.PhotoImage(Image.open("bubbles.png").resize((95, 95)))

button = tkinter.Button(notes, text="Theme", width=8, height=2, font=("Arial", 10, "bold"))

plus_button = tkinter.Button(
    notes, text="+", width=3, height=1,
    font=("Arial", 16, "bold"), command=lambda: add_note()
)

title = tkinter.Label(
    notes, text="Blossom!", bg="#FC824E",
    font=("Arial", 18, "bold"), fg="#BC0303"
)

note = tkinter.Text(
    notes, width=35, height=18,
    bg="#F5A2BB", fg="#170202",
    font=("Arial", 12, "bold")
)

picture = tkinter.Label(notes, image=blossom_img, bg="#FC824E")

picture.place(x=5, y=5)
plus_button.place(x=295, y=5)

button.pack(pady=(50, 10))
title.pack(pady=10)
note.pack(pady=5)

theme = 1

def add_note():
    new_note = tkinter.Toplevel(notes)
    new_note.title("New Note")
    new_note.geometry("300x250")
    new_note.configure(bg="#F5A2BB")

    new_text = tkinter.Text(
        new_note,
        width=30,
        height=12,
        bg="#F5A2BB",
        fg="#170202",
        font=("Arial", 11)
    )
    new_text.pack(padx=10, pady=10, fill="both", expand=True)

def change_theme():
    global theme

    theme += 1

    if theme == 4:
        theme = 1

    if theme == 1:
        notes.configure(bg="#FC824E")
        title.config(text="Blossom!", bg="#FC824E", fg="#BC0303")
        note.config(bg="#F5A2BB", fg="#170202")
        picture.config(image=blossom_img, bg="#FC824E")

    elif theme == 2:
        notes.configure(bg="#111111")
        title.config(text="Buttercup!", bg="#111111", fg="#FAF3F3")
        note.config(bg="#3DC94B", fg="#021702")
        picture.config(image=buttercup_img, bg="#111111")

    elif theme == 3:
        notes.configure(bg="#F9D36A")
        title.config(text="Bubbles!", bg="#F9D36A", fg="#5188B5")
        note.config(bg="#A2D8F5", fg="#021327")
        picture.config(image=bubbles_img, bg="#F9D36A")

button.config(command=change_theme)

notes.mainloop()
