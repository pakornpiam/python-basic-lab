from tkinter import * ## * import all function in tkinter main 
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title("COCONUT PRICE")
GUI.geometry('500x300')

bg = PhotoImage(file = 'coconut.png')
BG = Label(GUI, image=bg )
BG.pack()

L = Label(GUI, text = 'QTY', font=(None, 20))
L.pack()

v_qty= StringVar() # store input data
E1 = ttk.Entry(GUI, textvariable= v_qty, font=(None,20))
E1.pack()


def CAL():
    try:
        quan = float (v_qty.get())
        calc = quan * 9 # 9 baht per fruit
        messagebox.showinfo('TOTAL PRICE', 'TOTAL COCONUT PRICE{} Baht'.format(calc))
        v_qty.set('1') ### set QTY to 1
    except:
        messagebox.showwarning(' !!PLS PUT ONLY NUMBER!!','tryagain')
        v_qty.set('1') ### set QTY to 1 

B=ttk.Button(GUI, text= 'Calculate',command=CAL)
B.pack(ipadx=30, ipady=20, pady=20) # ipadx extend x /y

GUI.mainloop()# keep program runong all the time 