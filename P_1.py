import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time

placa = Arduino ('COM3')
it = util.Iterator(placa)
it.start()
a_0 = placa.get_pin('a:0:i')
a_1 = placa.get_pin('a:1:i')
a_2 = placa.get_pin('a:2:i')
led8 = placa.get_pin('d:8:o')
led9 = placa.get_pin('d:9:p')
led10 = placa.get_pin('d:10:p')
led11 = placa.get_pin('d:11:p')
led12 = placa.get_pin('d:12:o')
led13 = placa.get_pin('d:13:o')
time.sleep(0.1)
ventana = Tk()
ventana.geometry('800x600')
ventana.title("Parcial")

# Fetch the service account key JSON file contents
cred = credentials.Certificate('llave/llave.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-2b50d.firebaseio.com/'
})


marco1 = Frame(ventana, bg="blue", highlightthickness=1, width=1280, height=800, bd= 5)
marco1.place(x = 0,y = 0)

frame1 = Frame(marco1, bg="blue", highlightthickness=1, width=700, height=550, bd= 5)
frame1.place(x = 15,y = 15)

b=Label(frame1,text="")
img = Image.open("C:/Users/user/Desktop/gatito.png")
img = img.resize((150,150), Image.ANTIALIAS)
photoImg=  ImageTk.PhotoImage(img)
b.configure(image=photoImg)
b.place(x = 500,y = 20)

valor0= Label(marco1, bg='cadet blue', font=("Arial Bold", 15), fg="white", width=5)
adc_data0=StringVar()
valor1= Label(marco1, bg='cadet blue', font=("Arial Bold", 15), fg="white", width=5)
adc_data1=StringVar()
valor2= Label(marco1, bg='cadet blue', font=("Arial Bold", 15), fg="white", width=5)
adc_data2=StringVar()

def adc_read0():
        x=a_0.read()
        print(x)
        adc_data0.set(x)
        ventana.update()
        time.sleep(0.1)
        ref = db.reference('sensor')
        ref.update({
        'sensor0': x
    })

def adc_read1():
        x=a_1.read()
        print(x)
        adc_data1.set(x)
        ventana.update()
        time.sleep(0.1)
        ref = db.reference('sensor')
        ref.update({
        'sensor1': x
    })

def adc_read2():   
        x=a_2.read()
        print(x)
        adc_data2.set(x)
        ventana.update()
        time.sleep(0.1)
        ref = db.reference('sensor')
        ref.update({
        'sensor2': x
    })

valor0.configure(textvariable=adc_data0)
valor0.place(x=20, y=30)
bot0=Button(text="A0",command=adc_read0)
bot0.place(x=120, y=40)
valor1.configure(textvariable=adc_data1)
valor1.place(x=20, y=70)
bot1=Button(text="A1",command=adc_read1)
bot1.place(x=120, y=80)
valor2.configure(textvariable=adc_data2)
valor2.place(x=20, y=110)
bot2=Button(text="A2",command=adc_read2)
bot2.place(x=120, y=120)


ventana.mainloop()
