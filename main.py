import tkinter
from PIL import Image, ImageTk

notes = tkinter.Tk()
notes.withdraw()

blossom_img = ImageTk.PhotoImage(Image.open("blossom.png").resize((100, 100)))
buttercup_img = ImageTk.PhotoImage(Image.open("buttercup.png").resize((95, 95)))
bubbles_img = ImageTk.PhotoImage(Image.open("bubbles.png").resize((95, 95)))

all_notes = []


def get_theme_details(theme):
    if theme == 1:
        return "#FC824E", "#F5A2BB", "#170202", "Blossom!", "#BC0303", blossom_img

    elif theme == 2:
        return "#111111", "#3DC94B", "#021702", "Buttercup!", "#FAF3F3", buttercup_img

    else:
        return "#F9D36A", "#A2D8F5", "#021327", "Bubbles!", "#5188B5", bubbles_img


def cursor_effect(text_area):
    text_area.config(insertontime=0)

    text_area.bind(
        "<Enter>",
        lambda event: text_area.config(insertontime=600)
    )

    text_area.bind(
        "<Leave>",
        lambda event: text_area.config(insertontime=0)
    )


def check_windows():
    for item in all_notes:
        if item["window"].winfo_exists():
            return

    notes.destroy()


def create_note(theme=1, content=""):

    if theme not in (1, 2, 3):
        theme = 1

    new_note = tkinter.Toplevel(notes)

    x = 100 + (len(all_notes) % 6) * 30
    y = 100 + (len(all_notes) % 6) * 30

    new_note.geometry(f"340x400+{x}+{y}")

    window_bg, note_bg, note_fg, title_text, title_fg, character_img = get_theme_details(theme)

    new_note.title("Puffy-notes | " + title_text)
    new_note.configure(bg=window_bg)

    top_frame = tkinter.Frame(
        new_note,
        bg=window_bg
    )

    top_frame.pack(fill="x")

    new_picture = tkinter.Label(
        top_frame,
        image=character_img,
        bg=window_bg
    )

    new_picture.pack(side="left", padx=5)

    button_frame = tkinter.Frame(
        top_frame,
        bg=window_bg
    )

    button_frame.pack(side="right", padx=5)

    plus_button = tkinter.Button(
        button_frame,
        text="+",
        width=3,
        font=("Arial", 14, "bold"),
        command=lambda: create_note(1)
    )

    plus_button.pack(side="left", padx=2)

    theme_button = tkinter.Button(
        button_frame,
        text="Theme",
        font=("Arial", 9, "bold")
    )

    theme_button.pack(side="left", padx=2)

    new_title = tkinter.Label(
        new_note,
        text=title_text,
        bg=window_bg,
        font=("Arial", 18, "bold"),
        fg=title_fg
    )

    new_title.pack(pady=5)

    new_text = tkinter.Text(
        new_note,
        width=35,
        height=12,
        bg=note_bg,
        fg=note_fg,
        font=("Arial", 12, "bold")
    )

    new_text.pack(
        padx=5,
        pady=5,
        fill="both",
        expand=True
    )

    new_text.insert("1.0", content)

    cursor_effect(new_text)

    item = {
        "window": new_note,
        "text": new_text,
        "theme": theme
    }

    all_notes.append(item)

    def change_theme():
        item["theme"] += 1

        if item["theme"] > 3:
            item["theme"] = 1

        bg, text_bg, text_fg, name, color, image = get_theme_details(item["theme"])

        new_note.configure(bg=bg)
        top_frame.configure(bg=bg)
        button_frame.configure(bg=bg)
        new_picture.configure(image=image, bg=bg)
        new_title.configure(text=name, bg=bg, fg=color)
        new_text.configure(bg=text_bg, fg=text_fg)

        new_note.title("Puffy-notes | " + name)

    theme_button.config(command=change_theme)

    def delete_note():
        if item in all_notes:
            all_notes.remove(item)
        new_note.destroy()
        check_windows()

    delete_button = tkinter.Button(
        new_note,
        text="🗑 Delete",
        command=delete_note,
        font=("Arial", 10, "bold"),
        bg="#FF6B6B",
        fg="white"
    )

    delete_button.pack(side="bottom", pady=8)

    new_note.protocol(
        "WM_DELETE_WINDOW",
        delete_note
    )

    return new_note
create_note(1)
notes.mainloop()