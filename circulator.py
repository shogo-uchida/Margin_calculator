

'''
we have made the criculater
normal version
'''


from tkinter import *
import math
root = Tk()

root.title('calculator APP')
root.geometry('450x560+450+100')
root.resizable(False, False) # (x, y) # cannot resize
################################ Functions ############################
def enterNumber(x):
    if entry_box.get() == 'O':
        entry_box.delete(0, 'end')
        entry_box.insert(0, str(x))

    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))

def enterOperator(x):
    if entry_box.get() != 'O': # *7+9  to avoid like this
        length = len(entry_box.get())
        entry_box.insert(length, btn_operator[x]['text']) #(where, what)

def funcClear():
    entry_box.delete(0, END)
    entry_box.insert(0, 'O')

result = 0
result_list = []
def funcOperator():
    try:
        content = entry_box.get()
    #    print(content)
        result = eval(content) # this will calcurate the strings
        entry_box2.delete(0, END)
        entry_box2.insert(0, str(content))
    #    print(result)
        entry_box.delete(0, END)
        entry_box.insert(0, str(result))

        result_list.append(content)
        result_list.reverse()
        statusBar.configure(text = 'History : ' + '|'.join(result_list[:5]), font = 'verdana 10 bold') # history shows up to 5 equations
    except:
        entry_box.delete(0, END)
        entry_box.insert(0, 'O')
        entry_box2.delete(0, END)
        entry_box2.insert(0, 'ERROR')


def funcDelete():
    length = len(entry_box.get())
    entry_box.delete(length-1, 'end') # cuz len starts from 1
    if length == 1:
        entry_box.insert(0, 'O')

def funccopy():
    content = entry_box2.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(content))


################################## Event Action ##############################

def funcOperator2(event): # for the case you type enter key to operate the system
    content = entry_box.get()
#    print(content)
    result = eval(content) # this will calcurate the strings
    entry_box2.delete(0, END)
    entry_box2.insert(0, str(content))
#    print(result)
    entry_box.delete(0, END)
    entry_box.insert(0, str(result))

    result_list.append(content)
    result_list.reverse()
    statusBar.configure(text = 'History : ' + '|'.join(result_list[:5]), font = 'verdana 10 bold') # history shows up to 5 equations

def funccopy2(event):
    content = entry_box2.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(content))



#########################circulation box ##############################
entry_box2 = Entry(font = 'verdana 14 bold', width = 28, bd = 10, justify = RIGHT, bg = '#e6e6fa')
# justify = RIGHT means you type from right side
entry_box2.insert(0, 'O') # capital o
entry_box2.place(x = 20, y = 10)

########################## Entry box #################
entry_box = Entry(font = 'verdana 14 bold', width = 28, bd = 10, justify = RIGHT, bg = '#e6e6fa')
# justify = RIGHT means you type from right side
entry_box.insert(0, 'O') # capital o
entry_box.place(x = 20, y = 70)


############################   BUTTONS ############################
############################ number buttons ######################

numbers = [7, 8, 9 ,4, 5, 6, 1, 2, 3]
btn_numbers = []
for i in numbers:
    btn_numbers.append(Button(width = 5, text = str(i), font = 'times 15 bold', bd = 5, command = lambda x = i: enterNumber(x)))

btn_text = 0
for i in range(0, 3):
    for j in range(0, 3):
        btn_numbers[btn_text].place(x = 25 + j*90, y = 260 + i*60) # btn_numbers[3]
        btn_text += 1


############################ operator buttons ######################
btn_operator = []
for i in range(4):
    btn_operator.append(Button(width = 4, font = 'times 15 bold', bd = 5, command = lambda x = i:enterOperator(x)))

btn_operator[0]['text'] = '+'
btn_operator[1]['text'] = '-'
btn_operator[2]['text'] = '*'
btn_operator[3]['text'] = '/'

for i in range(4):
    btn_operator[i].place(x = 290, y = 260 + i*60)

############################### other buttons ###########################

btn_zero = Button(width = 5, text = '0', font = 'times 15 bold', bd = 5, command = lambda x = 0: enterNumber(x))
btn_clear = Button(width = 4, text = 'C', font = 'times 15 bold', bd = 5, command = funcClear)
btn_zero.place(x = 25, y = 440)
btn_clear.place(x = 370, y = 320)
btn_dot = Button(width = 5, text = '.', font = 'times 15 bold', bd = 5, command = lambda x = '.':enterNumber(x))
btn_dot.place(x = 115, y = 440)
btn_equal = Button(width = 4, text = '=', font = 'times 15 bold', bd = 5, command = funcOperator)
btn_equal.place(x = 370, y = 440)

#icon = PhotoImage(file = '')
btn_delete = Button(width = 4, text = '←', font = 'times 15 bold', bd = 5, command = funcDelete)
btn_delete.place(x = 370, y = 380)

############################ Math buttons #############################
btn_power = Button(width = 5, text = '10**x', font = 'times 15 bold', bd = 5, command = lambda x = '*10**':enterNumber(x))
btn_power.place(x = 205, y = 440)
btn_power2 = Button(width = 4, text = '**2', font = 'times 15 bold', bd = 5, command = lambda x = '**2':enterNumber(x))
btn_power2.place(x = 370, y = 260)
btn_powerx = Button(width = 4, text = '**x', font = 'times 15 bold', bd = 5, command = lambda x = '**':enterNumber(x))
btn_powerx.place(x = 290, y = 200)
btn_bracketl = Button(width = 5, text = '(', font = 'times 15 bold', bd = 5, command = lambda x = '(':enterNumber(x))
btn_bracketl.place(x = 25, y = 200)
btn_bracketr = Button(width = 5, text = ')', font = 'times 15 bold', bd = 5, command = lambda x = ')':enterNumber(x))
btn_bracketr.place(x = 115, y = 200)
btn_root = Button(width = 5, text = 'Root', font = 'times 15 bold', bd = 5, command = lambda x = 'math.sqrt()':enterNumber(x))
btn_root.place(x = 205, y = 200)
btn_sin = Button(width = 5, text = 'sin', font = 'times 15 bold', bd = 5, command = lambda x = 'math.sin()':enterNumber(x))
btn_sin.place(x = 25, y = 140)
btn_cos = Button(width = 5, text = 'cos', font = 'times 15 bold', bd = 5, command = lambda x = 'math.cos()':enterNumber(x))
btn_cos.place(x = 115, y = 140)
btn_tan = Button(width = 5, text = 'tan', font = 'times 15 bold', bd = 5, command = lambda x = 'math.tan()':enterNumber(x))
btn_tan.place(x = 205, y = 140)
btn_down = Button(width = 4, text = '↓', font = 'times 15 bold', bd = 5, command = funccopy)
btn_down.place(x = 290, y = 140)

############################### OTHER ########################

statusBar = Label(root, text = 'History : ', relief = SUNKEN, height = 3, anchor = W, font = 'verdana 11 bold')
statusBar.pack(side = BOTTOM, fill = X)

####################### click event ###################

root.bind('<Return>', funcOperator2) # to make an event with enter key
root.bind('<Down>', funccopy2)



################################# RUN ########################################

root.mainloop()















