from tkinter import *

root = Tk()
root.title("Entry Boxes")
root.geometry('700x500')

ask = Label(root , text = 'The total different number of frames').grid(row = 0, column = 0)

e = Entry(root, width = 50)
e.grid(row = 0, column = 1)


def click():
    widht_list = []
    length_list = []
    quantity_list = []

    def c():
        print(widht_list, length_list, quantity_list)



    row = int(e.get())
    b= Button(root, text = 'cc', command = c).grid(row = row + 2, column = 0)
    for i in range(row):
        width = Entry(root)
        width.grid(row = i+2, column = 0)
        widht_list.append(width.get())

        length = Entry(root)
        length.grid(row = i+2 , column = 1)
        length_list.append(length.get())

        quantity = Entry(root)
        quantity.grid(row = i+2, column = 2)
        quantity_list.append(quantity.get())
    
    


button = Button(root , text = 'click me!', command = click)
button.grid(row = 1, column = 0)

root.mainloop()