
import tkinter as tk

operation = ""

def equal():
    global operation
    result = str(eval(operation))
    enter_d.set(result)

def click_btn(number):
    global operation
    operation = operation + str(number)
    enter_d.set(operation)


def clear_btn():
    global operation
    enter_d.set("")
    operation = ""

root = tk.Tk()

root.geometry("300x300")
root.title("calculator")
btn1 = tk.Button(root, width=5, height=2, text="1", command=lambda :click_btn(1))
btn2 = tk.Button(root, width=5, height=2, text="2", command=lambda :click_btn(2))
btn3 = tk.Button(root, width=5, height=2, text="3", command=lambda :click_btn(3))
btn4 = tk.Button(root, width=5, height=2, text="4", command=lambda :click_btn(4))
btn5 = tk.Button(root, width=5, height=2, text="5", command=lambda :click_btn(5))
btn6 = tk.Button(root, width=5, height=2, text="6", command=lambda :click_btn(6))
btn7 = tk.Button(root, width=5, height=2, text="7", command=lambda :click_btn(7))
btn8 = tk.Button(root, width=5, height=2, text="8", command=lambda :click_btn(8))
btn9 = tk.Button(root, width=5, height=2, text="9", command=lambda :click_btn(9))
btn0 = tk.Button(root, width=5, height=2, text="0", command=lambda :click_btn(0))
btnc = tk.Button(root, width=5, height=2, text="c",command=clear_btn)
btndot= tk.Button(root, width=5, height=2, text=".", command=lambda :click_btn("."))
btnplus= tk.Button(root, width=5, height=2, text="+", command=lambda :click_btn("+"))
btnminus= tk.Button(root, width=5, height=2, text="-",command=lambda :click_btn("-"))
btnkob= tk.Button(root, width=5, height=2, text="*", command=lambda :click_btn("*"))
btnbol= tk.Button(root, width=5, height=2, text="/", command=lambda :click_btn("/"))
btnequal= tk.Button(root, width=5, height=2, text="=",command=equal)


enter_d = tk.DoubleVar()
enter = tk.Entry(root, width=20, font=40, textvariable=enter_d)


enter.place(x=20, y=10, )

btn1.place(x=10, y=50)
btn2.place(x=65, y=50)
btn3.place(x=125, y=50)
btn4.place(x=180, y=50)
btn5.place(x=10, y=106)
btn6.place(x=65, y=106)
btn7.place(x=125, y=106)
btn8.place(x=180, y=106)
btn9.place(x=10, y=162)
btn0.place(x=65, y=162)
btnc.place(x=125, y=162)
btndot.place(x=180, y=162)
btnplus.place(x=235, y=50)
btnminus.place(x=235, y=106)
btnkob.place(x=235, y=162)
btnbol.place(x=235, y=220)
btnequal.place(x=125, y=230)

root.mainloop()




