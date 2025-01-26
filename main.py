from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path
path = Path()
import time
fecha = time.strftime("%H:%M:%S") + " | " + time.strftime("%d/%m/%y")

# from recipe import donut_maker
import tkinter as tk
#import win32api
from tkinter import filedialog
#import win32print
import tempfile

# arch = open('ingredientes.txt','w')
# arch.close()

ingredientes = []

ingredients = {
'Harina': 35.2564,
'Margarina':1.839,
'Manteca':1.839,
'Huevo':5.288,
'Azucar':5.64312,
'Agua':12.7,
'Sal':0.29,
'Levadura':0.3522
}


root = Tk()
root.geometry("400x600")
root.configure(bg='white')

root.title("Donut Calculator")

#entry
e = Entry(root, width=25, borderwidth=5)
e.grid(row=0,column=0, padx=40, pady=10)


#Image
my_img = Image.open(path / "donut.png")
my_img = my_img.resize((200, 200), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(my_img)
label_img = Label(root, image = img)
label_img.grid(row=1,column=0)
label_img.configure(bg='white')


#canvas
T = Text(root, width=45, height=12, borderwidth=4)
T.config(font=("Courier",10))
T.grid(row=2, column=0,columnspan=2,pady=10)

#Buttons
def normal_button():
    T.delete('1.0',END)
    num = e.get()
    global cantidad
    cantidad = int(num)
    global resultado
    weather = 'Normal'
    text = f'Receta de donas para {cantidad} donas\nClima: {weather}\tHora: {fecha}\n---------------------------------\n'
    T.insert(END, text)
    ingredients['Levadura']=0.3522
    ingredientes.append(text)
    for ing in ingredients:
        multiply = ingredients[ing]*cantidad
        resultado = ing + ": " + str(multiply)+"\n"
        ingredientes.append(resultado)
        T.insert(END,resultado)
    arch = open('ingredientes.txt','w')
    for li in range(len(ingredientes)):
        arch.write(ingredientes[li])
    arch.close()


def cold_button():
    T.delete('1.0', END)
    num = e.get()
    global weather
    global cantidad
    weather = "Frio"
    cantidad = int(num)
    global resultado
    text = f'Receta de donas para {cantidad} donas\nClima: {weather}\tHora: {fecha}\n----------------------------------\n'
    T.insert(END, text)
    ingredientes.append(text)
    if weather =='Frio':
        lev=0.3522*0.30
        ingredients['Levadura'] = lev
        for ing in ingredients:
            multiply = ingredients[ing]*cantidad
            resultado = ing + ": " + str(multiply)+"\n"
            T.insert(END,resultado)
            ingredientes.append(resultado)
        arch = open('ingredientes.txt', 'w')
        for li in range(len(ingredientes)):
            arch.write(ingredientes[li])
        arch.close()

def delete_button():
    del ingredientes[0:len(ingredientes)]
    arch = open('ingredientes.txt', 'w')
    for i in range(len(ingredientes)):
        arch.write(ingredientes[i])
    arch.close()
    T.delete('1.0',END)


#
# #impr
# def __init__(self):
#     tk.Button(root, text='Imprimir', command=self.imprimir).grid(
#         row=4, columnspan=2, sticky="we")
#
#
#
def imprimit():
    archivo = 'ingredientes.txt'

   # win32api.ShellExecute (
    0,
    "printto",
    archivo,
   #'"%s"' % win32print.GetDefaultPrinter(),
    ".",
    0
   # )

#
Button(root, text="Print File", pady=10,padx=150,command=imprimit).grid(row=4,column=0,padx=10,pady=5,columnspan=3)





#button
button_hot = Button(root, text="Normal Weather", padx=30, pady=10, command=normal_button)
button_cold = Button(root, text="Cold weather", padx=35, pady=10, command=cold_button)
button_delete = Button(root, text="Delete", padx=25, pady=10, command=delete_button)
button_exit = Button(root, text="Exit", padx=25, pady=10,command=quit)

button_delete.grid(row=3,column=0)
button_exit.grid(row=3,column=1)
button_hot.grid(row=0, column=1, pady=10)
button_cold.grid(row=1, column=1, pady=0)






root.mainloop()