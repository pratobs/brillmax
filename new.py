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

            tkinter.Button(self.window, width=20, text="Calculate", command=self.submitEntries).grid(
            pady=15, padx=5, column=1, row=1
        )

    def submitEntries(self):
        total = []
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

        
        l =  len(widths)
        for j  in range(l):
            for z in range(int(quantities[j]*2)):
                total.append(int(widths[j]))
                total.append(int(lengths[j]))

        res = 0
        n = len(total)
        r = 5000
    
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
            min = r + 1
            bi = 0
    
            for jay in range(res):
                if (bin_rem[jay] >= total[ai] and bin_rem[jay] -
                                        total[ai] < min):
                    bi = jay
                    min = bin_rem[jay] - total[ai]
                
            # If no bin could accommodate total[ai],
            # create a new bin
            if (min == r + 1):
                bin_rem[res] = r - total[ai]
                res += 1
            else: # Assign the item to best bin
                bin_rem[bi] -= total[ai]

        tkinter.Label( self.window, text = ("The total number of bar would require:",res)).grid(column = 1, row = l+3)

class HomePage:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.wm_title("BRILLMAX")

        tkinter.Label(self.window, text="Number of different frames", width=25).grid(
            pady=5, column=1, row=1
        )
        self.nEntry = tkinter.Entry(self.window, width=25)
        self.nEntry.grid(pady=5, column=2, row=1)
        tkinter.Button(self.window, width=20, text="Insert", command=self.calculate).grid(
            pady=15, padx=5, column=3, row=1
        )

        self.window.mainloop()

    def calculate(self):
        self.n = int(self.nEntry.get())
        self.mainWindow = MainWindow(self.n)


homePage = HomePage()