from tkinter import *
from gestionp import gest
from Stock import s
from tkinter import Tk, Frame, Canvas
from PIL import ImageTk, Image
import sys

def list():
    def back():
        root.destroy()
        import main
        main.funct()

    root=Tk()
    root.geometry("500x340+400+200")
    root.resizable(False,False)
    root.title("SuperMarket")
    root.iconbitmap('ff.ico')
    title=Label(root, text="برنامح تسيير محل",  bg="black", fg="gold", font=('Arial',20,'bold'))
    title.pack(fill=X)
    canvas = Canvas(root, bg="black", width=500, height=320)
    canvas.pack()

    def gestio():
        root.destroy()
        gest()
    def stock():
        root.destroy()
        s()
    b0 = Button(root, text="المخزن ", width=20, bg="gold", fg="black",command=stock)
    b2 = Button(root, text="الرئيسية", width=20, bg="gold", fg="black",command=gestio)
    b0.place(x=320, y=175)
    b2.place(x=320, y=205)
    b3 = Button(root, text="إغلاق ", width=20, bg="gold", fg="black",command=sys.exit)
    b4 = Button(root, text="رجوع", width=20,bg="gold", fg="black",command=back)
    b3.place(x=320, y=235)
    b4.place(x=320, y=265)
    global photoimage
    photoimage = ImageTk.PhotoImage(file="download.png")
    canvas.create_image(175, 140, image=photoimage)