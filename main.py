import tkinter

notes = tkinter.Tk()
notes.title("Puffy-notes")
notes.geometry("370x370")
notes.configure(bg ="#FC824E")
title=tkinter.Label(notes, text="Blossom!", bg="#FC824E",font=("Arial",18,"bold"),fg=("#BC0303"))
note = tkinter.Text(notes, width=200, height=215,bg="#F5A2BB", fg="#170202",font=("Arial",12,"bold"))
title.pack(pady=20)
note.pack(pady=10)

notes.mainloop()