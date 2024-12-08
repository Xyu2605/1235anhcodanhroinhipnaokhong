from tkinter import *
import random

WIDTH = 420
HEIGHT = 210
Background = "#fb6f92"

def window_yes():
    popup = Toplevel()
    popup.title("Love")
    popup.geometry("210x160")

    icon = PhotoImage(file = "heart.png")
    popup.iconphoto(True, icon)

    popup.config(bg = Background)

    label = Label(popup, text = "I Love You", bg = Background, font = ("Noto Sans",18))
    label.pack(expand = True)

    x = random.randint(0,popup.winfo_screenwidth() - 280)
    y = random.randint(0,popup.winfo_screenheight() - 160)
    popup.geometry(f"320x160+{x}+{y}")


def Yes(count = 60, delay = 150 ):
    if count > 0:
        window_yes()
        window.after(delay, Yes, count - 1, delay)
    
def move_button(event):
    btn_x = button1.winfo_x()
    btn_y = button1.winfo_y()

    new_x = random.randint(0, WIDTH - 200 - button1.winfo_width())
    new_y = random.randint(0, HEIGHT - 150 - button1.winfo_height())
    if abs(new_x - btn_x) < 50 or abs(new_y - btn_y) < 50:
        new_x = (new_x + 100) % WIDTH
        new_y = (new_y + 100) % HEIGHT

    button1.place(x = new_x, y = new_y)



def main_window():
    global window
    window = Tk()
    window.title("HiHi")
    window.geometry("420x210")

    icon = PhotoImage(file = "heart.png")
    window.iconphoto(True, icon)

    window.config(bg = Background)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    pos_x = int((screen_width / 2) - WIDTH)
    pos_y = int((screen_height / 2) - HEIGHT)
    
    window.geometry(f"{WIDTH}x{HEIGHT}+{pos_x}+{pos_y}")

    label = Label(window, text = "Do you love me ?", bg = Background, font =("Noto Sans",24))
    label.place(x = 85 ,y = 50)

    global button1 
    button1 = Button(window, text= "No", bg = Background, font = ("Noto Sans",18))
    button1.place(x = 80, y = 130)
    button1.bind("<Enter>", move_button)

    button2 = Button(window, text= "Yes", bg = Background, font = ("Noto Sans",18), command = Yes)
    button2.place(x = WIDTH - 138, y = 130)

    window.mainloop()

main_window()