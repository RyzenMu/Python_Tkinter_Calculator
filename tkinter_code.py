
from tkinter import *

frame = Tk()
frame.title('Simple Calculator')
frame.geometry('700x500')

first_number = 0

def func(args):
    # entry.insert(0, args)
    entry.insert(END, args)


def clear():
    # entry.set = ""
    entry.delete(0, END)

def add():
    first_number = entry.get()
    entry.delete(0, END)
    with open ('temp.txt', 'a') as f:
        f.write(first_number+'+')

def sub():
    first_number = entry.get()
    entry.delete(0, END)
    with open ('temp.txt', 'a') as f:
        f.write(first_number+'-')

def mul():
    first_number = entry.get()
    entry.delete(0, END)
    with open ('temp.txt', 'a') as f:
        f.write(first_number+'*')

def div():
    first_number = entry.get()
    entry.delete(0, END)
    with open ('temp.txt', 'a') as f:
        f.write(first_number+'/')

def equ():
    first_number = entry.get()
    entry.delete(0, END)
    with open ('temp.txt', 'a') as f:
        f.write(first_number)

    with open ('temp.txt', 'r') as g:
        expression = g.read()
        # getting full number
               
        def number_1():
            if (expression[1] == '+' or expression[1] == '-' or expression[1] == '*' or expression[1] == '/'):
                return int(expression[0])
            else:
                i = 0
                number = ''
                while expression[i] != ('+' or '-' or '*' or '/'):
                    number += expression[i]
                    i += 1
                return int(number)
        
        def number_2():
            return int(expression[2])
        
        number_1 = number_1()
        number_2 = number_2()

        if expression[1] == '+':
            print('result is : ', number_1+number_2)
        elif expression[1] == '-':
            print('result is : ', number_1-number_2)
        elif expression[1] == '*':
            print('result is : ', number_1*number_2)
        elif expression[1] == '/':
            print('result is : ', number_1/number_2)

            
        
    with open ('temp.txt', 'w') as j:
        j.write('')


frame = Frame(frame, bg='blue', width=500, height=500)
frame.grid(row=0, column=0)

entry = Entry(frame, width=40, relief=RIDGE)
entry.grid(row=1, column=(1), columnspan=8)

button_1 = Button(frame, text='1', fg='black', width=10, command=lambda: func(1))
button_1.grid(row = 2, column=0)

button_2 = Button(frame, text='2', fg='black', width=10, command = lambda: func(2))
button_2.grid(row = 2, column=1)

button_3 = Button(frame, text='3', fg='black', width=10, command = lambda : func(3))
button_3.grid(row = 2, column=2)



button_4 = Button(frame, text='4', fg='black', width=10, command=lambda: func(4))
button_4.grid(row = 3, column=0)

button_5 = Button(frame, text='5', fg='black', width=10, command = lambda : func(5))
button_5.grid(row = 3, column=1)

button_6 = Button(frame, text='6', fg='black', width=10, command = lambda : func(6))
button_6.grid(row = 3, column=2)



button_7 = Button(frame, text='7', fg='black', width=10, command=lambda: func(7))
button_7.grid(row = 4, column=0)

button_8 = Button(frame, text='8', fg='black', width=10, command= lambda: func(8))
button_8.grid(row = 4, column=1)

button_9 = Button(frame, text='9', fg='black', width=10, command= lambda: func(9))
button_9.grid(row = 4, column=2)


button_0 = Button(frame, text='0', fg='black', width=10, command= lambda: func(0))
button_0.grid(row = 5, column=2)

# making integer variables
number_1 = IntVar(button_1, value=1, name='1')
number_2 = IntVar(button_2, value=2, name='2')
number_3 = IntVar(button_3, value=3, name='3')
number_4 = IntVar(button_4, value=4, name='4')
number_5 = IntVar(button_5, value=5, name='5')
number_6 = IntVar(button_6, value=6, name='6')
number_7 = IntVar(button_7, value=7, name='7')
number_8 = IntVar(button_8, value=8, name='8')
number_9 = IntVar(button_9, value=9, name='9')
number_0 = IntVar(button_0, value=0, name='0')


button_plus = Button(frame, text='+', fg='black', width=10, command = lambda : add())
button_plus.grid(row = 2, column=3)

button_minus = Button(frame, text='-', fg='black', width=10, command= lambda : sub())
button_minus.grid(row = 3, column=3)

button_multiply = Button(frame, text='*', fg='black', width=10, command= lambda : mul())
button_multiply.grid(row = 4, column=3)

button_divide = Button(frame, text='/', fg='black', width=10, command= lambda: div())
button_divide.grid(row = 5, column=0)

button_equal = Button(frame, text='=', fg='black', width=10, command= lambda: equ())
button_equal.grid(row = 5, column=1)

button_c = Button(frame, text='C', fg='black', width=10, command = lambda : clear())
button_c.grid(row=5, column=3)

frame.mainloop()





