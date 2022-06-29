# Python Project - Language Translator
# Aastha, Ankita, Nancy, Vaishnavi

from googletrans import Translator
from tkinter import *

window = Tk()
window.geometry('1000x560')
window.config(bg="maroon")
set_bg = PhotoImage(file="image1.png")

# To add image to background.
label_1 = Label(window, image=set_bg)
label_1.place(x=0, y=0)

# To take input
e1 = Entry(window, bg="white", fg="maroon", font=("Times New Roman", 14))
e1.place(x=320, y=120)


# User-defined function to convert text to languages.
def convert_language():
    convert = '\0'
    a1 = e1.get()
    t1 = Translator()
    t2 = click_option.get()

    if t2 == "English":
        convert = "en"
    elif t2 == "Hindi":
        convert = "hi"
    elif t2 == "Telugu":
        convert = "te"
    elif t2 == "Malayalam":
        convert = "ml"
    elif t2 == "German":
        convert = "de"
    elif t2 == "French":
        convert = "fr"
    elif t2 == "Spanish":
        convert = "es"
    elif t2 == "Russian":
        convert = "ru"

    trans_text = t1.translate(a1, dest=convert)
    trans_text = trans_text.text
    label_3.config(text=trans_text)


# To display in list.
choices = [
    "English",
    "Hindi",
    "Telugu",
    "Malayalam",
    "German",
    "French",
    "Spanish",
    "Russian"
]

click_option = StringVar()
click_option.set("Select Language")

list_drop = OptionMenu(window, click_option, *choices)
list_drop.configure(background="teal", foreground="white", font=("Times New Roman", 13))
list_drop.place(x=520, y=114)

label_2 = Label(window, text="\t\t\t\t\t\t\t\t\t\t", bg="white", fg="maroon", font=("Times New Roman", 14))
label_2.place(x=138, y=400)
label_3 = Label(window, text="Translated Text", bg="white", fg="maroon", font=("Times New Roman", 14))
label_3.place(x=140, y=400)

Button_1 = Button(window, text="TRANSLATE", bg="fuchsia", fg="white", font=("Times New Roman", 14, "bold"),
                  command=convert_language)
Button_1.place(x=425, y=255)

window.mainloop()