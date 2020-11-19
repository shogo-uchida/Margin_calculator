'''
author: shogo
the app where you circulate net, margin and gross
'''

from tkinter import *
import math


root = Tk()

root.title('margin APP')
root.geometry('450x300+450+100')
root.resizable(False, False) # (x, y) # cannot resize
canvas = Canvas(root, bg="oldlace", height=300, width=450)


################# FUNCTION ################
def circulation():
    if var.get() == 0:
        out_cir()
    else:
        in_cir()

#外掛け
def out_cir():
    try:
        rate = int(rate_box.get()) * 0.01
    except:
        eq2_box.delete(0, END)
        eq2_box.insert(0, 'enter the rate')
        return
    if gross_box.get().isdigit():
        gross = int(gross_box.get())
        net = gross * (1-rate)
        margin = gross * rate
        ans1_box.insert(0, net)
        ans2_box.insert(0, margin)
        eq1_box.insert(0, 'net = gross * (1-rate)')
        eq2_box.insert(0, 'margin = gross * rate')


    elif net_box.get().isdigit():
        net = int(net_box.get())
        gross = net / (1-rate)
        margin = rate * net / (1-rate)
        ans1_box.insert(0, gross)
        ans2_box.insert(0, margin)
        eq1_box.insert(0, 'gross = net / (1-rate)')
        eq2_box.insert(0, 'mgn = rate*net/(1-rate)')

    elif margin_box.get().isdigit():
        margin = int(margin_box.get())
        gross = margin / rate
        net = (1 - rate) * margin / rate
        ans1_box.insert(0, gross)
        ans2_box.insert(0, net)
        eq1_box.insert(0, 'gross = margin / rate')
        eq2_box.insert(0, 'net=(1-rate)*margin/rate')

    else:
        eq2_box.delete(0, END)
        eq2_box.insert(0, 'enter the number')


#内掛け
def in_cir():
    rate = int(rate_box.get()) * 0.01
    if gross_box.get().isdigit():
        gross = int(gross_box.get())
        net = gross / (1 + rate)
        margin = gross * rate / (1 + rate)
        ans1_box.insert(0, net)
        ans2_box.insert(0, margin)
        eq1_box.insert(0, 'net = gross / (1 + rate)')
        eq2_box.insert(0, 'mgn=gross*rate/(1 + rate)')


    elif net_box.get().isdigit():
        net = int(net_box.get())
        gross = net * (1 + rate)
        margin = net * rate
        ans1_box.insert(0, gross)
        ans2_box.insert(0, margin)
        eq1_box.insert(0, 'gross = net * (1 + rate)')
        eq2_box.insert(0, 'margin = net * rate')

    elif margin_box.get().isdigit():
        margin = int(margin_box.get())
        gross = (1 + rate) * margin / rate
        net = margin / rate
        ans1_box.insert(0, gross)
        ans2_box.insert(0, net)
        eq1_box.insert(0, 'gross=(1+rate)*margin/rate')
        eq2_box.insert(0, 'net = margin / rate')


    else:
        eq2_box.delete(0, END)
        eq2_box.insert(0, 'enter the number')


def reset():
    gross_box.delete(0, END)
    net_box.delete(0, END)
    margin_box.delete(0, END)
    eq1_box.delete(0, END)
    eq2_box.delete(0, END)
    ans1_box.delete(0, END)
    ans2_box.delete(0, END)
    rate_box.delete(0, END)

################# EVENT Action ############

################ Entry box ###################
gross_box = Entry(font = 'verdana 10 bold',
                  width = 10, bd = 2, bg = '#e6e6fa')

gross_box.place(x = 100, y = 80)
net_box = Entry(font = 'verdana 10 bold',
                  width = 10, bd = 2, bg = '#e6e6fa')
#net_box.insert(0, 0)
net_box.place(x = 100, y = 130)
margin_box = Entry(font = 'verdana 10 bold',
                  width = 10, bd = 2, bg = '#e6e6fa')
#margin_box.insert(0, 0)
margin_box.place(x = 100, y = 180)
discount_box = Entry(font = 'verdana 10 bold',
                  width = 10, bd = 2, bg = '#e6e6fa')
#discount_box.insert(0, 0)
discount_box.place(x = 310, y = 80)
fraud_box = Entry(font = 'verdana 10 bold',
                  width = 10, bd = 2, bg = '#e6e6fa')
#fraud_box.insert(0, 0)
fraud_box.place(x = 310, y = 130)
rate_box = Entry(font = 'verdana 10 bold',
                  width = 8, bd = 2, bg = '#e6e6fa')
rate_box.insert(0, 0)
rate_box.place(x = 250, y = 20)
ans1_box = Entry(font = 'verdana 10 bold',
                  width = 17, bd = 2, justify = RIGHT,bg = '#e6e6fa')
ans1_box.insert(0, 0)
ans1_box.place(x = 60, y = 270)
ans2_box = Entry(font = 'verdana 10 bold',
                  width = 17, bd = 2, justify = RIGHT,bg = '#e6e6fa')
ans2_box.insert(0, 0)
ans2_box.place(x = 250, y = 270)
eq1_box = Entry(font = 'verdana 10 bold',
                  width = 20, bd = 2, justify = RIGHT,bg = '#e6e6fa')
eq1_box.place(x = 40, y =240)
eq2_box = Entry(font = 'verdana 10 bold',
                  width = 20, bd = 2, justify = RIGHT,bg = '#e6e6fa')
eq2_box.place(x = 230, y =240)

################ Label ##################
gross_text = Label(root, text = 'gross:', relief = SUNKEN, height = 1,
                   anchor = E, font = 'verdana 11 bold')
gross_text.place(x = 25, y = 80)
net_text = Label(root, text = 'net:', relief = SUNKEN, height = 1,
                   anchor = E, font = 'verdana 11 bold')
net_text.place(x = 25, y = 130)
margin_text = Label(root, text = 'margin:', relief = SUNKEN, height = 1,
                   anchor = W, font = 'verdana 11 bold')
margin_text.place(x = 25, y =180)
discount_text = Label(root, text = 'discount:', relief = SUNKEN, height = 1,
                   anchor = W, font = 'verdana 11 bold')
discount_text.place(x = 225, y =80)
fraud_text = Label(root, text = 'fraud:', relief = SUNKEN, height = 1,
                   anchor = W, font = 'verdana 11 bold')
fraud_text.place(x = 225, y =130)
rate_text = Label(root, text = '%', relief = SUNKEN, height = 1,
                   anchor = W, font = 'verdana 11 bold')
rate_text.place(x = 320, y =20)
#eq1_text = Label(root, text = '', relief = SUNKEN, height = 1,
#                   anchor = W, font = 'verdana 11 bold', width = 15)
#eq1_text.place(x = 60, y =240)
#eq2_text = Label(root, text = '', relief = SUNKEN, height = 1,
#                   anchor = W, font = 'verdana 11 bold', width = 15)
#eq2_text.place(x = 250, y =240)

canvas.create_line(10, 65, 440, 65, fill='black', width = 5)
canvas.pack()
canvas.create_line(10, 230, 440, 230, fill='black', width = 5)
canvas.pack()

################## radiobutton ############
var = IntVar()
var.set(0)
out = Radiobutton(root, value=0, variable=var, text='外掛け')
out.place(x=40, y=20)
in_ = Radiobutton(root, value=1, variable=var, text='内掛け')
in_.place(x=130, y=20)

################### Button #################
circulation = Button(width = 7, text = 'circulate', font = 'times 15 bold',
                 bd = 4, command = circulation)
circulation.place(x = 300, y = 170)
reset = Button(width = 4, text = 'reset', font = 'times 15 bold',
                 bd = 4, command = reset)
reset.place(x = 230, y = 170)
################## RUN ##################
root.mainloop()

















