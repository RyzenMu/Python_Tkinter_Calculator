import tkinter
from tkinter import *

frame = Tk()

frame = Frame(frame, bg='blue', width=500, height=500)
frame.grid(row=0, column=0)

entry = Entry(frame, width=40)
entry.grid(row=1, column=(1), columnspan=8)

button_1 = Button(frame, text='1', fg='black', width=10)
button_1.grid(row = 2, column=0)

button_2 = Button(frame, text='2', fg='black', width=10)
button_2.grid(row = 2, column=1)

button_3 = Button(frame, text='3', fg='black', width=10)
button_3.grid(row = 2, column=2)

button_plus = Button(frame, text='+', fg='black', width=10)
button_plus.grid(row = 2, column=3)

button_4 = Button(frame, text='4', fg='black', width=10)
button_4.grid(row = 3, column=0)

button_5 = Button(frame, text='5', fg='black', width=10)
button_5.grid(row = 3, column=1)

button_6 = Button(frame, text='6', fg='black', width=10)
button_6.grid(row = 3, column=2)

button_minus = Button(frame, text='-', fg='black', width=10)
button_minus.grid(row = 3, column=3)

button_7 = Button(frame, text='7', fg='black', width=10)
button_7.grid(row = 4, column=0)

button_8 = Button(frame, text='8', fg='black', width=10)
button_8.grid(row = 4, column=1)

button_9 = Button(frame, text='9', fg='black', width=10)
button_9.grid(row = 4, column=2)

button_multiply = Button(frame, text='*', fg='black', width=10)
button_multiply.grid(row = 4, column=3)

button_divide = Button(frame, text='/', fg='black', width=10)
button_divide.grid(row = 5, column=0)

button_equal = Button(frame, text='=', fg='black', width=10)
button_equal.grid(row = 5, column=1, columnspan=6)

frame.mainloop()