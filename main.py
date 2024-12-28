from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Quick Notes")

text = Text() 
label = Label(text="Write the file name in the single line entry and the notes in text box")
entry = Entry()

def main():
    with open (entry.get(), 'a') as file:
        file.write(text.get())
button = Button(text="save", bg = 'white', fg = "black")

#packing everything up
label.place(width=600)
entry.place(width=100,height=50,x=100,y=40)
text.place(width=400,height=400,x=100,y=100)
button.place(width=100,height=20, x=100,y=80)

root.mainloop()

        