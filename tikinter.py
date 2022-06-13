from tkinter import *
# 1 - bosqich
root = Tk()
root.title("Kalkulator")
input1 = Entry(root, width=60, borderwidth = 5)
input1.grid(row = 0,column = 0, columnspan = 10,padx=10,pady = 10)
def button_click(number):
	string = input1.get()
	input1.delete(0,END)
	input1.insert(0,str(string)+str(number))
def button_clear():
	input1.delete(0,END)
def button_add():
	raqam_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal = "qushish"
	saqlangan_raqam = int(raqam_olish)
	input1.delete(0,END)
def button_ayir():
	raqam_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal = "ayirish"
	saqlangan_raqam = int(raqam_olish)
	input1.delete(0,END)
def button_kop():
	raqam_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal = "kopaytirish"
	saqlangan_raqam = int(raqam_olish)
	input1.delete(0,END)
def button_bolish():
	raqam_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal = "bolish"
	saqlangan_raqam = int(raqam_olish)
	input1.delete(0,END)
def button_teng():
	summa=input1.get()
	input1.delete(0,END)
	if amal == "qushish":
		input1.insert(0,saqlangan_raqam + int(summa))
	if amal == "ayirish":
		input1.insert(0,saqlangan_raqam - int(summa))
	if amal == "kopaytirish":
		input1.insert(0,saqlangan_raqam * int(summa))
	if amal == "bolish":
		input1.insert(0,saqlangan_raqam / int(summa))
button1 = Button(root,text='1', padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root,text='2', padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root,text='3', padx=40, pady=20, command=lambda: button_click(3))

button4 = Button(root,text='4', padx=40, pady=20,command=lambda: button_click(4))
button5 = Button(root,text='5', padx=40, pady=20,command=lambda: button_click(5))
button6 = Button(root,text='6', padx=40, pady=20,command=lambda: button_click(6))

button7 = Button(root,text='7', padx=40, pady=20,command=lambda: button_click(7))
button8 = Button(root,text='8', padx=40, pady=20,command=lambda: button_click(8))
button9 = Button(root,text='9', padx=40, pady=20,command=lambda: button_click(9))

button0 = Button(root,text='0', padx=40, pady=20, command=lambda: button_click(0))
buttont = Button(root,text='cl', padx=40, pady=20, command=lambda: button_click('cl'))
buttonteng = Button(root,text='=', padx=40, pady=20, command=lambda: button_click('='))

buttonq = Button(root,text = '+', padx = 20, pady = 20, command = button_add)
buttona = Button(root,text = '-', padx = 20, pady = 20, command = button_ayir)
buttonk = Button(root,text = '*', padx = 20, pady = 20, command = button_kop)
buttonb = Button(root,text = '/', padx = 20, pady = 20, command = button_bolish)
buttonteng = Button(root,text = '=', padx = 20, pady = 20, command = button_teng)
buttont = Button(root,text = 'cl', padx = 20, pady = 20, command = button_clear)

button1.grid(row = 3,column = 0)
button2.grid(row = 3,column = 1)
button3.grid(row = 3,column = 2)
button4.grid(row = 4,column = 0)
button5.grid(row = 4,column = 1)
button6.grid(row = 4,column = 2)
button7.grid(row = 5,column = 0)
button8.grid(row = 5,column = 1)
button9.grid(row = 5,column = 2)
buttont.grid(row = 6,column = 0)
button0.grid(row = 6,column = 1)
buttonteng.grid(row = 6,column = 2)
buttonq.grid(row = 3,column = 3)
buttona.grid(row = 4,column = 3)
buttonb.grid(row = 5,column = 3)
buttonk.grid(row = 6,column = 3)
root.mainloop()