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
cred = credentials.Certificate('key/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-2b50d.firebaseio.com/'
})


marco1 = Frame(ventana, bg="blue", highlightthickness=1, width=1280, height=800, bd= 5)
marco1.place(x = 0,y = 0)
b=Label(marco1,text="")
img = Image.open("C:/Users/user/Desktop/gatito.png")
img = img.resize((150,150), Image.ANTIALIAS)
photoImg=  ImageTk.PhotoImage(img)
b.configure(image=photoImg)
b.place(x = 500,y = 20)

def adc_read0():
    ref = db.reference('sensor')
    x=ref.get()
    i=x.get('sensor0')
    print(i)
    led9.write(i)
    
def adc_read1():
    ref = db.reference('sensor')
    x=ref.get()
    i=x.get('sensor1')
    print(i)
    led9.write(i)

def adc_read2():   
    ref = db.reference('sensor')
    x=ref.get()
    i=x.get('sensor2')
    print(i)
    led9.write(i)


bot0=Button(text="adc1_update",command=adc_read0)
bot0.place(x=120, y=30)

bot1=Button(text="adc2_update",command=adc_read1)
bot1.place(x=120, y=70)

bot2=Button(text="adc3_update",command=adc_read2)
bot2.place(x=120, y=110)


ventana.mainloop()
