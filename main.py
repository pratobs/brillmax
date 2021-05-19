import tkinter
import tkinter.ttk
import tkinter.messagebox


class MainWindow:
    def __init__(self, n, r, k):
        self.window = tkinter.Tk()
        self.window.wm_title("Insert data")

        self.n = n
        self.r = r
        self.k = k
        self.widthList = []
        self.lengthList = []
        self.quantityList = []

        self.addEntries(n)
        self.window.mainloop()

    def addEntries(self, n):
        tkinter.Label(self.window, text="Lenth").grid(column=1, row=0)
        tkinter.Label(self.window, text="Width").grid(column=2, row=0)
        tkinter.Label(self.window, text="Quantity").grid(column=3, row=0)

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

        tkinter.Button(self.window, width=20, text="Calculate", command=self.submitEntries).grid(
            pady=15, padx=5, column=1, row=i+3
        )

    def submitEntries(self):
        widthList = self.widthList
        lengthList = self.lengthList
        quantityList = self.quantityList
        widths = []
        for width in widthList:
            widths.append(int(width.get()))
        lengths = []
        for length in lengthList:
            lengths.append(int(length.get()))
        quantities = []
        for quantity in quantityList:
            quantities.append(int(quantity.get()))

        total = []
        l = len(widths)
        for j in range(l):
            for z in range(quantities[j]*2):
                total.append(int(widths[j]))
                total.append(int(lengths[j]))
        # print(total)

        res = 0
        n = len(total)

        # Create an array to store
        # remaining space in bins
        # there can be at most n bins

        bin_rem = [0]*n

        # Place items one by one
        for ai in range(n):

            # Find the first bin that
            # can accommodate
            # total[ai]
            jay = 0

            # Initialize minimum space
            # left and index
            # of best bin
            min = self.r + 1
            bi = 0

            for jay in range(res):
                if (bin_rem[jay] >= total[ai] and bin_rem[jay] -
                        total[ai] < min):
                    bi = jay
                    min = bin_rem[jay] - total[ai]

            # If no bin could accommodate total[ai],
            # create a new bin
            if (min == self.r + 1):
                bin_rem[res] = self.r - total[ai]
                res += 1
            else:  # Assign the item to best bin
                bin_rem[bi] -= total[ai]

        tkinter.Label(self.window, text=(
            "The total number of bar would require:", res)).grid(column=1, row=l+3)


class HomePage:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.wm_title("BRILLMAX")

        tkinter.Label(self.window, text="Number of different frames: ", width=25).grid(
            pady=5, column=1, row=1
        )
        tkinter.Label(self.window, text="The length of the raw material: ", width=25).grid(
            pady=5, column=1, row=2
        )
        tkinter.Label(self.window, text="The kerf size: ", width=25).grid(
            pady=5, column=1, row=3
        )

        self.nEntry = tkinter.Entry(self.window, width=25)
        self.nEntry.grid(pady=5, column=2, row=1)

        self.rEntry = tkinter.Entry(self.window, width=25)
        self.rEntry.grid(pady=5, column=2, row=2)

        self.kEntry = tkinter.Entry(self.window, width=25)
        self.kEntry.grid(pady=5, column=2, row=3)

        tkinter.Button(self.window, width=20, text="Insert", command=self.calculate).grid(
            padx=5, column=3, row=3
        )

        self.window.mainloop()

    def calculate(self):
        self.n = int(self.nEntry.get())
        self.r = int(self.rEntry.get())
        self.k = int(self.kEntry.get())
        self.mainWindow = MainWindow(self.n, self.r, self.k)


homePage = HomePage()
