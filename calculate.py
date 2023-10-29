from tkinter import *
root = Tk()
root.title("Calculute")

content = ""
txt_input = StringVar(value = "0")

def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

def equal():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)
    content = ""
def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"0")
#เเสดงผล 5 x 4
display = Entry(font=('arial',30,'bold'),fg="white",bg="green",textvariable=txt_input,justify="right")
display.grid(columnspan=4)
#รับค่าผ่านปุ่ม
btn7 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(7),text="7",padx=30,pady=15).grid(row=1,column=0)
btn8 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(8),text="8",padx=30,pady=15).grid(row=1,column=1)
btn9 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(9),text="9",padx=30,pady=15).grid(row=1,column=2)
btnc = Button(fg="black",bg="orange",font=('arial',30,'bold'),command = clear,text="C",padx=30,pady=15).grid(row=1,column=3)


btn4 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(4),text="4",padx=30,pady=15).grid(row=2,column=0)
btn5 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(5),text="5",padx=30,pady=15).grid(row=2,column=1)
btn6 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(6),text="6",padx=30,pady=15).grid(row=2,column=2)
btnplus = Button(fg="black",bg="orange",font=('arial',30,'bold'),command=lambda:btn("+"),text="+",padx=30,pady=15).grid(row=2,column=3)


btn1 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(1),text="1",padx=30,pady=15).grid(row=3,column=0)
btn2 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(2),text="2",padx=30,pady=15).grid(row=3,column=1)
btn3 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(3),text="3",padx=30,pady=15).grid(row=3,column=2)
btnminus = Button(fg="black",bg="orange",font=('arial',30,'bold'),command=lambda:btn("-"),text="-",padx=35,pady=15).grid(row=3,column=3)

btndot = Button(fg="black",font=('arial',30,'bold'),text=".",padx=30,pady=15).grid(row=4,column=0)
btn0 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(0),text="0",padx=35,pady=15).grid(row=4,column=1)
btndivision = Button(fg="black",bg="orange",font=('arial',30,'bold'),command=lambda:btn("/"),text="/",padx=35,pady=15).grid(row=4,column=2)
btnmultiply = Button(fg="black",bg="orange",font=('arial',30,'bold'),command=lambda:btn("*"),text="x",padx=30,pady=15).grid(row=4,column=3)

btnqual= Button(fg="black",bg="green",font=('arial',30,'bold'),command=equal,text="=",padx=95,pady=15).grid(row=5,column=0,columnspan=2)
btnopen = Button(fg="black",bg="orange",font=('arial',30,'bold'),command=lambda:btn("("),text="(",padx=35,pady=15).grid(row=5,column=2)
btnclose = Button(fg="black",bg="orange",font=('arial',30,'bold'),command=lambda:btn(")"),text=")",padx=35,pady=15).grid(row=5,column=3)

root.mainloop()