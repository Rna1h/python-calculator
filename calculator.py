import tkinter as tk


def action(x):
    global li
    try:
        """li takes the last value from calculator to check operator collapsing"""
        li = label1["text"][-1]
    except:
        pass
    finally:
        if x == 'C':
            label1["text"] = " "

        elif x in ['+', '-', '/', '*']:
            """it checks if two or more operators are collapsing or not"""
            if li in ['+', '-', '/', '*']:
                pass
            else:
                label1["text"] = str(label1["text"]) + str(x)

        else:
            label1["text"] = str(label1["text"]) + str(x)


def cal():
    try:
        """ it evaluates the string expression to perform the mathematical function """
        label1['text'] = str(eval(label1['text']))
    except:
        label1['text'] = '0'
        pass


window = tk.Tk()
window.title("Calculator")
window.rowconfigure(0, minsize=80, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

"""calculator window"""
label1 = tk.Label(master=window, text=" ")
label1.grid(row=0, column=3, sticky="nswe")

"""Column 1"""
btn1 = tk.Button(master=window, text=1, width=5, height=3, command=lambda: action(1))
btn1.grid(row=1, column=0, sticky="nswe")
btn2 = tk.Button(master=window, text=5, width=5, height=3, command=lambda: action(5))
btn2.grid(row=2, column=0, sticky="nswe")
btn3 = tk.Button(master=window, text='+', width=5, height=3, command=lambda: action('+'))
btn3.grid(row=3, column=0, sticky="nswe")
btn4 = tk.Button(master=window, text='*', width=5, height=3, command=lambda: action('*'))
btn4.grid(row=4, column=0, sticky="nswe")

"""Column 2"""
btn6 = tk.Button(master=window, text=2, width=5, height=3, command=lambda: action(2))
btn6.grid(row=1, column=1, sticky="nswe")
btn7 = tk.Button(master=window, text=6, width=5, height=3, command=lambda: action(6))
btn7.grid(row=2, column=1, sticky="nswe")
btn8 = tk.Button(master=window, text="-", width=5, height=3, command=lambda: action('-'))
btn8.grid(row=3, column=1, sticky="nswe")
btn9 = tk.Button(master=window, text="/", width=5, height=3, command=lambda: action('/'))
btn9.grid(row=4, column=1, sticky="nswe")

"""Column 3"""
btn11 = tk.Button(master=window, text=3, width=5, height=3, command=lambda: action(3))
btn11.grid(row=1, column=2, sticky="nswe")
btn12 = tk.Button(master=window, text=7, width=5, height=3, command=lambda: action(7))
btn12.grid(row=2, column=2, sticky="nswe")
btn13 = tk.Button(master=window, text=0, width=5, height=3, command=lambda: action(0))
btn13.grid(row=3, column=2, sticky="nswe")
btn14 = tk.Button(master=window, text="C", width=5, height=3, command=lambda: action('C'))
btn14.grid(row=4, column=2, sticky="nswe")

"""Column 4"""
btn16 = tk.Button(master=window, text=4, width=5, height=3, command=lambda: action(4))
btn16.grid(row=1, column=3, sticky="nswe")
btn17 = tk.Button(master=window, text=8, width=5, height=3, command=lambda: action(8))
btn17.grid(row=2, column=3, sticky="nswe")
btn18 = tk.Button(master=window, text=9, width=5, height=3, command=lambda: action(9))
btn18.grid(row=3, column=3, sticky="nswe")
btn19 = tk.Button(master=window, text='=', width=5, height=3, command=cal)
btn19.grid(row=4, column=3, sticky="nswe")

window.mainloop()
