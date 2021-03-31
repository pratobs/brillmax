import tkinter
import tkinter.ttk
import tkinter.messagebox


class MainWindow:
    def __init__(self, n):
        self.window = tkinter.Tk()
        self.window.wm_title("Insert data")

        self.n = n
        self.widthList = []
        self.lengthList = []
        self.quantityList = []

        self.addEntries(n)
        self.window.mainloop()

        tkinter.Button(self.window, width=20, text="Insert", command=self.submitEntries).grid(
            pady=15, padx=5, column=1, row=1
        )

    def addEntries(self, n):
        for i in range(n):
            width = tkinter.StringVar()
            length = tkinter.StringVar()
            quantity = tkinter.StringVar()

            widthEntry = tkinter.Entry(
                self.window, width=25, textvariable=width
            )
            widthEntry.grid(pady=5, column=1, row=i+2)
            self.widthList.append(widthEntry)

            lengthEntry = tkinter.Entry(
                self.window, width=25, textvariable=length
            )
            lengthEntry.grid(pady=5, column=2, row=i+2)
            self.lengthList.append(lengthEntry)

            quantityEntry = tkinter.Entry(
                self.window, width=25, textvariable=quantity
            )
            quantityEntry.grid(pady=5, column=3, row=i+2)
            self.quantityList.append(quantityEntry)

    def submitEntries(self):
        widthList = self.widthList
        lengthList = self.lengthList
        quantityList = self.quantityList
        widths = []
        for width in widthList:
            widths.append(width.get())

        lengths = []
        for length in lengthList:
            lengths.append(length.get())

        quantities = []
        for quantity in quantityList:
            quantities.append(quantity.get())

        print(widths, lengths, quantities)


class HomePage:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.wm_title("BRILLMAX")

        tkinter.Label(self.window, text="Number of different frames", width=25).grid(
            pady=5, column=1, row=1
        )
        self.nEntry = tkinter.Entry(self.window, width=25)
        self.nEntry.grid(pady=5, column=2, row=1)
        tkinter.Button(self.window, width=20, text="Calculate", command=self.calculate).grid(
            pady=15, padx=5, column=3, row=1
        )

        self.window.mainloop()

    def calculate(self):
        self.n = int(self.nEntry.get())
        self.mainWindow = MainWindow(self.n)


homePage = HomePage()
