import tkinter as tk  
from functools import partial  
   
   
def call_result(label_result, n1, n2 , n3):
    DiffFrames = int(n1.get())
    l = int(n2.get())
    w = int(n3.get())
    n = 4
    length = [l,l,w,w]
    c = 5490
    res = 0  
    bin_rem = [0]*n 

    for i in range(n): 
        j = 0 
        min = c + 1 
        bi = 0 
        for j in range(res): 
            if (bin_rem[j] >= length[i] and bin_rem[j] - length[i] < min): 
                bi = j 
                min = bin_rem[j] - length[i] 
        if (min == c + 1): 
            bin_rem[res] = c - length[i] 
            res += 1 
        else:
            bin_rem[bi] -= length[i] 
    label_result.config(text="Result = %d" % res)  
    return  
   
root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()
number3 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="Enter different type of frames").grid(row=1, column=0)  
  
labelNum2 = tk.Label(root, text="Enter length").grid(row=2, column=0)

labelNum3 = tk.Label(root, text="Enter width").grid(row=3, column=0)
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=10, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=4)  
  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=4)  

entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=4)
  
call_result = partial(call_result, labelResult, number1, number2, number3)  
  
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=10, column=0)  
  
root.mainloop() 