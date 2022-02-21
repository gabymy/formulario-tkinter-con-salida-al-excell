from tkinter import Tk, Label, Button,Entry, Frame, END
import pandas as pd

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry


def agregar_datos():
	global asociado, cuit, domicilio, periodo, monto, eleccion, cal

	asociado.append(ingresa_nombre.get())
	cuit.append(ingresa_cuit.get())
	domicilio.append(ingresa_domicilio.get())
	periodo.append(ingresa_periodo.get())
	monto.append(ingresa_monto.get())
	eleccion.append(ingresa_eleccion.get())
	cal.append(ingresa_tiempo.get())

	asociado_entry.delete(0, END)
	cuit_entry.delete(0, END)
	domicilio_entry.delete(0, END)
	periodo_entry.delete(0, END)
	monto_entry.delete(0, END)
	eleccion_entry.delete(0, END)
	cal_entry.delete(0, END)

def guardar_datos():	
	global asociado, cuit, domicilio, periodo, monto, eleccion
	datos = {"Fecha":cal, 'Nombre y Apellido':asociado,'CUIT':cuit, 'Domicilio':domicilio, 'Periodo a liquidar':periodo, "Importe a percibir":monto,'Forma de pago':eleccion } 
	nom_excel  = str(nombre_archivo.get() + ".xlsx")	
	df = pd.DataFrame(datos,columns =  ['Nombre y Apellido', 'CUIT', 'Domicilio', 'Periodo a liquidar',"Importe a percibir", 'Forma de Pago']) 
	df.to_excel(nom_excel)
	nombre_archivo.delete(0,END)



mywindow = Tk()
mywindow.geometry("700x700")
mywindow.title("ANTICIPO DE RETORNO")
mywindow.resizable(0,0)
main_title=Label(text="Cooperativa de Trabajo POLILU Ltda.",bd=5, font=("Curier 18 bold italic"),bg="#56CD63",fg="white",width="550",height="1")
main_title.pack()
mywindow.config(background="#213141")
asociado, cuit, domicilio, periodo, monto, eleccion, cal= [],[],[],[],[],[], []




cal_label=Label(text="Fecha", bg="#FFEEDD", font=("Curier 12 bold"))
cal_label.place(x=22, y=70)


asociado_label=Label(text="Apellido y Nombre", bg="#FFEEDD", font=("Curier 12 bold"))
asociado_label.place(x=22, y=130)

cuit_label=Label(text="C.U.I.T", bg="#FFEEDD",font=("Curier 12 bold") )
cuit_label.place(x=22, y=190)

domicilio_label=Label(text="Domicilio", bg="#FFEEDD", font=("Curier 12 bold"))
domicilio_label.place(x=22, y=250)

periodo_label=Label(text="Periodo a Liquidar", bg="#FFEEDD",font=("Curier 12 bold") )
periodo_label.place(x=22, y=310)

monto_label=Label(text="Monto en $",bg="#FFEEDD",font=("Curier 12 bold") )
monto_label.place(x=22, y=370)

eleccion_label=Label(text="Forma de pago", bg="#FFEEDD",font=("Curier 12 bold") )
eleccion_label.place(x=22, y=430)


cal_entry=Entry(textvariable=cal, width="50")

asociado_entry=Entry(textvariable=asociado, width="50")

cuit_entry=Entry(textvariable=cuit, width="50")

domicilio_entry=Entry(textvariable=domicilio, width="50")

periodo_entry=Entry(textvariable=periodo, width="40")

monto_entry=Entry(textvariable=monto, width="50")

eleccion_entry=Entry(textvariable=eleccion, width="50")


cal_entry.place(x=22, y=100)

asociado_entry.place(x=22, y=160)

cuit_entry.place(x=22, y=220)

domicilio_entry.place(x=22, y=280)

periodo_entry.place(x=22, y=340)

monto_entry.place(x=22, y=400)

eleccion_entry.place(x=22, y=460)



archivo = Label(text ='Ingrese Nombre del archivo', width=20, bg="#213141",font = ('Arial',12, 'bold'), fg='white')


nombre_archivo = Entry(width=23, font = ('Arial',12),highlightbackground = "green", highlightthickness=4)
nombre_archivo.place(x=22,y=520)

guardar = Button(mywindow,text="Guardar Datos",command=guardar_datos, bd=8,font=("Curier 11 bold"), width="30",height="1",bg="#00CD63")
guardar.place(x=22,y=580)













mywindow.mainloop()
