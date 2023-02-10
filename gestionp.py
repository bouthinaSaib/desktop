from tkinter import *
import tkinter as tk
import datetime as dt
from tkinter import ttk
import database
import sys
import os
def gest():
    def initBill():
        t.delete('1.0', END)
        t.insert(END, "\t مرحبا بكم في متجركم")
        t.insert(END, "\n===========================================")
        t.insert(END, "\n السلعة")
        t.insert(END, "\t \t")
        t.insert(END, " عدد الوحدات /الوزن")
        t.insert(END, "\t \t")
        t.insert(END, " السعر")

    def open_text(event):
        t.delete('1.0', END)
        text_file = open(os.path.join(os.getcwd(),"billes",drop2.get()) ,"r",encoding='utf-8', errors='ignore')
        content = text_file.read()
        t.insert(END, content)
        text_file.close()
    def delete():
        # Get selected item to Delete
        selected_item = tree.selection()[0]
        tree.delete(selected_item)
    i = 1
    def save_text():
        date = dt.datetime.now()
        name= date.strftime("%m_%d_%Y_%H.%M.%S")+ ".txt"
        t.insert(END, "\n===========================================")
        t.insert(END, "\n")
        t.insert(END,date.strftime("%m/%d/%Y %H:%M:%S"))
        t.insert(END, "\n===========================================")
        t.insert(END, "\n نشكركم على ثقتكم في متجرنا و نرحب بكم دائما")
        text_file = open(os.path.join(os.getcwd(),"billes",name), "w",encoding='utf-8', errors='ignore')
        text_file.write(t.get(1.0, END))
        os.startfile(os.path.join(os.getcwd(),"billes",name), "print")
        root.destroy()
        gest()
    def getPriceByName(event):
        en2.delete(0, END)
        en2.insert(END,database.getbyname(drop.get()))

    def getPriceByName2(event):
        en2u.delete(0, END)
        en2u.insert(END, database.getbyname(dropu.get()))
    def calc_w():
        tree.insert("", 'end', values=(drop.get(), en.get(),int(en.get())*int(en2.get())/1000 ))
    def calc_u():
        tree.insert("", 'end',values=(dropu.get(), enu.get(),int(en2u.get())*int(enu.get()) ))
    def bill_go():
        t.insert(END,"\n")
        somme=0
        for items in tree.get_children():
           t.insert(END, tree.item(items)["values"][0])
           t.insert(END, "\t \t")
           t.insert(END, tree.item(items)["values"][1])
           t.insert(END, "\t \t \t")
           t.insert(END, tree.item(items)["values"][2])
           t.insert(END, "\n")
           somme=somme+float(tree.item(items)["values"][2])
        t.insert(END, "\n Total cost:  ")
        t.insert(END, somme)
    def rest():
        en2.delete(0,END)
        en.delete(0,END)
        enu.delete(0,END)
        en2u.delete(0,END)
        initBill()

    root = Tk()
    root.geometry("1200x700+50+50")
    root.resizable(False, False)
    root.title("SuperMarket")
    root.iconbitmap('ff.ico')
    title = Label(root, text="برنامح تسيير محل", fg="gold", bg="black", font=('Arial', 20, 'bold'))
    title.pack(fill=X)
    f = Frame(root)
    f.place(x=780, y=80)
    scrollbar = Scrollbar(f)
    t = Text(f, height=30, width=50, yscrollcommand=scrollbar.set)
    scrollbar.config(command=t.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    t.pack(side="left")
    initBill()
    fa = Label(root, text="الفـــاتورة", fg='Black', font=('Arial', 18, 'bold'))
    fa.place(x=1100, y=40)
    arr = [x for x in os.listdir(os.path.join(os.getcwd(),'billes')) if x.endswith(".txt")]
    clicked = StringVar()
    drop2 = ttk.Combobox(root, textvariable=clicked, values=arr)
    drop2.config(width=30, height=10)
    drop2.place(x=850, y=50)
    drop2.bind("<<ComboboxSelected>>",open_text)
    f2 = Frame(root, bg='gold', width=415, height=125)
    f2.place(x=778, y=570)
    Button(f2, text="طباعة الفاتورة", width=28, bg='black', fg='gold',command=save_text).place(x=160, y=10)
    Button(f2, text="افراغ الحقول", width=28, bg='black', fg='gold',command=rest).place(x=160, y=50)
    Button(f2, text="اغلاق البرنامج", width=28, bg='black', fg='gold',command=sys.exit).place(x=160, y=90)
    Button(f2, text="حساب المجموع \nالكلي", width=15,height=5, bg='black', fg='gold',command=bill_go).place(x=20, y=20)
    Label(root,text="المنتج",font=('Arial', 18, 'bold'),fg="black").place(x=80,y=60)
    tab1=database.getbyunit('KG')
    drop=ttk.Combobox(root,values=tab1)
    drop.config(width=30,height=10)
    drop['state'] = 'readonly'
    drop.bind("<<ComboboxSelected>>",getPriceByName)
    drop.current(0)
    drop.place(x=80,y=105)
    Label(root,text="الوزن بالغرام",font=('Arial', 18, 'bold'),fg="black").place(x=350,y=60)
    en=Entry(root,width=18,justify="center")
    en.place(x=350,y=100,height=30)
    en2 = Entry(root, width=15,justify="center" )
    en2.place(x=500, y=100, height=30)
    Label(root,text="سعر الكيلو",font=('Arial', 18, 'bold'),fg="black").place(x=500,y=60)
    Button(root, text="إضافة للفاتورة", bg="black", fg="gold",height=2,command=calc_w).place(x=650,y=95)
    Label(root, text="المنتج", font=('Arial', 18, 'bold'), fg="black").place(x=80, y=130)
    tab=database.getbyunit('Unit')
    dropu = ttk.Combobox(root,values=tab)
    dropu.current(0)
    dropu ['state'] = 'readonly'
    dropu.config(width=30,height=10)
    dropu.bind("<<ComboboxSelected>>",getPriceByName2)
    dropu.place(x=80, y=165)
    Label(root, text="عدد الوحدات", font=('Arial', 18, 'bold'), fg="black").place(x=350, y=130)
    enu = Entry(root, width=18, justify="center")
    enu.place(x=350, y=160, height=30)
    en2u = Entry(root, width=15, justify="center")
    en2u.place(x=500, y=160, height=30)
    Label(root, text="سعر الوحدة",font=('Arial', 18, 'bold'), fg="black").place(x=500, y=130)
    Button(root, text="إضافة للفاتورة", bg="black", fg="gold", height=2,command=calc_u).place(x=650, y=155)

    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings', height=20, selectmode="browse")
    tree.column("#1", anchor=CENTER, stretch=NO)
    tree.heading("#1", text="السلعة")
    tree.column("#2", anchor=CENTER, stretch=NO)
    tree.heading("#2", text="عدد الوحدات\ الوزن")
    tree.column("#3", anchor=CENTER, stretch=NO)
    tree.heading("#3", text="السعر")

    treeScroll = ttk.Scrollbar(root)
    treeScroll.configure(command=tree.yview)
    tree.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side=LEFT, fill=BOTH)
    tree.place(x=80, y=200)
    del_btn = Button(root, text="Delete", bg="black", fg="gold", height=2,width=11, command=delete)
    del_btn.place(x=300, y=650)
