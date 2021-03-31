from tkinter import *

root = Tk()
root.title("Entry Boxes")
root.geometry('700x500')

my_label =  Label(root, text = "Enter the number of different frames : ").grid(row = 0 , column = 0 , padx =5, pady = 20)
my_frame_entry = Entry(root, width = 50 , bd = 3).grid(row = 0,column = 1)


def multiple_frames():
    new_label = Label(root, text = my_frame_entry.get())
    new_label.grid(row =4, column = 4)

    
my_confirm_button = Button(root, text = "Confirm", command = multiple_frames, bd = 3).grid(row = 1, column = 0, pady = 10 , padx = 5)


root.mainloop()