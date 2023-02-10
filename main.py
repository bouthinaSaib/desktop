from tkinter import *
from tkinter import Tk, Frame, Canvas
from PIL import ImageTk,Image
import tkinter as tk
import sys
from tkinter import messagebox
import webbrowser
import database
def funct():
    def quit():
        sys.exit()

    user1 = ''
    passw1 = ''

    def link1():
        webbrowser.open('https://www.facebook.com/informatiqueCfep')

    def link2():
        webbrowser.open('https://www.facebook.com/profile.php?id=100073478570409')

    def about():
        messagebox.showinfo("المطور", "سايب بثينة")

    def login():
        user = en1.get()
        passw = en2.get()
        if user == user1 and passw == passw1:
            messagebox.showinfo('welcome', 'أهلا بك مجددا , يوم موفق لك')
            root.destroy()
            import choose
            choose.list()
        else:
            messagebox.showerror('Error', 'يرجى التأكد من المعلومات و المحاولة ثانية')

    def openNewWindow():

        # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(root)

        def exit_btn():
            newWindow.destroy()

        # sets the title of the
        # Toplevel widget
        newWindow.title("Change password")
        # sets the geometry of toplevel
        newWindow.geometry("400x400")
        l1 = Label(newWindow, text=":كلمة السر القديمة", fg="black")
        l1.place(x=280, y=50)
        l2 = Label(newWindow, text=":كلمة السر الجديدة", fg="black")
        l2.place(x=280, y=100)
        l3 = Label(newWindow, text=":إعادة كتابة كلمة السر", fg="black")
        l3.place(x=280, y=150)
        en10 = Entry(newWindow,show="*", justify="center")
        en10.place(x=150, y=55)
        en20 = Entry(newWindow,show="*", justify="center")
        en20.place(x=150, y=105)
        en30 = Entry(newWindow,show="*", justify="center")
        en30.place(x=150, y=155)

        def changepsw():
            global passw1
            old = en10.get()
            new1 = en20.get()
            new2 = en30.get()
            if old == passw1:
                if new2 == new1:
                    passw1 = new1
                    messagebox.showinfo('مبروك', 'تم تغيير كلمة السر بنجاح')
                else:
                    messagebox.showerror('خطأ', 'كلمتي السر غير متطابقتين')
            else:
                messagebox.showerror('خطأ', 'كلمة السر القديمة خاطئة')

        b1 = Button(newWindow, text='تأكيد', width=28, bg='gold', fg='black', command=changepsw)
        b1.place(x=100, y=205)
        b2 = Button(newWindow, text='إلغاء', width=28, bg='gold', fg='black', command=exit_btn)
        b2.place(x=100, y=250)
        # A Label widget to show in toplevel
        Label(newWindow, text="تغيير كلمة السر", bg='black', fg='gold', font=('Arial', 25, 'bold')).pack(fill=X)

    def my_show():
        if (showpsw.get() == 1):
            en2.config(show='')
        else:
            en2.config(show='*')
    root = Tk()
    root.geometry("800x450+400+200")
    root.resizable(False, False)

    root.title("SuperMarket")
    root.iconbitmap('ff.ico')
    title = Label(root, text="برنامح تسيير محل", fg="gold", bg="black", font=('Arial', 20, 'bold'))
    title.pack(fill=X)
    f1 = Frame(root, width=230, height=420, bg="gold")
    f1.place(x=0, y=38)
    canvas = Canvas(f1, bg="black", width=230, height=420)
    canvas.pack()
    b = Button(f1, text="المطور", width=28, fg="black", bg="gold", command=about)
    b.place(x=6, y=280)
    b1 = Button(f1, text="صفحتنا غلى الفيسبوك", width=28, fg="black", bg="gold", command=link1)
    b1.place(x=6, y=310)
    b = Button(f1, text="اتصل بالمطور", width=28, fg="black", bg="gold", command=link2)
    b.place(x=6, y=340)
    b1 = Button(f1, text="إغلاق البرنامج", width=28, fg="black", bg="gold", command=quit)
    b1.place(x=6, y=370)
    photo = PhotoImage(file="download.png")
    imo = Label(root, image=photo)
    imo.place(x=350, y=50)
    l1 = Label(root, text=":إسم المستخدم", fg="black")
    l1.place(x=650, y=370)
    l2 = Label(root, text=":كلمة السر", fg="black")
    l2.place(x=675, y=410)
    en1 = Entry(root, justify="center")
    en1.place(x=500, y=375)
    en2 = Entry(root,show="*", justify="center")
    en2.place(x=500, y=400)
    showpsw = IntVar(value=0)
    c1 = tk.Checkbutton(root, text='Show Password', variable=showpsw,onvalue=1, offvalue=0, command=my_show)
    c1.place(x=500, y=420)
    b0 = Button(root, text="تسجبل الدخول ", width=14, height=4, fg="gold", bg="black", command=login)
    b2 = Button(root, text="تغيير كلمة السر", width=14, height=4, fg="gold", bg="black", command=openNewWindow)
    b0.place(x=380, y=370)
    b2.place(x=260, y=370)
    photo2 = PhotoImage(file="272354.png")
    imo2 = Label(root, image=photo2)
    imo2.place(x=730, y=365)
    image=Image.open("292241852_435261221942342_2908983390412372794_n-removebg-preview.png")
    resized_image = image.resize((200, 200), Image.LANCZOS)
    photoimage = ImageTk.PhotoImage(resized_image )
    canvas.create_image(100, 140, image=photoimage)
    root.mainloop()
funct()












