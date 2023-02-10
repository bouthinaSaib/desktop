from tkinter import *
import sys
import database
from tkinter import ttk

def s():
    def additem():
        database.AddToDb(en1.get(), en2.get(), dropu.get())
        root.destroy()
        s()
    def deletitem():
        database.deleteby(en1.get())
        root.destroy()
        s()
    def updateitems():
        database.updateitem(en1.get(), en2.get(), dropu.get())
        root.destroy()
        s()
    root=Tk()
    root.geometry("603x450+200+200")
    root.resizable(False,False)
    root.title("SuperMarket")
    root.iconbitmap('ff.ico')
    title=Label(root, text="برنامح تسيير محل",  fg="gold", bg="black", font=('Arial',20,'bold'))
    title.pack(fill=X)
    l1 = Label(root, text="السلعة", fg="black")
    l1.place(x=10, y=70)
    l2 = Label(root, text="السعر", fg="black")
    l2.place(x=200, y=70)
    l3 = Label(root, text="وحدة القياس", fg="black")
    l3.place(x=350, y=70)
    en1 = Entry(root, justify="center")
    en1.place(x=10, y=120)
    en2 = Entry(root, justify="center")
    en2.place(x=180, y=120)
    tab=['Unit','KG']
    clickedu = StringVar()
    dropu = ttk.Combobox(root, textvariable=clickedu, values=tab)
    dropu.set('KG')
    dropu.config(width=30, height=10)
    dropu.place(x=350, y=120)
    b0 = Button(root, text="UPDATE ", width=16, height=4, fg="gold", bg="black",command=updateitems)
    b2 = Button(root, text="ADD", width=16, height=4, fg="gold", bg="black",command=additem)
    b3 = Button(root, text="DELETE", width=16, height=4, fg="gold", bg="black",command=deletitem)
    b0.place(x=10, y=170)
    b2.place(x=180, y=170)
    b3.place(x=350, y=170)
    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings', height=8, selectmode="browse")
    tree.column("#1", anchor=CENTER, stretch=NO)
    tree.heading("#1", text="السلعة")
    tree.column("#2", anchor=CENTER, stretch=NO)
    tree.heading("#2", text="السعر")
    tree.column("#3", anchor=CENTER, stretch=NO)
    tree.heading("#3", text="الوحدة")
    # Insert the data in Treeview widget
    rows=database.table()
    for i in rows:
        tree.insert('','end',values=i)
    # Adding a vertical scrollbar to Treeview widget
    treeScroll = ttk.Scrollbar(root)
    treeScroll.configure(command=tree.yview)
    tree.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side=RIGHT, fill=BOTH)
    tree.place(x=0, y=250)



