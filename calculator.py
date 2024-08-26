# Autor: Israel Avila Mares
from tkinter import *
from tkinter import Button
from tkinter import END
from tkinter import Entry
from tkinter import Frame
from tkinter import Tk
from tkinter import messagebox
import math

# Variables globales
operacion = None
listOper = []

# funciones
def on_button_click(value):
    current_text = screen.get()
    screen.delete(0, END)
    screen.insert(0, current_text + str(value))

def cleanScren():
    listOper.clear()
    screen.delete(0, END)

def KindOperone(option):
    global operacion
    try:
        numaux = screen.get()
        numConve = float(numaux)
        listOper.append(numConve)
        operacion = option
    except ValueError:
        messagebox.showinfo(title="Error", message="Carácter incorrecto")

def KindOperation(op):
    global operacion
    try:
        numaux = screen.get()
        numConve = float(numaux)
        listOper.append(numConve)
        operacion = op
        screen.delete(0, END)
    except ValueError:
        messagebox.showinfo(title="Error", message="Carácter incorrecto")

def resultEquel():
    global operacion
    try:
        numConve = float(screen.get())
        listOper.append(numConve)
        
        if operacion == "+":
            resultado = sum(listOper)
        elif operacion == "!":
            numerotoFact = listOper[-1]
            if numerotoFact < 0:
                messagebox.showinfo(title="Error", message="El factorial no está definido para números negativos")
                return
            resultado = math.factorial(int(numerotoFact))

        elif operacion == "^":
            resultado = ExpOper() 

        elif operacion == "%":
            resultado = percentege()

        elif operacion == "√":
            resultado = RootSquare()
        
        elif operacion == "|x|":
            resultado = valueAbs()

        elif operacion == "*":
            resultado = 1
            for num in listOper:
                resultado *= num

        elif operacion == "/":
            resultado = listOper[0]
            try:
                for num in listOper[1:]:
                    resultado /= num
            except ZeroDivisionError:
                messagebox.showinfo(title="Error", message="No se puede dividir entre cero")
                return        
        elif operacion == "-":
            resultado = listOper[0] - sum(listOper[1:])

        screen.delete(0, END)
        screen.insert(0, str(resultado))
        listOper.clear()
        operacion = None

    except ValueError:
        messagebox.showinfo(title="Error", message="Carácter incorrecto")

################################### FUNCIONES DE OPERACIONES  ##########################

def ExpOper():
    num1 = listOper[0]
    num2 = listOper[1]
    return math.pow(num1, num2)

def percentege():
    num1 = listOper[0]
    num2 = listOper[1]
    return (num1*num2)/100


def RootSquare():
    num = listOper[-1]
    return math.sqrt(num)

def valueAbs():
    num = listOper[-1]
    return abs(num)

##############################------   Main tkinter -------- ######################################
def main():
    # Crear la ventana principal
    root = Tk()
    root.geometry("750x650")
    root.title("Calculator")
    root.config(bg="light green", bd=25, relief="flat")

    # Crear el frame principal 
    global screen  # Declarar la variable como global
    frame = Frame(root, bg="steel blue", width=580, height=540, bd=20)
    frame.pack(pady=10)
    frame.pack_propagate(0)

    # Crear el campo de entrada dentro del frame
    screen = Entry(frame, width=80, font=("Arial", 20))
    screen.pack(pady=20)

    # Crear un frame para los botones
    button_frame = Frame(frame, bg="steel blue")
    button_frame.pack()

    # Crear los botones numéricos (0-9)
    buttons = [
        Button(button_frame, bg="DodgerBlue3", text=str(i), font=("Arial", 18), width=5, height=2, command=lambda i=i: on_button_click(i))
        for i in range(10)
    ]

    # Organizar los botones en la cuadrícula (grid)
    buttons[1].grid(row=0, column=0)
    buttons[2].grid(row=0, column=1)
    buttons[3].grid(row=0, column=2)
    buttons[4].grid(row=1, column=0)
    buttons[5].grid(row=1, column=1)
    buttons[6].grid(row=1, column=2)
    buttons[7].grid(row=2, column=0)
    buttons[8].grid(row=2, column=1)
    buttons[9].grid(row=2, column=2)
    buttons[0].grid(row=3, column=1)

    # Crear los botones de operaciones y limpiar
    btAddition = Button(button_frame, text="+", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=lambda: KindOperation("+"))
    btAddition.grid(row=0, column=3)

    btSubtraction = Button(button_frame, text="-", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=lambda: KindOperation("-"))
    btSubtraction.grid(row=1, column=3)

    btMultiplication = Button(button_frame, text="*", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=lambda: KindOperation("*"))
    btMultiplication.grid(row=2, column=3)

    btDivision = Button(button_frame, text="/", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=lambda: KindOperation("/"))
    btDivision.grid(row=3, column=3)

    btequel = Button(button_frame, text="=", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=resultEquel)
    btequel.grid(row=3, column=2)

    btnclean = Button(button_frame, text="C", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=cleanScren)
    btnclean.grid(row=3, column=0)

    # Agregar el botón de factorial
    btnfactorial = Button(button_frame, text="x!", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=lambda: KindOperone("!"))
    btnfactorial.grid(row=0, column=4)

    # Agregar el botón de exponente
    btnExpont = Button(button_frame, text="^", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=lambda: KindOperation("^"))
    btnExpont.grid(row=1, column=4)

    #porcentaje
    btnpercent = Button(button_frame, text="%", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=lambda: KindOperation("%"))
    btnpercent.grid(row=2, column=4)

    #Raiz cuadrada
    bntRaizsquare = Button(button_frame, text="√", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=lambda: KindOperone("√"))
    bntRaizsquare.grid(row=3, column=4)

    #abs valor absoluto
    bntAbs = Button(button_frame, text="|x|", font=("Arial", 18), bg="DodgerBlue3", width=5, height=2, command=lambda: KindOperone("|x|"))
    bntAbs.grid(row=4, column=4)
    # Ejecutar el bucle principal de la ventana
    root.mainloop()

if __name__ == "__main__":
    main()
