
from tkinter import Tk, Label, Button, PhotoImage, ttk, messagebox, Entry, END, Frame
import math
window=Tk()

window["bg"] = "#362b2b" 
window.geometry("900x600")
window.title("NEO. Math helper")
window.resizable(False,False)
window["bg"]="#362b2b"
loadimage = PhotoImage(file="atm_5.png") 


def first_build():
    global loadimage 
    roundedbutton = Label(image=loadimage,bg="#362b2b") 
    roundedbutton["border"] = "0"
    roundedbutton.place(x=254,y=20)
    btn_start=Button(text="Приступим!",font=("Arial", 22, "bold"),fg="#F1DB00",bg="#ff4900",command=lambda:build())
    btn_start.place(height=55,width=220,x=345,y=460)
    def build():
        roundedbutton.destroy()
        btn_start.destroy()
        window.geometry("900x600")
        btn=Button(text="Калькулятор",command=lambda:calc(), font=("Calibri", 27, "bold"),bg="#362b2b",fg="#f67300") 
        btn2=Button(text="Алгебра",command= lambda:alg(), font=("Calibri", 27, "bold"),bg="#f67300",fg="#362b2b")
        btn3=Button(text="Геометрия",command=lambda:geom_dop(), font=("Calibri", 27, "bold"),bg="#362b2b",fg="#f67300") 
        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
        btn.place(x=0,y=0,height=600, width=303)
        btn2.place(height=600, width=303,y=0, x=300)
        btn3.place(height=600, width=303, x=600, y=0)
        btn_back.place(x=5,y=5)
        def geom_dop():
            btn_back.destroy()
            geom()
        def back():
            btn.destroy()
            btn2.destroy()
            btn3.destroy()
            btn_back.destroy()

            first_build()
        def calc():
            btn.destroy()
            btn2.destroy()
            btn3.destroy()
            btn_back.destroy()
            window.geometry("550x600")
            class Main(Frame):
                def __init__(self, root):
                    super(Main, self).__init__(root)
                    self.build()

                def build(self):
                    self.formula = "0"
                    self.lbl = Label(text=self.formula, font=("Calibri", 27, "bold"), bg="#362b2b", foreground="orange")
                    self.lbl.place(x=45, y=90)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)
                    def back():
                        self.lbl.destroy()
                        btn_back.destroy()
                        for i in name:
                            i.destroy()
                        build()
                    name=[]
                    btns = [
                        "C", "DEL", "*", "=",
                        "1", "2", "3", "/",
                        "4", "5", "6", "+",
                        "7", "8", "9", "-",
                        "(", "0", ")", "."
                    ]

                    x = 35
                    y = 180
                    i=0
                    for bt in btns:
                        com = lambda x=bt: self.logicalc(x)
                        obj=Button(text=bt, bg="#f67300",
                                font=("Arial", 22),
                                command=com)
                        name.append(obj)
                        obj.place(x=x, y=y, width=115, height=79)                   

                        x += 120
                        if x > 425:
                            x = 35
                            y += 81

                def logicalc(self, operation):
                    try:
                        if operation == "C":
                            self.formula = ""
                        elif operation == "DEL":
                            self.formula = self.formula[0:-1]
                        elif operation == "=":
                            if self.formula[-1]=="0":
                                if self.formula[-2]=="/":
                                    self.formula = "НЕЛЬЗЯ ДЕЛИТЬ НА НОЛЬ"
                                else:
                                    self.formula = str(round(eval(self.formula),5))
                            else:
                                self.formula = str(round(eval(self.formula),5))
                        else:
                            if self.formula == "0":
                                self.formula = ""
               
                            self.formula += operation

                        self.update()
                    except:
                        self.formula="Ошибка"
                        self.update()

                def update(self):
                    if self.formula == "":
                        self.formula = "0"
                    self.lbl.configure(text=self.formula)
            app = Main(window)
            app.pack()

        def alg():
            btn.destroy()
            btn2.destroy()
            btn3.destroy()
            btn_back.destroy()
            btn_algebra1=Button(text="Нахождение\nНОД и НОК",command=lambda:destroy_alg("NOD_NOK"),bg="#f67300",fg="#362b2b",font=("Calibri",20,"bold"))
            btn_algebra1.place(height=150,width=250,x=40,y=30)
            btn_algebra2=Button(text="Сокращение \nдробей",command=lambda:destroy_alg("socr_drob"),fg="#f67300",bg="#362b2b",font=("Calibri",20,"bold"))
            btn_algebra2.place(height=150,width=250,x=330,y=30)
            btn_algebra3=Button(text="Квадратные\nуравнения",command=lambda:destroy_alg("uravn"),bg="#f67300",fg="#362b2b",font=("Calibri",20,"bold"))
            btn_algebra3.place(height=150,width=250,x=620,y=30)
            btn_algebra4=Button(text="Факториалы",command=lambda:destroy_alg("fact"),fg="#f67300",bg="#362b2b",font=("Calibri",20,"bold"))
            btn_algebra4.place(height=150,width=250,x=40,y=220)
            btn_algebra5=Button(text="Прогрессии",command=lambda:destroy_alg("progress"),bg="#f67300",fg="#362b2b",font=("Calibri",20,"bold"))
            btn_algebra5.place(height=150,width=250,x=330,y=220)
            btn_algebra6=Button(text="Разложение\nна множители",command=lambda:destroy_alg("mnoj"),fg="#f67300",bg="#362b2b",font=("Calibri",20,"bold"))
            btn_algebra6.place(height=150,width=250,x=620,y=220)
            btn_algebra7=Button(text="Проценты",command=lambda:destroy_alg("proc"),bg="#f67300",fg="#362b2b",font=("Calibri",20,"bold"))
            btn_algebra7.place(height=150,width=250,x=40,y=410)
            btn_algebra8=Button(text="Степени",command=lambda:destroy_alg("pow"),fg="#f67300",bg="#362b2b",font=("Calibri",20,"bold"))
            btn_algebra8.place(height=150,width=250,x=330,y=410)
            btn_algebra9=Button(text="Числа\nФибоначчи",command=lambda:destroy_alg("fib"),bg="#f67300",fg="#362b2b",font=("Calibri",20,"bold"))
            btn_algebra9.place(height=150,width=250,x=620,y=410)
            btn_back1=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
            btn_back1.place(x=5,y=5)
            def back():
                btn_algebra1.destroy()
                btn_algebra2.destroy()
                btn_algebra3.destroy()
                btn_algebra4.destroy()
                btn_algebra5.destroy()
                btn_algebra6.destroy()
                btn_algebra7.destroy()
                btn_algebra8.destroy()
                btn_algebra9.destroy()
                btn_back1.destroy()
                build()

            def destroy_alg(x):
                btn_algebra1.destroy()
                btn_algebra2.destroy()
                btn_algebra3.destroy()
                btn_algebra4.destroy()
                btn_algebra5.destroy()
                btn_algebra6.destroy()
                btn_algebra7.destroy()
                btn_algebra8.destroy()
                btn_algebra9.destroy()
                btn_back1.destroy()

                if x=="NOD_NOK":
                    NOD_and_NOK()
                elif x=="socr_drob":
                    socr_drob()
                elif x=="uravn":
                    uravn()
                elif x=="fact":
                    fact()
                elif x=="progress":
                    progress()
                elif x=="mnoj":
                    mnoj()
                elif x=="proc":
                    proc()
                elif x=="pow":
                    pow()
                else:
                    fib()



            def fib():
                head_fib=Label(text="Введите индекс числа Фибоначи",font="Calibri 25 bold",justify="center",bg="#362b2b",fg="#f67300")
                head_fib.place(x=220,y=10)
                ent_fib=Entry(font="Calibri 23 bold",justify="center",width=8)
                ent_fib.place(x=200,y=120)
                btn_fib=Button(text="Найти",font="Calibri 28 bold",bg="#362b2b",fg="#f67300",command=lambda:fib_find())
                btn_fib.place(x=490,y=100,height=75,width=150)
                out_fib=Label(text="           ",font=("Calibri",29,"bold"),bg="#463b3b", fg="#f67300")
                out_fib.place(x=30,y=270)
                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def back():
                    head_fib.destroy()
                    ent_fib.destroy()
                    btn_fib.destroy()
                    out_fib.destroy()
                    btn_back.destroy()
                    alg()
                def fib_find():
                    element=ent_fib.get()
                    error=0
                    try:
                        if int(element)!=float(element):
                            error=1
                            x=int("x")
                            messagebox.showinfo("Ошибка","Введите целочисленные значения   ")
                    except:
                        if error==0:
                            messagebox.showinfo("Ошибка","Введите числовые значения")
                    else:
                        element = int(element)
                        if element>200:
                            messagebox.showinfo("Ошибка","Слишком большое число\nВведите индекс не больше 200")
                        else:
                            prew = cur = 1
                            for n in range(int(element-2)):
                                tmp = prew + cur
                                prew = cur
                                cur = tmp
                            out_fib.configure(text=cur)
                            '''cur - ответ'''

            def pow():
                head_pow=Label(text="Введите значения",font="Calibri 25 bold",justify="center",bg="#362b2b",fg="#f67300")
                head_pow.place(x=320,y=10)
                ent_pow_1_1=Entry(font="Calibri 28 bold",justify="center",width=6)
                ent_pow_1_2=Entry(font="Calibri 22 bold",justify="center",width=4)
                ent_pow_1_1.place(x=80,y=170)
                ent_pow_1_2.place(x=210,y=152)
                lbl_pow_1=Label(text="",font=("Calibri",29,"bold"),bg="#463b3b", fg="#f67300",width=21)
                lbl_pow_1.place(x=440,y=170)
                btn_pow_1=Button(text="=",font="Calibri 43 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:pow_1())
                btn_pow_1.place(x=310,y=165,height=60,width=80)  
                ent_pow_2_1=Entry(font="Calibri 27 bold",justify="center",width=5)
                ent_pow_2_2=Entry(font="Calibri 27 bold",justify="center",width=5)
                ent_pow_2_3=Entry(font="Calibri 27 bold",justify="center",width=5)
                ent_pow_2_4=Entry(font="Calibri 22 bold",justify="center",width=4)
                scobka_1=Label(text="(",font=("Arial",100),bg="#362b2b", fg="#f67300")
                scobka_2=Label(text=")",font=("Arial",100),bg="#362b2b", fg="#f67300")
                scobka_1.place(x=30,y=315)
                scobka_2.place(x=300,y=315)
                cherta_pow=Label(bg="#f67300")
                cherta_pow.place(x=195,y=400,width=105,height=5)
                ent_pow_2_1.place(x=80,y=380)
                ent_pow_2_2.place(x=200,y=345)
                ent_pow_2_3.place(x=200,y=415)
                ent_pow_2_4.place(x=350,y=315)
                btn_pow_2=Button(text="=",font="Calibri 43 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:pow_2())
                btn_pow_2.place(x=410,y=375,height=60,width=80)
                cel_out_pow=Label(text="",font=("Calibri",29,"bold"),bg="#463b3b", fg="#f67300")
                chisl_out_pow=Label(text="",font=("Calibri",29,"bold"),bg="#463b3b", fg="#f67300")
                znam_out_pow=Label(text="",font=("Calibri",29,"bold"),bg="#463b3b", fg="#f67300")
                cherta_out_pow=Label(text="",font=("Calibri",29,"bold"),bg="#f67300")
                cel_out_pow.place(x=530,y=380,width=140)
                chisl_out_pow.place(x=700,y=340,width=140)
                cherta_out_pow.place(x=690,y=400,width=160,height=5)
                znam_out_pow.place(x=700,y=412,width=140)
                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def back():
                    head_pow.destroy()
                    ent_pow_1_1.destroy()
                    ent_pow_1_2.destroy()
                    lbl_pow_1.destroy()
                    btn_pow_1.destroy()
                    scobka_1.destroy()
                    scobka_2.destroy()
                    cherta_pow.destroy()
                    cel_out_pow.destroy()
                    znam_out_pow.destroy()
                    cherta_out_pow.destroy()
                    chisl_out_pow.destroy()
                    ent_pow_2_1.destroy()
                    ent_pow_2_2.destroy()
                    ent_pow_2_3.destroy()
                    ent_pow_2_4.destroy()
                    btn_pow_2.destroy()
                    btn_back.destroy()
                    alg()

                def pow_1():
                    error=0
                    chislo=ent_pow_1_1.get()
                    poww=ent_pow_1_2.get()
                    if chislo!="" or poww!="":
                        try:
                            if int(chislo)==float(chislo):
                                chislo=int(chislo)
                            else:
                                chislo=float(chislo)
                            if int(poww)==float(poww):
                                poww=int(poww)
                            else:
                                poww=float(poww)
                            chislo=chislo**poww
                            if chislo>99999999999999:
                                error=1
                                messagebox.showinfo("Ошибка","Слишком большие значения       ")
                            if error==0:
                                lbl_pow_1.configure(text=chislo)

                        except:
                            if error==0:
                                messagebox.showinfo("Ошибка","Введите числовые значения\nдля указания дробной части\nиспользуйте знак '.'")
                    else:
                        error=1
                        messagebox.showinfo("Ошибка","Введите значения")

                    

                def pow_2():
                    error=0
                    cel=ent_pow_2_1.get()
                    chisl=ent_pow_2_2.get()
                    znam=ent_pow_2_3.get()
                    poww=ent_pow_2_4.get()
                    if cel=="":
                        cel=0
                    if chisl=="" or znam=="" or poww=="":
                        error=1
                        messagebox.showinfo("Ошибка","Введите значения           ")
                    else:
                        try:
                            if int(chisl)!=float(chisl) or int(znam)!=float(znam) or int(poww)!=float(poww) or int(cel)!=float(cel):
                                messagebox.showinfo("Ошибка","Введите целые значения    ")
                                error=1
                        except:
                            if error ==0:
                                messagebox.showinfo("Ошибка","Введите числовые значения ")
                        else:
                            chisl=int(chisl)
                            znam=int(znam)
                            cel=int(cel)
                            poww=int(poww)
                            if cel<0:
                                minus="yes"
                                cel=0-cel
                            else:
                                minus=""
                            if chisl>znam:
                                cel_2=math.floor(chisl/znam)
                                cel+=cel_2
                                chisl-=cel_2*znam
                            if chisl!=0:
                                if chisl > znam:
                                    k = chisl
                                else:
                                    k = znam
                                while k != 1:
                                    if chisl % k == 0 and znam % k == 0:
                                        chisl= chisl // k
                                        znam= znam // k
                                    else:
                                        k -= 1
                            chisl+=znam*cel
                            cel=0
                            chisl=chisl**poww
                            znam=znam**poww
                            if chisl>znam:
                                cel_2=math.floor(chisl/znam)
                                if cel>=0:
                                    cel+=cel_2
                                chisl-=cel_2*znam
                            if chisl!=0:
                                if chisl > znam:
                                    k = chisl
                                else:
                                    k = znam
                                while k != 1:
                                    if chisl % k == 0 and znam % k == 0:
                                        chisl= chisl // k
                                        znam= znam // k
                                    else:
                                        k -= 1
                            if minus=="yes":
                                cel=0-cel
                            cel_out_pow.configure(text=cel)
                            chisl_out_pow.configure(text=chisl)
                            znam_out_pow.configure(text=znam)


            def proc():
                head_proc=Label(text="Введите значения",font="Calibri 25 bold",justify="center",bg="#362b2b",fg="#f67300")
                head_proc.place(x=320,y=10)
                ent_proc_1_1=Entry(font="Calibri 23 bold",justify="center")
                lbl_proc_1_1=Label(text="%  от",font=("Calibri",31,"bold"),bg="#362b2b", fg="#f67300")
                ent_proc_1_2=Entry(font="Calibri 23 bold",justify="center")
                btn_proc_1=Button(text="=",font="Calibri 43 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:proc_1())
                lbl_proc_1_out=Label(text="",font=("Calibri",31,"bold"),bg="#463b3b", fg="#f67300")
                lbl_proc_1_out.place(x=25,y=120,height=50,width=155)
                btn_proc_1.place(x=210,y=120,height=50,width=80)
                ent_proc_1_1.place(x=310,y=120,height=50,width=200)
                lbl_proc_1_1.place(x=540,y=120)
                ent_proc_1_2.place(x=660,y=120,height=50,width=200)

                ent_proc_2_1=Entry(font="Calibri 23 bold",justify="center")
                btn_proc_2=Button(text="=",font="Calibri 43 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:proc_2())
                lbl_proc_2_out=Label(text="",font=("Calibri",23,"bold"),bg="#463b3b", fg="#f67300")
                lbl_proc_2_1=Label(text="%  от",font=("Calibri",31,"bold"),bg="#362b2b", fg="#f67300")
                ent_proc_2_2=Entry(font="Calibri 23 bold",justify="center")
                ent_proc_2_1.place(x=25,y=270,height=50,width=155)
                btn_proc_2.place(x=210,y=270,height=50,width=80)
                lbl_proc_2_out.place(x=310,y=270,height=50,width=200)
                lbl_proc_2_1.place(x=540,y=270)
                ent_proc_2_2.place(x=660,y=270,height=50,width=200)
                
                ent_proc_3_1=Entry(font="Calibri 23 bold",justify="center")
                btn_proc_3=Button(text="=",font="Calibri 43 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:proc_3())
                ent_proc_3_2=Entry(font="Calibri 23 bold",justify="center")
                lbl_proc_3_1=Label(text="%  от",font=("Calibri",31,"bold"),bg="#362b2b", fg="#f67300")
                lbl_proc_3_out=Label(text="",font=("Calibri",23,"bold"),bg="#463b3b", fg="#f67300")
                ent_proc_3_1.place(x=25,y=420,height=50,width=155)
                btn_proc_3.place(x=210,y=420,height=50,width=80)
                ent_proc_3_2.place(x=310,y=420,height=50,width=200)
                lbl_proc_3_1.place(x=540,y=420)
                lbl_proc_3_out.place(x=660,y=420,height=50,width=200)

                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def back():
                    head_proc.destroy()
                    ent_proc_1_1.destroy()
                    lbl_proc_1_1.destroy()
                    ent_proc_1_2.destroy()
                    btn_proc_1.destroy()
                    lbl_proc_1_out.destroy()

                    ent_proc_2_1.destroy()
                    lbl_proc_2_1.destroy()
                    ent_proc_2_2.destroy()
                    btn_proc_2.destroy()
                    lbl_proc_2_out.destroy()

                    ent_proc_3_1.destroy()
                    lbl_proc_3_1.destroy()
                    ent_proc_3_2.destroy()
                    btn_proc_3.destroy()
                    lbl_proc_3_out.destroy()
                    btn_back.destroy()
                    alg()

                def proc_1():
                    proc_1_ch_1=ent_proc_1_1.get()
                    proc_1_ch_2=ent_proc_1_2.get()
                    try:
                        if proc_1_ch_1 !="" and proc_1_ch_2!="":
                            proc_1_ch_1=float(proc_1_ch_1)
                            proc_1_ch_2=float(proc_1_ch_2)
                        else:
                            error=int("j")
                    except:
                        messagebox.showinfo("Ошибка","Введите числовые значение          ")

                    else:
                        answer_proc_1=round(proc_1_ch_1*proc_1_ch_2/100,3)
                        if int(answer_proc_1)==float(answer_proc_1):
                            answer_proc_1=int(answer_proc_1)
                        lbl_proc_1_out.configure(text=answer_proc_1)


                def proc_2():
                    proc_2_ch_1=ent_proc_2_1.get()
                    proc_2_ch_2=ent_proc_2_2.get()
                    try:
                        if proc_2_ch_1 !="" and proc_2_ch_2!="":
                            proc_2_ch_1=float(proc_2_ch_1)
                            proc_2_ch_2=float(proc_2_ch_2)
                        else:
                            error=int("j")
                    except:
                        messagebox.showinfo("Ошибка","Введите числовые значение          ")

                    else:
                        answer_proc_2=round(100*proc_2_ch_1/proc_2_ch_2,3)
                        if int(answer_proc_2)==float(answer_proc_2):
                            answer_proc_2=int(answer_proc_2)
                        lbl_proc_2_out.configure(text=answer_proc_2)


                def proc_3():
                    proc_3_ch_1=ent_proc_3_1.get()
                    proc_3_ch_2=ent_proc_3_2.get()
                    try:
                        if proc_3_ch_1 !="" and proc_3_ch_2!="":
                            proc_3_ch_1=float(proc_3_ch_1)
                            proc_3_ch_2=float(proc_3_ch_2)
                        else:
                            error=int("j")
                    except:
                        messagebox.showinfo("Ошибка","Введите числовые значение          ")

                    else:
                        answer_proc_3=round(proc_3_ch_1*100/proc_3_ch_2,3)
                        if int(answer_proc_3)==float(answer_proc_3):
                            answer_proc_3=int(answer_proc_3)
                        lbl_proc_3_out.configure(text=answer_proc_3)


            def mnoj():
                head_mnoj=Label(text="Введите число",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300")
                head_mnoj.place(x=350,y=10)
                ent_mnoj=Entry(font="Calibri 30 bold",justify="center")
                ent_mnoj.place(x=100,y=110,height=65,width=325)
                btn_mnoj=Button(text="Найти",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_mnoj())
                btn_mnoj.place(x=550,y=110,width=150,height=65)
                lbl_mnoj=Label(text="Простые множители числа:",font=("Calibri",31,"bold"),bg="#362b2b", fg="#f67300")
                lbl_mnoj.place(x=50,y=260)

                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def back():
                    head_mnoj.destroy()
                    ent_mnoj.destroy()
                    btn_mnoj.destroy()
                    lbl_mnoj.destroy()
                    btn_back.destroy()
                    alg()
                def find_mnoj():
                    error=0
                    chisl_mnoj=ent_mnoj.get()
                    try:
                        if chisl_mnoj!="":
                            if int(chisl_mnoj)==float(chisl_mnoj):
                                chisl_mnoj=int(chisl_mnoj)
                                if chisl_mnoj<=0:
                                    error=1
                                    messagebox.showinfo("Ошибка","Введите число больше нуля")
                            else:
                                error=1
                                messagebox.showinfo("Ошибка","Введите целое положительное значение")
                        else:
                            error=1
                            messagebox.showinfo("Ошибка","Введите значение")
                    except:
                        messagebox.showinfo("Ошибка","Введите числа                            ")
                    if error==0:
                        mnojiteli=primfacs(chisl_mnoj)
                        mnojiteli=str(mnojiteli)
                        mnojiteli.replace("[","")
                        mnojiteli=mnojiteli.replace(",","*")
                        text_mnoj=(str(chisl_mnoj)+" = "+str(mnojiteli))
                        lbl_mnoj.configure(text=text_mnoj)

                        
                def primfacs(n):
                    i = 2
                    primfac = ""
                    while i * i <= n:
                        while n % i == 0:
                            primfac=(primfac+str(int(i)) +"*")
                            n = n / i
                        i = i + 1
                    if n > 1:
                        primfac=(primfac+str(int(n)))
                    if primfac[-1]=="*":
                        primfac=primfac[0:-1]
                    return primfac


            def NOD_and_NOK():
                head_NOD=Label(text="Введите нужное количество чисел",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300")
                head_NOD.place(x=220,y=10)
                ent_1=Entry(font="Calibri 22 bold",justify="center")
                ent_1.place(x=110,y=110,height=55,width=145)
                ent_2=Entry(font="Calibri 22 bold",justify="center")
                ent_2.place(x=345,y=110,height=55,width=145)
                ent_3=Entry(font="Calibri 22 bold",justify="center")
                ent_3.place(x=615,y=110,height=55,width=145)
                btn_find_NOD=Button(text="Найти",font="Calibri 31 bold",bg="#362b2b",fg="#f67300",command=lambda:find_NOD_NOK())
                btn_find_NOD.place(x=334,y=220,width=170,height=60)
                NOD_out=Label(text="",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                NOK_out=Label(text="",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                NOD_out.place(x=30,y=340)
                NOK_out.place(x=30,y=440)

                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def back():
                    head_NOD.destroy()
                    ent_1.destroy()
                    ent_2.destroy()
                    ent_3.destroy()
                    btn_find_NOD.destroy()
                    NOD_out.destroy()
                    NOK_out.destroy()
                    btn_back.destroy()
                    alg()
                def find_NOD_NOK():
                    global chislo_1,chislo_2,chislo_3
                    chislo_1=ent_1.get()
                    chislo_2=ent_2.get()
                    chislo_3=ent_3.get()
                    error=0
                    if chislo_1!="":
                        if int(chislo_1)!=float(chislo_1):
                            error=1
                            messagebox.showinfo("Ошибка","Введите целые значения")
                        else:
                            if int(chislo_1)>0:
                                chislo_1=int(chislo_1)
                            else:
                                error=1
                                messagebox.showinfo("Ошибка","Введите положительное число")
                    else:
                        error=1
                        messagebox.showinfo("Ошибка","Вводите числа, начиная с левого блока")

                    if chislo_2!="":
                        if int(chislo_2)!=float(chislo_2):
                            error=1
                            messagebox.showinfo("Ошибка","Введите целые значения")
                        else:
                            if int(chislo_2)>0:
                                chislo_2=int(chislo_2)
                            else:
                                error=1
                                messagebox.showinfo("Ошибка","Введите положительное число")    
                    else:   
                        error=1
                        messagebox.showinfo("Ошибка","Вводите числа, начиная с левого блока")

                    if chislo_3!="":
                        if int(chislo_3)!=float(chislo_3):
                            error=1
                            messagebox.showinfo("Ошибка","Введите целые значения")
                        else:
                            if int(chislo_3)>0:
                                chislo_3=int(chislo_3)
                            else:
                                error=1
                                messagebox.showinfo("Ошибка","Введите положительное число")
                    if chislo_1!="" and chislo_2!="" and chislo_3!="" and error==0:
                        NOD=gcd(chislo_1, chislo_2, chislo_3)
                        NOK=NOK_f(chislo_1,chislo_2,chislo_3)
                        text_NOD=("Наибольший общий делитель: "+str(NOD))
                        NOD_out.configure(text=text_NOD)
                        text_NOK=("Наименьшее общее кратное: "+str(NOK))
                        NOK_out.configure(text=text_NOK)

                    elif chislo_1!="" and chislo_2!="" and error==0:
                        NOD=gcd(chislo_1, chislo_2)
                        NOK=lcm(chislo_1,chislo_2)
                        text_NOD=("Наибольший общий делитель: "+str(NOD))
                        NOD_out.configure(text=text_NOD)
                        text_NOK=("Наименьшее общее кратное: "+str(NOK))
                        NOK_out.configure(text=text_NOK)

                    else:
                        messagebox.showinfo("Ошибка","Введите значения, начиная с левого блока")

                def lcm(a, b):
                    m = a * b
                    while a != 0 and b != 0:
                        if a > b:
                            a %= b
                        else:
                            b %= a
                    return m // (a + b)


                def gcd(a, b, c=None):
                    return ((a if b == 0 else gcd(b, a % b)) if c is None
                            else gcd(gcd(a, b), gcd(a, c)))
                def NOK_f(a,b,c):
                    # каноническое разложение n на простые множители    
                    def canon( n ):
                        can = []
                        for d in range( 2, n + 1 ):
                            k = 0
                            while n % d == 0:
                                 n //= d
                                 k  += 1
                            if k > 0:
                                can.append( ( d, k ) )
                        return can   
                     
                    # НОК(a,b)
                    def smallest_common( a, b ):
                        a_canon = canon( a )
                        b_canon = canon( b )
                        scm = a * b
                        for ca in a_canon:
                            for cb in b_canon:
                                if ca[ 0 ] == cb[ 0 ]:
                                    scm //= ca[ 0 ] ** min( ca[ 1 ], cb[ 1 ] )
                        return scm    
                        
                    # НОК(a,b,c)
                    def smallest_common_3( a, b, c ):
                        return  smallest_common( smallest_common( a, b ), c )            
                    return smallest_common_3( a, b, c )
                        

            def socr_drob():
                find_geom_prog_lbl1=Label(text="Введите свои значения",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                find_geom_prog_lbl1.place(x=260,y=10)
                ent_celaya_chast= Entry (font = "Calibri 24 bold",justify="center")
                ent_chislitel = Entry(font="Calibri 25 bold",justify="center")
                ent_znamenatel = Entry(font="Calibri 25 bold",justify="center")
                cherta=Label( text="", font=("Calibri",15,"bold"), bg="orange")
                cherta.place(x=160,y=299,height=4,width=110)
                btn_socr_drob = Button(text="=",font="Calibri 45 bold", bg="#362b2b", fg="#f67300",justify="center",command=lambda:socr_drob_find())
                btn_socr_drob.place(x=310,y=268, height=60 )
                ent_celaya_chast.place(x=70,y=280, width =70, height=50)
                ent_chislitel.place(x=168,y=240,width=93, height=50)
                ent_znamenatel.place(x=168,y=312,width=93, height=50)
                out_cel=Label(text="",font = "Calibri 26 bold",justify="center",fg="#f67300",bg="#362b2b")
                out_cel.place(y=265,x=420,width=70,height=70)
                out_chisl=Label(text="",font="Calibri 25 bold",justify="center",fg="#f67300",bg="#362b2b")
                out_chisl.place(y=240,x=518,width=93, height=50)
                out_znam=Label(text="",font="Calibri 25 bold",justify="center",fg="#f67300",bg="#362b2b")
                out_znam.place(x=518,y=312,width=93, height=50)
                cherta_2=Label(text="", font=("Calibri",15,"bold"),bg="#362b2b")
                cherta_2.place(x=510,y=299,height=4,width=110)
                znak_ravno=Label(text="", font=("Calibri 40 bold"),bg="#362b2b", fg="#f67300")
                znak_ravno.place(x=650, y=260)
                out_10_drob=Label(text="",font = "Calibri 26 bold",justify="center",fg="#f67300",bg="#362b2b")
                out_10_drob.place(x=695,y=270)

                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def back():
                    find_geom_prog_lbl1.destroy()
                    ent_celaya_chast.destroy()
                    ent_chislitel.destroy()
                    ent_znamenatel.destroy()
                    cherta.destroy()
                    btn_socr_drob.destroy()
                    out_cel.destroy()
                    out_chisl.destroy()
                    out_znam.destroy()
                    cherta_2.destroy()
                    znak_ravno.destroy()
                    out_10_drob.destroy()
                    btn_back.destroy()
                    alg()
                def socr_drob_find():

                    try:
                        if ent_celaya_chast.get()!="":
                            cel=int(ent_celaya_chast.get())
                        else: cel=0
                        
                        if ent_znamenatel.get()!="":
                            if ent_znamenatel.get()!="0":
                                if int(ent_znamenatel.get())>0:
                                    znam=int(ent_znamenatel.get())
                                else: messagebox.showinfo("Ошибка","Минус должен стоять перед целой частью")
                            else: messagebox.showinfo("Ошибка","Знаменатель не может быть равен '0'")
                        else:messagebox.showinfo("Ошибка","Введите знаменатель")
                        if ent_chislitel.get()!="":
                            if int(ent_chislitel.get())>=0:
                                chisl=int(ent_chislitel.get())
                            else: messagebox.showinfo("Ошибка","Минус должен стоять перед целой частью")
                        else: messagebox.showinfo("Ошибка","Введите числитель")
                    except ValueError:
                        messagebox.showinfo("Ошибка","Введите целые числа")

                    if chisl == znam:
                        if cel>=0:
                            cel+=1
                        elif cel<0:
                            cel-=1
                        chisl=0
                    elif chisl > znam:
                        cel_2=math.floor(chisl/znam)
                        if cel>=0:
                            cel+=cel_2
                        elif cel<0:
                            cel-=cel_2
                        chisl-=cel_2*znam
                        if chisl!=0:
                            if chisl > znam:
                                k = chisl
                            else:
                                k = znam
                            while k != 1:
                                if chisl % k == 0 and znam % k == 0:
                                    chisl= chisl // k
                                    znam= znam // k
                                else:
                                    k -= 1
                    elif chisl < znam:
                        if chisl > znam:
                            k = chisl
                        else:
                            k = znam
                        while k != 1:
                            if chisl % k == 0 and znam % k == 0:
                                chisl= chisl // k
                                znam= znam // k
                            else:
                                k -= 1
                    out_chisl.configure(text=chisl)
                    out_znam.configure(text=znam)
                    out_cel.configure(text=cel)

                    if chisl==0: 
                       cherta_2.configure(bg="#362b2b")
                       out_chisl.configure(text="")
                       out_znam.configure(text="")
                       znak_ravno.configure(text="")
                       out_10_drob.configure(text="")
                    else:
                        znak_ravno.configure(text="=")
                        if cel>0:
                            drob_10 = round(cel+chisl/znam,6)
                        else:
                            drob_10 = round(cel-chisl/znam,6)
                        out_10_drob.configure(text=drob_10)
                        cherta_2.configure(bg="#f67300")
                    if cel==0:
                       cel=""
                       out_cel.configure(text=cel)


            def uravn():
                head_uravn=Label(text="Введите коэфиценты\N{SUPERSCRIPT TWO}",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300")
                head_uravn.place(x=290,y=10)
                ent_A=Entry(font="Calibri 22 bold",justify="center")
                ent_A.place(x=40,y=110,height=45,width=75)
                lbl_xx=Label(text="x\N{SUPERSCRIPT TWO}",font="Calibri 31 bold",bg="#362b2b",fg="#f67300")
                lbl_xx.place(x=125,y=103)
                plus_1=Label(text="+",font="Calibri 35 bold",bg="#362b2b",fg="#f67300")
                plus_1.place(x=175,y=96)
                ent_B=Entry(font="Calibri 22 bold",justify="center")
                ent_B.place(x=215,y=110,height=45,width=75)
                lbl_x=Label(text="x",font="Calibri 31 bold",bg="#362b2b",fg="#f67300")
                lbl_x.place(x=300,y=103)
                plus_2=Label(text="+",font="Calibri 35 bold",bg="#362b2b",fg="#f67300")
                plus_2.place(x=345,y=96)
                ent_C=Entry(font="Calibri 22 bold",justify="center")
                ent_C.place(x=385,y=110,height=45,width=75)
                znak_ravno_zero=Label(text="=  0",font="Calibri 31 bold",bg="#362b2b",fg="#f67300")
                znak_ravno_zero.place(x=465,y=103)
                ent_A.insert(0,"A")
                ent_B.insert(0,"B")
                ent_C.insert(0,"C")
                btn_find_uravn=Button(text="Найти",font="Calibri 31 bold",bg="#362b2b",fg="#f67300",command=lambda:find_uravn())
                btn_find_uravn.place(x=580,y=100,width=170,height=60)
                discr=Label(text="",font="Calibri 28 bold",justify="left", fg="#f67300",bg="#362b2b")
                discr.place(x=25,y=230)
                lbl_x_1=Label(text="",font="Calibri 28 bold",fg="#f67300",bg="#362b2b")
                lbl_x_2=Label(text="",font="Calibri 28 bold",fg="#f67300",bg="#362b2b")
                btn_clear=Button(text="Очистить", command=lambda:clear(),font=("Calibri",15,"bold"),fg="#ffffff",bg="#ff0059")
                btn_clear.place(x=210,y=175,height=40,width=90)

                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def clear():
                    ent_A.delete(0,END)
                    ent_B.delete(0,END)
                    ent_C.delete(0,END)
                    discr.configure(text="")
                    lbl_x_1.configure(text="")
                    lbl_x_2.configure(text="")


                def back():
                    head_uravn.destroy()
                    ent_A.destroy()
                    lbl_xx.destroy()
                    plus_1.destroy()
                    ent_B.destroy()
                    lbl_x.destroy()
                    plus_2.destroy()
                    ent_C.destroy()
                    znak_ravno_zero.destroy()
                    btn_find_uravn.destroy()
                    discr.destroy()
                    lbl_x_1.destroy()
                    lbl_x_2.destroy()
                    btn_clear.destroy()
                    btn_back.destroy()
                    alg()
                def find_uravn():
                    global discriminant,A,B,C
                    A=ent_A.get()
                    B=ent_B.get()
                    C=ent_C.get()
                    error=0
                    lbl_x_1.configure(text="")
                    lbl_x_2.configure(text="")
                    try:
                        if A=="":
                            ent_A.insert(0,1)
                        else:
                            A=float(A)
                            if A==0:
                                error=1

                        if B=="":
                            ent_B.insert(0,0)
                            B=0
                        else:
                            B=float(B)

                        if C=="":
                            ent_C.insert(0,0)
                            C=0
                        else:
                            C=float(C)
                        if error==1:
                            error=2/0
                    except:
                        messagebox.showinfo("Ошибка","Введены некорректные данные\nЕсли вы оставляете поле пустым,\nто оно считается как '0'\nКоэфицент 'A' не может быть равен нулю")
                    else:
                        if int(A)==float(A):
                            A=int(A)
                        if int(B)==float(B):
                            B=int(B)
                        if int(C)==float(C):
                            C=int(C)
                        txt_uravn=("("+str(B)+" * "+str(B)+") - ("+"4 * "+str(A) + " * "+str(C)+")")
                        discriminant=eval(txt_uravn)
                        if discriminant>=0:
                            txt_uravn_in_lbl=("D = "+ txt_uravn+" = "+ str(discriminant))
                            discr.configure(text=txt_uravn_in_lbl)
                            find_korni()
                        else:
                            txt_uravn_in_lbl=(("D = "+ txt_uravn+" = "+ str(discriminant))+"\nДискриминант меньше нуля. Корней нет")
                            discr.configure(text=txt_uravn_in_lbl)
                def find_korni():
                    global A,B,C,discriminant
                    discriminant=float(discriminant)
                    if discriminant==0:
                        if B>0:
                            txt_x_1_uravn_out=("X = -"+str(B)+" ± √"+str(discriminant)+"  / 2 * "+str(A)+" = ")
                        else:
                            txt_x_1_uravn_out=("X = "+str(-B)+" ± √"+str(discriminant)+"  / 2 * "+str(A)+" = ")
                        koren_discriminant=discriminant**0.5
                        koren_discriminant=str(koren_discriminant)
                        txt_x_1_uravn_in=("( -"+str(B)+")  /  2 *"+str(A))
                        txt_x_1_uravn_out=(str(txt_x_1_uravn_out)+str(round(eval(txt_x_1_uravn_in),5)))
                        lbl_x_1.place(x=25,y=300)
                        lbl_x_1.configure(text=txt_x_1_uravn_out)
                    if discriminant>0:
                        if B>0:
                            txt_x_1_uravn_out=("X\N{SUBSCRIPT ONE} = -"+str(B)+" + √"+str(discriminant)+"  / 2 * "+str(A)+" = ")
                        else:
                            txt_x_1_uravn_out=("X\N{SUBSCRIPT ONE} = "+str(-B)+" + √"+str(discriminant)+"  / 2 * "+str(A)+" = ")
                        koren_discriminant=discriminant**0.5
                        koren_discriminant=str(koren_discriminant)
                        txt_x_1_uravn_in=("(( -"+str(B)+") + "+str(koren_discriminant)+")  /  (2 *"+str(A)+")")
                        txt_x_1_uravn_out=(str(txt_x_1_uravn_out)+str(round(eval(txt_x_1_uravn_in),5)))
                        lbl_x_1.place(x=25,y=340)
                        lbl_x_1.configure(text=txt_x_1_uravn_out)
                        '''Второй корень ↓'''
                        if B>0:
                            txt_x_2_uravn_out=("X\N{SUBSCRIPT TWO} = -"+str(B)+" - √"+str(discriminant)+"  / 2 * "+str(A)+" = ")
                        else:
                            txt_x_2_uravn_out=("X\N{SUBSCRIPT TWO} = "+str(-B)+" - √"+str(discriminant)+"  / 2 * "+str(A)+" = ")
                        koren_discriminant=discriminant**0.5
                        koren_discriminant=str(koren_discriminant)
                        txt_x_2_uravn_in=("(( -"+str(B)+") - "+str(koren_discriminant)+")  /  (2 *"+str(A)+")")
                        txt_x_2_uravn_out=(str(txt_x_2_uravn_out)+str(round(eval(txt_x_2_uravn_in),5)))
                        lbl_x_2.place(x=25,y=420)
                        lbl_x_2.configure(text=txt_x_2_uravn_out)


            def fact():
                btn_fact1=Button(text="\nФакториал\n\n1*2*3*4...",command=lambda:destroy_fact("fact1"),bg="#f67300",font=("Calibri",30,"bold"),fg="#362b2b")
                btn_fact1.place(x=0,y=0,height=600,width=452)
                btn_fact2=Button(text="Функция, похожая\nна факториал, но\nвместо '*' знак '+'\n1+2+3+4...",command=lambda:destroy_fact("fact2"),bg="#362b2b",font=("Calibri",30,"bold"),fg="#f67300")
                btn_fact2.place(x=450,y=0,height=600,width=452)

                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def back():
                    btn_fact1.destroy()
                    btn_fact2.destroy()
                    btn_back.destroy()
                    alg()
                def destroy_fact(x):
                    btn_fact1.destroy()
                    btn_fact2.destroy()
                    btn_back.destroy()
                    if x=="fact1":
                        fact1()
                    else:
                        fact2()
                def fact1():
                    find_fact1=Label(text="Введите свои значения",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                    find_fact1.place(x=215,y=10)
                    ent_fact1= Entry (font = "Calibri 24 bold",justify="center")
                    ent_fact1.place(x=50,y=145, width =70, height=50)
                    btn_fact1 = Button(text="=",font="Calibri 50", bg="#362b2b", fg="#f67300",justify="center",command=lambda:fact1_find())
                    btn_fact1.place(x=160,y=143, height=60 )
                    fact1_znak=Label(text="!",font=("Calibri",32,"bold"),bg="#362b2b", fg="#f67300")
                    fact1_znak.place(x=123,y=140)
                    answer_fact1=Label(text="",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                    answer_fact1.place(x=280,y=145)
                    lbl_line=Label(text="", bg="#f67300")
                    lbl_line.place(x=-2,y=250,width=920,height=5)
                    qst_fact1_dop=Label(text="Введите дополнительные параметры\n*ноль исключается (Например:(..(-2)*(-1)*1*2..)*",font=("Calibri",25,"bold"),bg="#362b2b", fg="#f67300")
                    qst_fact1_dop.place(x=140,y=265)
                    qst_fact1_dop_1=Label(text="Первый член =",font=("Calibri",20,"bold"),bg="#362b2b", fg="#f67300")
                    qst_fact1_dop_1.place(x=40,y=370)
                    ent_fact1_dop_1=Entry(font = "Calibri 24 bold",justify="center")
                    ent_fact1_dop_1.place(x=240,y=370,width=70)
                    qst_fact1_dop_2=Label(text="Последний член =",font=("Calibri",20,"bold"),bg="#362b2b", fg="#f67300")
                    qst_fact1_dop_2.place(x=465,y=370)
                    ent_fact1_dop_2=Entry(font = "Calibri 24 bold",justify="center")
                    ent_fact1_dop_2.place(x=700,y=370,width=70)
                    btn_fact1_dop=Button(text="=",font="Calibri 50", bg="#362b2b", fg="#f67300",justify="center",command=lambda:fact1_find_dop())
                    btn_fact1_dop.place(x=40, y=460, height=60)
                    answer_fact1_dop=Label(text="",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                    answer_fact1_dop.place(x=150,y=460)

                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)
                    def back():
                        find_fact1.destroy()
                        ent_fact1.destroy()
                        btn_fact1.destroy()
                        fact1_znak.destroy()
                        answer_fact1.destroy()
                        lbl_line.destroy()
                        qst_fact1_dop.destroy()
                        qst_fact1_dop_1.destroy()
                        ent_fact1_dop_1.destroy()
                        qst_fact1_dop_2.destroy()
                        ent_fact1_dop_2.destroy()
                        btn_fact1_dop.destroy()
                        answer_fact1_dop.destroy()
                        btn_back.destroy()
                        fact()
                    def fact1_find():
                        error=0
                        fact_znam=ent_fact1.get()
                        try:
                            fact1_proba=int(fact_znam)
                            if int(fact_znam)!=float(fact_znam):
                                fact1_proba=1/0
                        except:
                            messagebox.showinfo("Ошибка","Введите целочисленные значения")
                        else:
                            if fact_znam=="":
                                messagebox.showinfo("Ошибка","Введи корректные значения")
                                error=1
                            if int(fact_znam)<1:
                                messagebox.showinfo("Ошибка","Введи число, большее или равное '1'")
                                error=1
                            if error==0:
                                answ_fact1=math.factorial(int(fact_znam))
                                answer_fact1.configure(text=answ_fact1)  

                    def fact1_find_dop():
                        fact_1_first=ent_fact1_dop_1.get()
                        fact_1_last=ent_fact1_dop_2.get()
                        try:
                            error=0
                            if fact_1_first!="" and fact_1_last!="":
                                if int(fact_1_first)==float(fact_1_first):
                                    first_f1=int(fact_1_first)
                                else:
                                    error=1
                                if int(fact_1_last)==float(fact_1_last):
                                    last_f1=int(fact_1_last)
                                else:
                                    error=1
                                if fact_1_last<fact_1_first:
                                    error=1
                            else:
                                error=1
                            if error==1:
                                proba=1/0
                        except:
                            messagebox.showinfo("Ошибка","Введите целые числа")
                        else:
                            i=first_f1
                            answ_fact1_dop=first_f1
                            if first_f1==-1:
                                i+=2
                            while i!=last_f1:
                                if i!=-1:
                                    i+=1
                                else:
                                    i+=2
                                answ_fact1_dop*=i
                            answer_fact1_dop.configure(text=answ_fact1_dop)
                           # answer_fact1_dop.configure(text=answ_fact1_dop)



                def fact2():
                    find_fact2=Label(text="Введите свои значения\n1+2+...+ Ваше число.",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                    find_fact2.place(x=215,y=10)
                    ent_fact2= Entry (font = "Calibri 24 bold",justify="center")
                    ent_fact2.place(x=55,y=145, width =70, height=50)
                    btn_fact2 = Button(text="=",font="Calibri 50", bg="#362b2b", fg="#f67300",justify="center",command=lambda:fact2_find())
                    btn_fact2.place(x=160,y=143, height=60 )
                    answer_fact2=Label(text="",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                    answer_fact2.place(x=280,y=145)
                    lbl_line=Label(text="", bg="#f67300")
                    lbl_line.place(x=-2,y=270,width=920,height=5)
                    qst_fact2_dop=Label(text="Введите дополнительные параметры",font=("Calibri",25,"bold"),bg="#362b2b", fg="#f67300")
                    qst_fact2_dop.place(x=140,y=285)
                    qst_fact2_dop_1=Label(text="Первый член =",font=("Calibri",20,"bold"),bg="#362b2b", fg="#f67300")
                    qst_fact2_dop_1.place(x=40,y=370)
                    ent_fact2_dop_1=Entry(font = "Calibri 24 bold",justify="center")
                    ent_fact2_dop_1.place(x=240,y=370,width=70)
                    qst_fact2_dop_2=Label(text="Последний член =",font=("Calibri",20,"bold"),bg="#362b2b", fg="#f67300")
                    qst_fact2_dop_2.place(x=465,y=370)
                    ent_fact2_dop_2=Entry(font = "Calibri 24 bold",justify="center")
                    ent_fact2_dop_2.place(x=700,y=370,width=70)
                    btn_fact2_dop=Button(text="=",font="Calibri 50", bg="#362b2b", fg="#f67300",justify="center",command=lambda:fact2_find_dop())
                    btn_fact2_dop.place(x=40, y=460, height=60)
                    answer_fact2_dop=Label(text="",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                    answer_fact2_dop.place(x=150,y=460)

                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)
                    def back():
                        find_fact2.destroy()
                        ent_fact2.destroy()
                        btn_fact2.destroy()
                        answer_fact2.destroy()
                        lbl_line.destroy()
                        qst_fact2_dop.destroy()
                        qst_fact2_dop_1.destroy()
                        ent_fact2_dop_1.destroy()
                        qst_fact2_dop_2.destroy()
                        ent_fact2_dop_2.destroy()
                        btn_fact2_dop.destroy()
                        answer_fact2_dop.destroy()
                        btn_back.destroy()
                        fact()
                    def fact2_find():
                        error=0
                        fact2_znam=ent_fact2.get()
                        answ_fact2=0
                        try:
                            fact2_proba=int(fact2_znam)
                            if int(fact2_znam)!=float(fact2_znam):
                                fact2_proba=1/0
                        except:
                            messagebox.showinfo("Ошибка","Введите целочисленные значения")
                        else:
                            if fact2_znam=="":
                                messagebox.showinfo("Ошибка","Введи корректные значения")
                                error=1
                            if int(fact2_znam)<1:
                                messagebox.showinfo("Ошибка","Введи число, большее или равное '1'")
                                error=1
                            if error==0:
                                i=0
                                while i != int(fact2_znam):
                                    i+=1
                                    answ_fact2+=i
                                    
                                answer_fact2.configure(text=answ_fact2)  

                    def fact2_find_dop():
                        fact_2_first=ent_fact2_dop_1.get()
                        fact_2_last=ent_fact2_dop_2.get()
                        try:
                            error=0
                            if fact_2_first!="" and fact_2_last!="":
                                if int(fact_2_first)==float(fact_2_first):
                                    first_f2=int(fact_2_first)
                                else:
                                    error=1
                                if int(fact_2_last)==float(fact_2_last):
                                    last_f2=int(fact_2_last)
                                else:
                                    error=1
                                if fact_2_last<fact_2_first:
                                    error=1
                            else:
                                error=1
                            if error==1:
                                proba=1/0
                        except:
                            messagebox.showinfo("Ошибка","Введите целые числа")
                        else:
                            i=first_f2
                            answ_fact2_dop=first_f2
                            while i!=last_f2:
                                i+=1
                                answ_fact2_dop+=i
                            answer_fact2_dop.configure(text=answ_fact2_dop)


            def progress():
                btn_arif_progr=Button(text="Арифметические \nпрогрессии",command=lambda:destroy_progress("arif_progr"),bg="#f67300",font=("Calibri",30,"bold"),fg="#362b2b")
                btn_arif_progr.place(x=0,y=0,height=600,width=452)
                btn_geom_progr=Button(text="Геометрические \nпрогрессии",command=lambda:destroy_progress("geom_progr"),bg="#362b2b",font=("Calibri",30,"bold"),fg="#f67300")
                btn_geom_progr.place(x=450,y=0,height=600,width=452)

                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def back():
                    btn_arif_progr.destroy()
                    btn_geom_progr.destroy()
                    btn_back.destroy()
                    alg()
                def destroy_progress(x):
                    btn_arif_progr.destroy()
                    btn_geom_progr.destroy()
                    btn_back.destroy()
                    if x == "arif_progr":
                        arif_progr()
                    else:
                        geom_progr()
                def geom_progr():
                    find_geom_prog_lbl1=Label(text="Что вам нужно найти?",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                    find_geom_prog_lbl1.place(x=260,y=10)
                    btn_geom1=Button(text="Сумма\nSn",command=lambda:geom_prog("Sn"),bg="#f67300",font=("Calibri",25,"bold"),fg="#c90700")
                    btn_geom2=Button(text="Знаменатель\nq",command=lambda:geom_prog("q"),bg="#f67300",font=("Calibri",25,"bold"),fg="#c90700")
                    btn_geom3=Button(text="Первый член\nB1",command=lambda:geom_prog("B1"),bg="#f67300",font=("Calibri",25,"bold"),fg="#c90700")
                    btn_geom4=Button(text="'n'-ый член\nBn",command=lambda:geom_prog("Bn"),bg="#f67300",font=("Calibri",25,"bold"),fg="#c90700")
                    btn_geom5=Button(text="Индекс n",command=lambda:geom_prog("n"),bg="#f67300",font=("Calibri",25,"bold"),fg="#c90700")
                    btn_geom1.place(x=50,y=110,width=240,height=170)
                    btn_geom2.place(x=330,y=110,width=240,height=170)
                    btn_geom3.place(x=610,y=110,width=250,height=170)
                    btn_geom4.place(x=50,y=350,width=370,height=170)
                    btn_geom5.place(x=470,y=350,width=385,height=170)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)
                    def back():
                        find_geom_prog_lbl1.destroy()
                        btn_geom1.destroy()
                        btn_geom2.destroy()
                        btn_geom3.destroy()
                        btn_geom4.destroy()
                        btn_geom5.destroy()
                        btn_back.destroy()
                        progress()
                    def geom_prog(x):
                        find_geom_prog_lbl1.destroy()
                        btn_geom1.destroy()
                        btn_geom2.destroy()
                        btn_geom3.destroy()
                        btn_geom4.destroy()
                        btn_geom5.destroy()
                        btn_back.destroy()
                        if x=="Sn":
                            Sn()
                        elif x=="q":
                            q()
                        elif x=="B1":
                            B1()
                        elif x=="Bn":
                            Bn()
                        elif x=="n":
                            n()
     


                    def Sn():
                        bg=Label(text="", bg="#f67300")
                        bg.place(width=300,height=460, x=80,y=90)
                        lbl_quest=Label(text="Введите значения",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                        lbl_quest.place(x=200, y=20)
                        ent_B1=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_B1.place(x=230,y=125)
                        ent_Bn=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_Bn.place(x=230,y=205)
                        ent_q=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_q.place(x=230,y=290)
                        ent_n=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_n.place(x=230,y=380)
                        find_geom_prog_lbl2=Label(text="B1 =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl2.place(x=150,y=115,width=70)
                        find_geom_prog_lbl3=Label(text="Bn =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl3.place(x=150,y=195,width=70)
                        find_geom_prog_lbl4=Label(text="q =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl4.place(x=150,y=280,width=70)
                        find_geom_prog_lbl5=Label(text="n =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl5.place(x=150,y=370,width=70)
                        btn_clear=Button(text="Очистить", command=lambda:clear(),font=("Calibri",15,"bold"),fg="#ffffff",bg="#ff0059")
                        btn_clear.place(x=230,y=480,height=40,width=90)
                        btn_arif_prog_next=Button(text="Найти",command=lambda:find_Sn_geom_prog(),font=("Calibri", 20, "bold"),bg="#eeff00")
                        btn_arif_prog_next.place(x=540,y=480)
                        lbl_Sn=Label(text="Sn=",font=("Calibri",50,"bold"),bg="#362b2b",fg="#f67300")
                        lbl_Sn.place(x=440,y=180)
                        answer_Sn=Label(text="",font=("Calibri",50,"bold"),bg="#362b2b",fg="#f67300")
                        answer_Sn.place(x=550,y=180)
                        comment=Label(text="",font=("Calibri",20,"bold"),bg="#362b2b",fg="#f67300")
                        comment.place(x=430,y=300,width=430)

                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            bg.destroy()
                            lbl_quest.destroy()
                            ent_B1.destroy()
                            ent_Bn.destroy()
                            ent_q.destroy()
                            ent_n.destroy()
                            find_geom_prog_lbl2.destroy()
                            find_geom_prog_lbl3.destroy()
                            find_geom_prog_lbl4.destroy()
                            find_geom_prog_lbl5.destroy()
                            btn_clear.destroy()
                            btn_arif_prog_next.destroy()
                            lbl_Sn.destroy()
                            answer_Sn.destroy()
                            comment.destroy()
                            btn_back.destroy()
                            geom_progr()
                        def clear():
                            ent_B1.delete(0,END)
                            ent_Bn.delete(0,END)
                            ent_q.delete(0,END)
                            ent_n.delete(0,END)
                            comment.configure(text="")
                            answer_Sn.configure(text="")
                        def find_Sn_geom_prog():
                            B1=ent_B1.get()
                            Bn=ent_Bn.get()
                            q=ent_q.get()
                            n=ent_n.get()
                            list_check=[]
                            Sn_find2=0
                            Sn_find3=0
                            Sn_ogran_1=0
                            Sn=""
                            Sn_ogran=0
                            error=0
                            answer_Sn.configure(text="")
                            comment.configure(text="")

                            try:
                                if B1!="":
                                    B1=float(B1)
                                    list_check.append("B1")
                                if Bn!="":
                                    Bn=float(Bn)
                                    list_check.append("Bn")
                                if q!="":
                                    q=float(q)
                                    list_check.append("q")
                                if n!="":
                                    n=int(n)
                                    list_check.append("n")
                                    if n==0 or int(n)!=float(n):
                                        n_proba=1/0
                            except:
                                messagebox.showinfo("Ошибка","Введите числа\nДробнуя часть вводите через точку\nЗначение 'n' должно быть целым натуральным числом")
                            else:
                                if "q" in list_check:
                                    if q ==1:
                                        comment.configure(text="Все члены прогрессии \n одинаковы")
                                        if "n" in list_check:
                                            if "Bn" in list_check:
                                                Sn=Bn*n
                                            if "B1" in list_check:
                                                if Sn!="":
                                                    if Sn==B1*n:
                                                        answer_Sn.configure(text=Sn)
                                                    else: 
                                                        Sn=""
                                                        error=1
                                                        messagebox.showinfo("Ошибка","Неверно введены данные.\n Такой прогрессии не существует")
                                                else:
                                                    Sn=B1*n
                                        else:
                                            messagebox.showinfo("Ошибка","Недостаточно данных")

                                    if abs(q)<1:
                                        if "B1" in list_check:
                                            Sn_ogran_1=B1/(1-q)
                                            Sn_ogran=Sn_ogran_1
                                        if "Bn" in list_check:
                                            if Sn_ogran_1!=0:
                                                if "n" in list_check:
                                                    Sn_ogran_2 = Bn/((q**(n-1))*(1-q))
                                                    if Sn_ogran_1==Sn_ogran_2:
                                                        Sn_ogran=Sn_ogran_1
                                                    else:
                                                        error=1
                                                        messagebox.showinfo("Ошибка","Неверно введены данные.\n Такой прогрессии не существует")

                                            else: 
                                                if "n" in list_check:
                                                    Sn_ogran_2 = Bn/((q**(n-1))*(1-q))
                                                    Sn_ogran=Sn_ogran_2                          
                                                else:
                                                    error=1
                                                    messagebox.showinfo("Ошибка","Неверно введены данные.\n Такой прогрессии не существует")

                                                
                                        if Sn_ogran!=0:
                                            Sn_ogran=round(Sn_ogran,3)
                                            comm1="Бесконечно убывающая \nпрогрессия, стремящаяся к "
                                            comm=(comm1 + str(Sn_ogran))
                                            comment.configure(text=comm)
                                        else:
                                            messagebox.showinfo("Ошибка","Недостаточно данных")

                                        
                                        '''Первое решение'''
                                    if q!=1:
                                        if "Bn" in list_check and "B1" in list_check:
                                            Sn = ((Bn*q-B1)/(q-1))
                                        """Второе решение"""
                                        if "n" in list_check and "B1" in list_check:
                                            Sn_find2 = ((B1*((q**n)-1))/(q-1))
                                            if Sn!="":
                                                if Sn==Sn_find2:
                                                    Sn=Sn_find2
                                                else:
                                                    Sn=""
                                                    error=1
                                                    messagebox.showinfo("Ошибка","Неверно введены данные.\n Такой прогрессии не существует")
                                                    
                                            else: 
                                                Sn=Sn_find2
                                        if "Bn" in list_check and "n" in list_check:
                                            Sn_find3=(Bn*q-(Bn/(q**(n-1))))/(q-1)
                                            if Sn!="":
                                                if Sn == Sn_find3:
                                                    Sn=Sn_find3
                                                else:
                                                    Sn=""
                                                    error=1
                                                    messagebox.showinfo("Ошибка","Неверно введены данные.\n Такой прогрессии не существует")
                                            else: 
                                                Sn=Sn_find3
                                    if Sn!="" and error==0:
                                        answer_Sn.configure(text=round(Sn,4))
                                else: 
                                    if "Bn" in list_check and "n" in list_check and "B1" in list_check:
                                        q = (Bn/B1)**(1/(n-1))
                                        Sn=(Bn*q-B1)/(q-1)
                                        answer_Sn.configure(text=round(Sn,4))
                                    else: 

                                        messagebox.showinfo("Ошибка","Недостаточно данных")

                    def q():
                        bg=Label(text="", bg="#f67300")
                        bg.place(width=300,height=460, x=80,y=90)
                        lbl_quest=Label(text="Введите значения",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                        lbl_quest.place(x=200, y=20)
                        ent_B1=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_B1.place(x=230,y=125)
                        ent_Bn=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_Bn.place(x=230,y=205)
                        ent_Sn=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_Sn.place(x=230,y=290)
                        ent_n=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_n.place(x=230,y=380)
                        find_geom_prog_lbl2=Label(text="B1 =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl2.place(x=150,y=115,width=70)
                        find_geom_prog_lbl3=Label(text="Bn =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl3.place(x=150,y=195,width=70)
                        find_geom_prog_lbl4=Label(text="Sn =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl4.place(x=150,y=280,width=70)
                        find_geom_prog_lbl5=Label(text="n =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl5.place(x=150,y=370,width=70)
                        btn_clear=Button(text="Очистить", command=lambda:clear(),font=("Calibri",15,"bold"),fg="#ffffff",bg="#ff0059")
                        btn_clear.place(x=230,y=480,height=40,width=90)
                        btn_arif_prog_next=Button(text="Найти",command=lambda:find_q_geom_prog(),font=("Calibri", 20, "bold"),bg="#eeff00")
                        btn_arif_prog_next.place(x=540,y=480)
                        lbl_q=Label(text="q =",font=("Calibri",50,"bold"),bg="#362b2b",fg="#f67300")
                        lbl_q.place(x=440,y=180)
                        answer_q=Label(text="",font=("Calibri",50,"bold"),bg="#362b2b",fg="#f67300")
                        answer_q.place(x=550,y=180)
                        comment=Label(text="",font=("Calibri",20,"bold"),bg="#362b2b",fg="#f67300")
                        comment.place(x=430,y=300,width=430)

                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            bg.destroy()
                            lbl_quest.destroy()
                            ent_B1.destroy()
                            ent_Bn.destroy()
                            ent_Sn.destroy()
                            ent_n.destroy()
                            find_geom_prog_lbl2.destroy()
                            find_geom_prog_lbl3.destroy()
                            find_geom_prog_lbl4.destroy()
                            find_geom_prog_lbl5.destroy()
                            btn_clear.destroy()
                            btn_arif_prog_next.destroy()
                            lbl_q.destroy()
                            answer_q.destroy()
                            comment.destroy()
                            btn_back.destroy()
                            geom_progr()
                        def clear():
                            ent_B1.delete(0,END)
                            ent_Bn.delete(0,END)
                            ent_Sn.delete(0,END)
                            ent_n.delete(0,END)
                            comment.configure(text="")
                            answer_q.configure(text="")
                        def find_q_geom_prog():
                            B1=ent_B1.get()
                            Bn=ent_Bn.get()
                            Sn=ent_Sn.get()
                            n=ent_n.get()
                            list_check=[]
                            q=""
                            error=0
                            answer_q.configure(text="")
                            comment.configure(text="")
                            try:
                                if B1!="":
                                    B1=float(B1)
                                    list_check.append("B1")
                                if Bn!="":
                                    Bn=float(Bn)
                                    list_check.append("Bn")
                                if Sn!="":
                                    Sn=float(Sn)
                                    list_check.append("Sn")
                                if n!="":
                                    n=int(n)
                                    list_check.append("n")
                                    if n==0 or int(n)!=float(n):
                                        n_proba=1/0
                            except:
                                messagebox.showinfo("Ошибка","Введите числа\nДробнуя часть вводите через точку\nЗначение 'n' должно быть целым натуральным числом")
                            else:
                                if "B1" in list_check and "Bn" in list_check:
                                    if B1==Bn:
                                        q=1
                                    elif "n" in list_check and n!=1:
                                        q=((Bn/B1) ** (1/(n-1)))
                                    else:
                                        messagebox.showinfo("Ошибка","Недостаточно данных")
                                else:
                                    messagebox.showinfo("Ошибка","Недостаточно данных")
                                if q!="":
                                    answer_q.configure(text=round(q,4))

                    def B1():
                        bg=Label(text="", bg="#f67300")
                        bg.place(width=300,height=460, x=80,y=90)
                        lbl_quest=Label(text="Введите значения",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                        lbl_quest.place(x=200, y=20)
                        ent_q=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_q.place(x=230,y=125)
                        ent_Bn=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_Bn.place(x=230,y=205)
                        ent_Sn=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_Sn.place(x=230,y=290)
                        ent_n=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_n.place(x=230,y=380)
                        find_geom_prog_lbl2=Label(text="q =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl2.place(x=150,y=115,width=70)
                        find_geom_prog_lbl3=Label(text="Bn =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl3.place(x=150,y=195,width=70)
                        find_geom_prog_lbl4=Label(text="Sn =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl4.place(x=150,y=280,width=70)
                        find_geom_prog_lbl5=Label(text="n =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl5.place(x=150,y=370,width=70)
                        btn_clear=Button(text="Очистить", command=lambda:clear(),font=("Calibri",15,"bold"),fg="#ffffff",bg="#ff0059")
                        btn_clear.place(x=230,y=480,height=40,width=90)
                        btn_arif_prog_next=Button(text="Найти",command=lambda:find_B1_geom_prog(),font=("Calibri", 20, "bold"),bg="#eeff00")
                        btn_arif_prog_next.place(x=540,y=480)
                        lbl_B1=Label(text="B1 =",font=("Calibri",50,"bold"),bg="#362b2b",fg="#f67300")
                        lbl_B1.place(x=430,y=180)
                        answer_B1=Label(text="",font=("Calibri",50,"bold"),bg="#362b2b",fg="#f67300")
                        answer_B1.place(x=560,y=180)
                        comment=Label(text="",font=("Calibri",20,"bold"),bg="#362b2b",fg="#f67300")
                        comment.place(x=430,y=300,width=430)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            bg.destroy()
                            lbl_quest.destroy()
                            ent_q.destroy()
                            ent_Bn.destroy()
                            ent_Sn.destroy()
                            ent_n.destroy()
                            find_geom_prog_lbl2.destroy()
                            find_geom_prog_lbl3.destroy()
                            find_geom_prog_lbl4.destroy()
                            find_geom_prog_lbl5.destroy()
                            btn_clear.destroy()
                            btn_arif_prog_next.destroy()
                            lbl_B1.destroy()
                            answer_B1.destroy()
                            comment.destroy()
                            btn_back.destroy()
                            geom_progr()
                        def clear():
                            ent_q.delete(0,END)
                            ent_Bn.delete(0,END)
                            ent_Sn.delete(0,END)
                            ent_n.delete(0,END)
                            comment.configure(text="")
                            answer_B1.configure(text="")
                        def find_B1_geom_prog():
                            q=ent_q.get()
                            Bn=ent_Bn.get()
                            Sn=ent_Sn.get()
                            n=ent_n.get()
                            list_check=[]
                            B1=""
                            error=0
                            answer_B1.configure(text="")
                            comment.configure(text="")
                            try:
                                if q!="":
                                    q=float(q)
                                    list_check.append("q")
                                    proba=1/q
                                if Bn!="":
                                    Bn=float(Bn)
                                    list_check.append("Bn")
                                if Sn!="":
                                    Sn=float(Sn)
                                    list_check.append("Sn")
                                if n!="":
                                    n=int(n)
                                    list_check.append("n")
                                    if n==0 or int(n)!=float(n):
                                        n_proba=1/0
                            except:
                                messagebox.showinfo("Ошибка","Введите числа\nДробнуя часть вводите через точку\nЗначение 'n' должно быть целым натуральным числом")
                            else:
                                if "q" in list_check:
                                    if q==1:
                                        if Bn!="":
                                            B1=Bn
                                        if "Sn" in list_check and "n" in list_check:
                                            if B1!="":
                                                if B1==Sn/n:
                                                    pass
                                                else:
                                                    error=1
                                            else: 
                                                B1=Sn/n
                                    if q!=1:
                                        if "Bn" in list_check and "n" in list_check:
                                            B1=Bn/(q**(n-1))
                                        if "Bn" in list_check and "Sn" in list_check:
                                            if B1!="":
                                                if B1==Bn*q-Sn*(q-1):
                                                    pass
                                                else:
                                                    error=1
                                            else:
                                                B1=Bn*q-Sn*(q-1)


                                        if "n" in list_check and "q" in list_check and "Sn" in list_check and n!=0:
                                            if B1!="":
                                                if B1==Sn*(q-1)/((q**n)-1):
                                                    pass
                                                else:
                                                    error=1
                                            else:
                                                B1=Sn*(q-1)/((q**n)-1)
                                if B1!="":
                                    if error==0:
                                        answer_B1.configure(text=round(B1,5))
                                    else:
                                        messagebox.showinfo("Ошибка","Неверно введены данные.\nТакой прогрессии не существует")
                                else:
                                    messagebox.showinfo("Ошибка","Недостаточно данных")

                    def Bn():
                        bg=Label(text="", bg="#f67300")
                        bg.place(width=300,height=460, x=80,y=90)
                        lbl_quest=Label(text="Введите значения",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                        lbl_quest.place(x=200, y=20)
                        ent_q=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_q.place(x=230,y=125)
                        ent_B1=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_B1.place(x=230,y=205)
                        ent_Sn=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_Sn.place(x=230,y=290)
                        ent_n=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_n.place(x=230,y=380)
                        find_geom_prog_lbl2=Label(text="q =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl2.place(x=150,y=115,width=70)
                        find_geom_prog_lbl3=Label(text="B1 =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl3.place(x=150,y=195,width=70)
                        find_geom_prog_lbl4=Label(text="Sn =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl4.place(x=150,y=280,width=70)
                        find_geom_prog_lbl5=Label(text="n =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl5.place(x=150,y=370,width=70)
                        btn_clear=Button(text="Очистить", command=lambda:clear(),font=("Calibri",15,"bold"),fg="#ffffff",bg="#ff0059")
                        btn_clear.place(x=230,y=480,height=40,width=90)
                        btn_arif_prog_next=Button(text="Найти",command=lambda:find_Bn_geom_prog(),font=("Calibri", 20, "bold"),bg="#eeff00")
                        btn_arif_prog_next.place(x=540,y=480)
                        lbl_Bn=Label(text="Bn =",font=("Calibri",50,"bold"),bg="#362b2b",fg="#f67300")
                        lbl_Bn.place(x=430,y=180)
                        answer_Bn=Label(text="",font=("Calibri",50,"bold"),bg="#362b2b",fg="#f67300")
                        answer_Bn.place(x=560,y=180)
                        comment=Label(text="",font=("Calibri",20,"bold"),bg="#362b2b",fg="#f67300")
                        comment.place(x=430,y=300,width=430)

                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            bg.destroy()
                            lbl_quest.destroy()
                            ent_q.destroy()
                            ent_B1.destroy()
                            ent_Sn.destroy()
                            ent_n.destroy()
                            find_geom_prog_lbl2.destroy()
                            find_geom_prog_lbl3.destroy()
                            find_geom_prog_lbl4.destroy()
                            find_geom_prog_lbl5.destroy()
                            btn_clear.destroy()
                            btn_arif_prog_next.destroy()
                            lbl_Bn.destroy()
                            answer_Bn.destroy()
                            comment.destroy()
                            btn_back.destroy()
                            geom_progr()
                        def clear():
                            ent_q.delete(0,END)
                            ent_B1.delete(0,END)
                            ent_Sn.delete(0,END)
                            ent_n.delete(0,END)
                            comment.configure(text="")
                            answer_Bn.configure(text="")
                        def find_Bn_geom_prog():
                            q=ent_q.get()
                            B1=ent_B1.get()
                            Sn=ent_Sn.get()
                            n=ent_n.get()
                            list_check=[]
                            Bn=""
                            error=0
                            answer_Bn.configure(text="")
                            comment.configure(text="")
                            try:
                                if q!="":
                                    q=float(q)
                                    list_check.append("q")
                                    proba=1/q
                                if B1!="":
                                    B1=float(B1)
                                    list_check.append("B1")
                                if Sn!="":
                                    Sn=float(Sn)
                                    list_check.append("Sn")
                                if n!="":
                                    n=int(n)
                                    list_check.append("n")
                                    if n==0 or int(n)!=float(n):
                                        n_proba=1/0
                                
                                
                            except:
                                messagebox.showinfo("Ошибка","Введите числа\nДробнуя часть вводите через точку\nЗначение 'n' должно быть целым натуральным числом\nА коэфицент 'q' не равен нулю")
                            else:
                                if "B1" in list_check and "q" in list_check and "n" in list_check:
                                    Bn=B1*(q**(n-1))
                                if q==1 and "B1" in list_check:
                                    if Bn!="":
                                        if Bn==B1:
                                            pass
                                        else:
                                            error=1
                                    else:
                                        Bn=B1

                                if q==1 and "Sn" in list_check and "n" in list_check:
                                    if Bn!="":
                                        if Bn==Sn/n:
                                            pass
                                        else:
                                            error=1
                                    else:
                                        Bn=Sn/n

                                if "B1" in list_check and "q" in list_check and "Sn" in list_check:
                                    if Bn!="":
                                        if Bn==((q-1)*Sn+B1)/q:
                                            pass
                                        else:
                                            error=1
                                    else:
                                        Bn=((q-1)*Sn+B1)/q


                                if "B1" in list_check and "q" in list_check and "Sn" in list_check:
                                    if Bn!="":
                                        if Bn==((q-1)*Sn+B1)/q:
                                            pass
                                        else:
                                            error=1
                                    else:
                                        Bn=((q-1)*Sn+B1)/q

                                if error == 0:
                                    if Bn!="":
                                        answer_Bn.configure(text=Bn)
                                    else:
                                        messagebox.showinfo("Ошибка","Недостаточно данных")
                                else:
                                    messagebox.showinfo("Ошибка","Неверно введены данные.\n Такой прогрессии не существует")

                    def n():
                        bg=Label(text="", bg="#f67300")
                        bg.place(width=300,height=460, x=80,y=90)
                        lbl_quest=Label(text="Введите значения",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                        lbl_quest.place(x=200, y=20)
                        ent_q=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_q.place(x=230,y=125)
                        ent_B1=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_B1.place(x=230,y=205)
                        ent_Sn=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_Sn.place(x=230,y=290)
                        ent_Bn=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                        ent_Bn.place(x=230,y=380)
                        find_geom_prog_lbl2=Label(text="q =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl2.place(x=150,y=115,width=70)
                        find_geom_prog_lbl3=Label(text="B1 =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl3.place(x=150,y=195,width=70)
                        find_geom_prog_lbl4=Label(text="Sn =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl4.place(x=150,y=280,width=70)
                        find_geom_prog_lbl5=Label(text="Bn =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                        find_geom_prog_lbl5.place(x=150,y=370,width=70)
                        btn_clear=Button(text="Очистить", command=lambda:clear(),font=("Calibri",15,"bold"),fg="#ffffff",bg="#ff0059")
                        btn_clear.place(x=230,y=480,height=40,width=90)
                        btn_arif_prog_next=Button(text="Найти",command=lambda:find_n_geom_prog(),font=("Calibri", 20, "bold"),bg="#eeff00")
                        btn_arif_prog_next.place(x=540,y=480)
                        lbl_n=Label(text="n =",font=("Calibri",50,"bold"),bg="#362b2b",fg="#f67300")
                        lbl_n.place(x=430,y=180)
                        answer_n=Label(text="",font=("Calibri",50,"bold"),bg="#362b2b",fg="#f67300")
                        answer_n.place(x=560,y=180)
                        comment=Label(text="",font=("Calibri",20,"bold"),bg="#362b2b",fg="#f67300")
                        comment.place(x=430,y=300,width=430)

                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            bg.destroy()
                            lbl_quest.destroy()
                            ent_q.destroy()
                            ent_B1.destroy()
                            ent_Sn.destroy()
                            ent_Bn.destroy()
                            find_geom_prog_lbl2.destroy()
                            find_geom_prog_lbl3.destroy()
                            find_geom_prog_lbl4.destroy()
                            find_geom_prog_lbl5.destroy()
                            btn_clear.destroy()
                            btn_arif_prog_next.destroy()
                            lbl_n.destroy()
                            answer_n.destroy()
                            comment.destroy()
                            btn_back.destroy()
                            geom_progr()


                        def clear():
                            ent_q.delete(0,END)
                            ent_B1.delete(0,END)
                            ent_Sn.delete(0,END)
                            ent_Bn.delete(0,END)
                            comment.configure(text="")
                            answer_n.configure(text="")
                        def find_n_geom_prog():
                            q=ent_q.get()
                            B1=ent_B1.get()
                            Sn=ent_Sn.get()
                            Bn=ent_Bn.get()
                            list_check=[]
                            n=""
                            error=0
                            answer_n.configure(text="")
                            comment.configure(text="")
                            try:
                                if q!="":
                                    q=float(q)
                                    list_check.append("q")
                                    if q==0:
                                        x=1/0
                                if B1!="":
                                    B1=float(B1)
                                    list_check.append("B1")
                                if Sn!="":
                                    Sn=float(Sn)
                                    list_check.append("Sn")
                                if Bn!="":
                                    Bn=int(Bn)
                                    list_check.append("Bn")
                            except:
                                messagebox.showinfo("Ошибка","Введите числа\nДробнуя часть вводите через точку\nЗначение 'n' должно быть целым натуральным числом\nА коэфицент 'q' не равен нулю")
                            else:
                                if "q" in list_check and abs(q)>1:
                                    if "B1" in list_check and "Bn" in list_check:
                                        n=2
                                        while abs(Bn/B1)>abs((q**n-1)):
                                            n+=1
                                        if (q**(n-1))==Bn/B1:
                                            pass
                                        else:
                                            error=1
                                    if "B1" in list_check and "Sn" in list_check and error==0:
                                        n_proba=n
                                        n=2
                                        while abs(1-(Sn-Sn*q)/B1)>abs(q**n):
                                            n+=1
                                        if (q**n)==1-(Sn-Sn*q)/B1:
                                            pass
                                        else:
                                            error=1
                                        if n_proba==n:
                                            pass
                                        else:
                                            error=1

                                if "q" in list_check and q==1 and error==0:
                                    if "B1" in list_check and "Bn" in list_check:
                                        if B1==Bn:
                                            pass
                                        else:
                                            error=1

                                    if "B1" in list_check and "Sn" in list_check and error==0:
                                        n=Sn/B1
                                    if "Bn" in list_check and "Sn" in list_check and error==0:
                                        n=Sn/Bn

                                if "q" in list_check and abs(q)<1 and error==0:
                                    if "B1" in list_check and "Bn" in list_check:
                                        n=2
                                        while abs(Bn/B1)<abs((q**(n-1))):
                                            n+=1
                                        if (q**(n-1))==Bn/B1:
                                            pass
                                        else:
                                            error=1
                                    if "B1" in list_check and "Sn" in list_check and error==0:
                                        n_proba=n
                                        n=2
                                        while abs(1-(Sn-Sn*q)/B1)<abs(q**n):
                                            n+=1
                                        if (q**n)==1-(Sn-Sn*q)/B1:
                                            pass
                                        else:
                                            error=1
                                        if n_proba==n:
                                            pass
                                        else:
                                            error=1

                                if "B1" in list_check and "Bn" in list_check and "Sn" in list_check and error==0:
                                    if B1==Bn:
                                        if n!="":
                                            if n==Sn/B1:
                                                pass
                                            else:
                                                error=1
                                        else:
                                            n=Sn/B1                             
                                    else:
                                        pass
                                if error==0:
                                    if n!="":
                                        if int(n) == float(n):
                                            answer_n.configure(text=n)
                                        else:
                                            messagebox.showinfo("Ошибка","Неверно введены данные.\n Такой прогрессии не существует")
                                    else:
                                        messagebox.showinfo("Ошибка","Недостаточно данных")
                                else:
                                    messagebox.showinfo("Ошибка","Неверно введены данные.\n Такой прогрессии не существует")

                def arif_progr():
                    bg=Label(text="", bg="#f67300")
                    bg.place(width=300,height=490, x=80,y=90)
                    find_arif_prog_lbl1=Label(text="Введите известные вам значения",font=("Calibri",27,"bold"),bg="#362b2b", fg="#f67300")
                    find_arif_prog_lbl1.place(x=260,y=10)
                    answer_lbl_num_bg=Label(bg="#f67300",fg="#EC0033",font=("Calibri",36,"bold"),text="")
                    answer_lbl_num_bg.place(x=530,y=110,width=330, height=300)
                    btn_arif_prog_next=Button(text="Найти",command=lambda:Type_Check(),font=("Calibri", 20, "bold"),bg="#eeff00")
                    btn_arif_prog_next.place(x=540,y=480)
                    find_arif_prog_lbl2=Label(text="B1 =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                    find_arif_prog_lbl2.place(x=150,y=105,width=70)
                    find_arif_prog_lbl3=Label(text="Bn =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                    find_arif_prog_lbl3.place(x=150,y=180,width=70)
                    find_arif_prog_lbl4=Label(text="Sn =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                    find_arif_prog_lbl4.place(x=150,y=270,width=70)
                    find_arif_prog_lbl5=Label(text="D =",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                    find_arif_prog_lbl5.place(x=150,y=360,width=70)
                    find_arif_prog_lbl6=Label(text=" n = ",font=("Calibri",30,"bold"),bg="#f67300",fg="#EC0033")
                    find_arif_prog_lbl6.place(x=150,y=440,width=70)
                    btn_clear=Button(text="Очистить", command=lambda:clear(),font=("Calibri",15,"bold"),fg="#ffffff",bg="#ff0059")
                    btn_clear.place(x=230,y=510,height=40,width=90)
                    arif_progr_answer_1=Label(text="",font=("Calibri",30,"bold"),bg="#f67300")
                    arif_progr_answer_1.place(x=540,y=160)
                    arif_progr_answer_1_znach=Label(text="",font=("Calibri",30,"bold"),bg="#f67300")
                    arif_progr_answer_1_znach.place(x=620,y=160)
                    arif_progr_answer_2=Label(text="",font=("Calibri",30,"bold"),bg="#f67300")
                    arif_progr_answer_2.place(x=540,y=290)
                    arif_progr_answer_2_znach=Label(text="",font=("Calibri",30,"bold"),bg="#f67300")
                    arif_progr_answer_2_znach.place(x=620,y=290)
                    ent_B1=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                    ent_B1.place(x=230,y=115)
                    ent_Bn=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                    ent_Bn.place(x=230,y=190)
                    ent_Sn=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                    ent_Sn.place(x=230,y=280)
                    ent_D=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                    ent_D.place(x=230,y=370)
                    ent_n=Entry(font=("Calibri",20,"bold"),bg="#fff",width=8)
                    ent_n.place(x=230,y=450)

                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)
                    def back():
                        bg.destroy()
                        find_arif_prog_lbl1.destroy()
                        answer_lbl_num_bg.destroy()
                        btn_arif_prog_next.destroy()
                        find_arif_prog_lbl2.destroy()
                        find_arif_prog_lbl3.destroy()
                        find_arif_prog_lbl4.destroy()
                        find_arif_prog_lbl5.destroy()
                        find_arif_prog_lbl6.destroy()
                        btn_clear.destroy()
                        arif_progr_answer_1.destroy()
                        arif_progr_answer_1_znach.destroy()
                        arif_progr_answer_2.destroy()
                        arif_progr_answer_2_znach.destroy()
                        ent_B1.destroy()
                        ent_Bn.destroy()
                        ent_Sn.destroy()
                        ent_D.destroy()
                        ent_n.destroy()
                        btn_back.destroy()
                        progress()

                    def clear():
                        ent_B1.delete(0,END)
                        ent_Bn.delete(0,END)
                        ent_Sn.delete(0,END)
                        ent_D.delete(0,END)
                        ent_n.delete(0,END)

                    def Type_Check():
                        B1=ent_B1.get()
                        Bn=ent_Bn.get()
                        Sn=ent_Sn.get()
                        D=ent_D.get()
                        n=ent_n.get()
                        list_check=[]
                        x=0
                        try:
                            if B1!="":
                                B1=float(B1)
                                list_check.append("B1")
                                x+=1
                            if Bn!="":
                                Bn=float(Bn)
                                list_check.append("Bn")
                                x+=1
                            if Sn!="":
                                Sn=float(Sn)
                                list_check.append("Sn")
                                x+=1
                            if D!="":
                                D=float(D)
                                list_check.append("D")
                                x+=1
                            if n!="":
                                n=int(n)
                                list_check.append("n")
                                if n==0 or int(n)!=float(n):
                                        n_proba=1/0


                        except ValueError:
                            messagebox.showinfo("Ошибка", "Введите цифровые значения.\nЗначение n - обязательно и должно быть равно целому числу, которое больше единицы")
                        else:
                            if n!="":
                                if n>1:
                                    if x>=2:
                                        arif_prog_find(list_check,B1,Bn,Sn,D,n)
                                    else:
                                        messagebox.showinfo("Ошибка", "Недостаточно данных")
                                        
                                else:
                                    messagebox.showinfo("Ошибка", "Значение n - обязательно для ввода и должно быть равно целому числу, которое больше единицы")
                            else:
                                messagebox.showinfo("Ошибка", "Введите цифровые значения.\nЗначение n - обязательно и должно быть равно целому числу, которое больше единицы")



                    def arif_prog_find(list_name,B1,Bn,Sn,D,n):

                        quest=0
                        list_name_quest=[]
                        list_name_znach=[]
                        Bn_find1=""
                        Bn_find2=""
                        Bn_find3=""
                        Bn_find=""
                        B1_find1=""
                        B1_find2=""
                        B1_find3=""
                        Bn_find=""
                        Sn_find1=""
                        Sn_find2=""
                        Sn_find3=""
                        Sn_find=""
                        D_find1=""
                        D_find2=""
                        D_find3=""
                        D_find=""



                        if "B1" in list_name:
                            pass
                        else:
                            list_name_quest.append("B1")
                            quest+=1
                            if "Bn" in list_name and "Sn" in list_name:
                                B1_find1=((2*Sn)/n-Bn)
                            if "Bn" in list_name and "D" in list_name:
                                B1_find2=(Bn-D*(n-1))
                            if "D" in list_name and "Sn" in list_name:
                                B1_find3=(Sn/n-D*(n-1)/2)
                            if B1_find1 != "":
                                if B1_find2 !="":
                                    if B1_find3 !="":
                                        if B1_find1 ==B1_find2 and B1_find2 == B1_find3:
                                            B1_find=round(B1_find1,2)  
                                        else:
                                            messagebox.showinfo("Ошибка","Неверно введены данные")
                                    else:
                                        if B1_find1 ==B1_find2:
                                            B1_find=round(B1_find1,2)
                                        else:
                                            messagebox.showinfo("Ошибка","Неверно введены данные")
                                elif B1_find3 !="":
                                    if B1_find1==B1_find3:
                                        B1_find=round(B1_find1,2)
                                    else:
                                        messagebox.showinfo("Ошибка","Неверно введены данные")
                                else:
                                    B1_find=round(B1_find1,2)
                            elif B1_find2 !="":
                                if B1_find3 !="":
                                    if B1_find2==B1_find3:
                                        B1_find=round(B1_find1,2)
                                    else: messagebox.showinfo("Ошибка","Неверно введены данные")
                                else: B1_find=round(B1_find2,2)
                            else:
                                B1_find=round(B1_find3,2)
                            if B1_find!="":
                                list_name_znach.append(B1_find)


                            

                        if "Bn" in list_name:
                            pass
                        else:
                            list_name_quest.append("Bn")
                            quest+=1
                            if "B1" in list_name and "Sn" in list_name:
                                Bn_find1=((2*Sn)/n-B1)
                            if "B1" in list_name and "D" in list_name:
                                Bn_find2=(B1+D*(n-1))
                            if "Sn" in list_name and "D" in list_name:
                                Bn_find3=(Sn/n + (D*(n-1))/2)

                            if Bn_find1 != "":
                                if Bn_find2 !="":
                                    if Bn_find3 !="":
                                        if Bn_find1 ==Bn_find2 and Bn_find2 == Bn_find3:
                                            Bn_find=round(Bn_find1,2)  
                                        else:
                                            messagebox.showinfo("Ошибка","Неверно введены данные")
                                    else:
                                        if Bn_find1 ==Bn_find2:
                                            Bn_find=round(Bn_find1,2)
                                        else:
                                            messagebox.showinfo("Ошибка","Неверно введены данные")
                                elif Bn_find3 !="":
                                    if Bn_find1==Bn_find3:
                                        Bn_find=round(Bn_find1,2)
                                    else:
                                        messagebox.showinfo("Ошибка","Неверно введены данные")
                                else:
                                    Bn_find=round(Bn_find1,2)
                            elif Bn_find2 !="":
                                if Bn_find3 !="":
                                    if Bn_find2==Bn_find3:
                                        Bn_find=round(Bn_find1,2)
                                    else: messagebox.showinfo("Ошибка","Неверно введены данные")
                                else: Bn_find=round(Bn_find2,2)
                            else:
                                Bn_find=round(Bn_find3,2)
                            if Bn_find!="":
                                list_name_znach.append(Bn_find)


                        if "Sn" in list_name:
                            pass
                        else:
                            list_name_quest.append("Sn")
                            quest+=1
                            if "B1" in list_name and "Bn" in list_name:
                                Sn_find1=(((Bn+B1)/2)*n)
                            if "B1" in list_name and "D" in list_name:
                                Sn_find2=((2*B1+D*(n-1))/2*n)
                            if "Bn" in list_name and "D" in list_name:
                                Sn_find3=((2*Bn-(D*(n-1)))/2*n)

                            if Sn_find1 != "":
                                if Sn_find2 !="":
                                    if Sn_find3 !="":
                                        if Sn_find1 ==Sn_find2 and Sn_find2 == Sn_find3:
                                            Sn_find=round(Sn_find1,2)  
                                        else:
                                            messagebox.showinfo("Ошибка","Неверно введены данные")
                                    else:
                                        if Sn_find1 ==Sn_find2:
                                            Sn_find=round(Sn_find1,2)
                                        else:
                                            messagebox.showinfo("Ошибка","Неверно введены данные")
                                elif Sn_find3 !="":
                                    if Sn_find1==Sn_find3:
                                        Sn_find=round(Sn_find1,2)
                                    else:
                                        messagebox.showinfo("Ошибка","Неверно введены данные")
                                else:
                                    Sn_find=round(Sn_find1,2)
                            elif Sn_find2 !="":
                                if Sn_find3 !="":
                                    if Sn_find2==Sn_find3:
                                        Sn_find=round(Sn_find1,2)
                                    else: messagebox.showinfo("Ошибка","Неверно введены данные")
                                else: Sn_find=round(Sn_find2,2)
                            else:
                                Sn_find=round(Sn_find3,2)
                            if Sn_find!="":
                                list_name_znach.append(Sn_find)



                        if "D" in list_name:
                            pass
                        else:
                            list_name_quest.append("D")
                            quest+=1
                            if "B1" in list_name and "Bn" in list_name:
                                D_find1=((Bn-B1)/(n-1))
                            if "B1" in list_name and "Sn" in list_name:
                                D_find2=((2*Sn)/(n*(n-1))-(2*B1)/(n-1))
                            if "Bn" in list_name and "Sn" in list_name:
                                D_find3=((Bn-((2*Sn)/n-Bn))/(n-1))
                            if D_find1 != "":
                                if D_find2 !="":
                                    if D_find3 !="":
                                        if D_find1 ==D_find2 and D_find2 == D_find3:
                                            D_find=round(D_find1,2)  
                                        else:
                                            messagebox.showinfo("Ошибка","Неверно введены данные")
                                    else:
                                        if D_find1 ==D_find2:
                                            D_find=round(D_find1,2)
                                        else:
                                            messagebox.showinfo("Ошибка","Неверно введены данные")
                                elif D_find3 !="":
                                    if D_find1==D_find3:
                                        D_find=round(D_find1,2)
                                    else:
                                        messagebox.showinfo("Ошибка","Неверно введены данные")
                                else:
                                    D_find=round(D_find1,2)
                            elif D_find2!="":
                                if D_find3!="":
                                    if D_find2==D_find3:
                                        D_find=round(D_find1,2)
                                    else:
                                        messagebox.showinfo("Ошибка","Неверно введены данные")
                                else:
                                    D_find=round(D_find2,2)
                            else:
                                D_find=round(D_find3,2)
                            if D_find!="":
                                list_name_znach.append(D_find)

                        if len(list_name_quest)==0:
                            messagebox.showinfo("Ошибка","Нам и так всё известно")
                        elif len(list_name_quest)==1:
                            arif_progr_answer_1.configure(text=(list_name_quest[0]+" ="))
                            arif_progr_answer_1_znach.configure(text=list_name_znach[0])
                            arif_progr_answer_2.configure(text="")
                            arif_progr_answer_2_znach.configure(text="")
                        elif len(list_name_quest)==2:
                            arif_progr_answer_1.configure(text=(list_name_quest[0]+" ="))
                            arif_progr_answer_1_znach.configure(text=list_name_znach[0])
                            arif_progr_answer_2.configure(text=(list_name_quest[1]+" ="))
                            arif_progr_answer_2_znach.configure(text=list_name_znach[1])

        def geom():
            btn.destroy()
            btn2.destroy()
            btn3.destroy()
            triug=Button(text="Треугольник",command=lambda:next("triugolnik"), font=("Calibri", 27, "bold"),bg="#f67300",fg="#362b2b") 
            krugl=Button(text="Круг",command= lambda:next("krug"), font=("Calibri", 27, "bold"),bg="#362b2b",fg="#f67300")
            ugl_4=Button(text="Четырехугольник",command=lambda:next("ugolnik_4"), font=("Calibri", 27, "bold"),bg="#f67300",fg="#362b2b") 
            triug.place(x=0,y=0,height=600, width=303)
            krugl.place(height=600, width=303,y=0, x=300)
            ugl_4.place(height=600, width=303, x=600, y=0)
            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
            btn_back.place(x=5,y=5)
            def back():
                btn_back.destroy()
                triug.destroy()
                krugl.destroy()
                ugl_4.destroy()
                build()

            def next(x):
                triug.destroy()
                krugl.destroy()
                ugl_4.destroy()
                btn_back.destroy()
                if x=="triugolnik":
                    triugolnik()
                elif x=="krug":
                    krug()
                elif x=="ugolnik_4":
                    ugolnik_4()
            def triugolnik():
                triug_head=Label(text="Что нужно найти",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                triug_head.place(x=290,y=10)
                btn_triug_1=Button(text="Площадь",command=lambda:next("triug_S"),bg="#f67300",fg="#362b2b",font=("Calibri",27,"bold"))
                btn_triug_2=Button(text="Периметр",command=lambda:next("triug_P"),bg="#f67300",fg="#362b2b",font=("Calibri",27,"bold"))
                btn_triug_3=Button(text="Нахождение\nстороны",command=lambda:next("triug_AB"),bg="#f67300",fg="#362b2b",font=("Calibri",27,"bold"))
                btn_triug_4=Button(text="Нахождение\nугла",command=lambda:next("triug_a"),bg="#f67300",fg="#362b2b",font=("Calibri",27,"bold"))
                btn_triug_1.place(x=90,y=110,width=310,height=190)
                btn_triug_2.place(x=490,y=110,width=310,height=190)
                btn_triug_3.place(x=90,y=350,width=310,height=190)
                btn_triug_4.place(x=490,y=350,width=310,height=190)
                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def next(x):
                    triug_head.destroy()
                    btn_triug_1.destroy()
                    btn_triug_2.destroy()
                    btn_triug_3.destroy()
                    btn_triug_4.destroy()
                    btn_back.destroy()
                    if x=="triug_S":
                        triug_S()
                    elif x=="triug_P":
                        triug_P()
                    elif x=="triug_AB":
                        triug_AB()
                    elif x=="triug_a":
                        triug_a()


                def back():
                    btn_back.destroy()
                    triug_head.destroy()
                    btn_triug_1.destroy()
                    btn_triug_2.destroy()
                    btn_triug_3.destroy()
                    btn_triug_4.destroy()
                    geom()

                def triug_S():
                    S_head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    S_head.place(x=290,y=10)
                    btn_S_1=Button(text="Три стороны",command=lambda:next("S_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_S_2=Button(text="Две стороны угол\nи угол между ними",command=lambda:next("S_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_S_3=Button(text="Высота\nи сторона, к которой\nпроведена высота",command=lambda:next("S_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_S_4=Button(text="Два угла и сторона\nмежду ними",command=lambda:next("S_4"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_S_1.place(x=90,y=110,width=310,height=190)
                    btn_S_2.place(x=490,y=110,width=310,height=190)
                    btn_S_3.place(x=90,y=350,width=310,height=190)
                    btn_S_4.place(x=490,y=350,width=310,height=190)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)
                    def next(x):
                        S_head.destroy()
                        btn_S_1.destroy()
                        btn_S_2.destroy()
                        btn_S_3.destroy()
                        btn_S_4.destroy()
                        btn_back.destroy()
                        if x=="S_1":
                            S_1()
                        elif x=="S_2":
                            S_2()
                        elif x=="S_3":
                            S_3()
                        elif x=="S_4":
                            S_4()

                    def back():
                        btn_back.destroy()
                        S_head.destroy()
                        btn_S_1.destroy()
                        btn_S_2.destroy()
                        btn_S_3.destroy()
                        btn_S_4.destroy()
                        triugolnik()
                    def S_1():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text=" Сторона 1 ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text=" Сторона 2 ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text=" Сторона 3 ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_S_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_S())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",24,"bold"),bg="#463b3b",fg="#f87808")
                        lbl_txt_1.place(x=427,y=110)
                        bg.place(x=415,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_S_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_S_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_S()



                        def find_S():
                            a=ent_1.get()
                            b=ent_2.get()
                            c=ent_3.get()
                            txt_1="p(полупериметр) = (a+b+c)/2\n\nS = \u221a(p*(p-a)*(p-b)*(p-c))\n\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                a=float(a)
                                b=float(b)
                                c=float(c)
                                if a>1000 or b>1000 or c>1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if a=="" or b=="" or c=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if a<=0 or b<=0 or c<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                                if a+b<=c or b+c<=a or a+c<=b:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Вы ввели некоректные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:
                                p=(a+b+c)/2
                                S1=(p*(p-a)*(p-b)*(p-c))
                                S=round(pow(S1,0.5),3)
                                txt_2=("S =  \u221a("+str(S1)+") = "+ str(S))
                                txt=txt_1+txt_2
                                lbl_txt_1.configure(text=txt)
                                





                    def S_2():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text=" Сторона 1 ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text=" Сторона 2 ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text="      Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_S_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_S())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",24,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=110)
                        bg.place(x=415,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_S_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_S_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_S()
                        def find_S():
                            a=ent_1.get()
                            b=ent_2.get()
                            ugl=ent_3.get()
                            txt_1="   S= a*b*sin(α)/2\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                a=float(a)
                                b=float(b)
                                ugl=float(ugl)
                                if a>1000 or b>1000 or ugl>180:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if a=="" or b=="" or ugl=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if a<=0 or b<=0 or ugl<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:
                                txt_2=("   S= "+str(a*b/2)+" * sin ("+str(ugl)+")\n\n")
                                ugl=math.radians(ugl)
                                S=a*b*(math.sin(ugl))/2
                                S=round(S,5)
                                if S<0:
                                    S=S*(-1)
                                txt_3=("   S= "+ str(S))
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)






                    def S_3():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="  Сторона   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="    Высота   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_S_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_S())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",28,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=110)
                        bg.place(x=415,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=140)
                        ent_1.place(x=50,y=195,width=150,height=45)
                        lbl_2.place(x=40,y=340)
                        ent_2.place(x=50,y=405,width=150,height=45)
                        btn_S_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_S_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            lbl_txt_1.destroy()
                            triug_S()
                        def find_S():
                            a=ent_1.get()
                            h=ent_2.get()
                            txt_1="\n\n   S = a * h / 2  \n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                a=float(a)
                                h=float(h)
                                if a>1000 or h>1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if a=="" or h=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if a<=0 or h<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:

                                S=a*h/2
                                txt_2=("   S = "+str(a)+" * "+str(h)+" / 2 = "+str(S))
                                txt=(txt_1+txt_2)
                                lbl_txt_1.configure(text=txt)


                    def S_4():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text=" Сторона а  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="     Угол γ    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text="     Угол β    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_S_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_S())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        bg_1=Label(bg="#f67300")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_S_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_S_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_S()
                        def find_S():
                            a=ent_1.get()
                            ugl_2=ent_2.get()
                            ugl_1=ent_3.get()
                            bg_1.place(x=487,y=247,height=4,width=260)
                            txt_1="  S =  а²*sin(γ)*sin(β)\n             2*sin(γ+β)\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                a=float(a)
                                ugl_1=float(ugl_1)
                                ugl_2=float(ugl_2)
                                if a>1000 or ugl_1+ugl_2>=180 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if a=="" or ugl_1=="" or ugl_2=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if a<=0 or ugl_1<=0 or ugl_2<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:
                                if int(ugl_1)==float(ugl_1):
                                    ugl_1=int(ugl_1)
                                if int(ugl_2)==float(ugl_2):
                                    ugl_2=int(ugl_2)
                                if int(a)==float(a):
                                    a=int(a)
                                ugl_1=math.radians(ugl_1)
                                ugl_2=math.radians(ugl_2)
                                S=(a*a*math.sin(ugl_1)*math.sin(ugl_2)/(2*math.sin(ugl_1+ugl_2)))
                                S=round(S,5)
                                txt=txt_1+"   S = "+str(S)
                                lbl_txt_1.configure(text=txt)


                def triug_P():
                    P_head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    P_head.place(x=290,y=10)
                    btn_P_1=Button(text="Три стороны",command=lambda:next("P_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_P_2=Button(text="Две стороны и угол\nмежду ними",command=lambda:next("P_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_P_3=Button(text="Площадь треугольника и радиус\nвписанной окружности",command=lambda:next("P_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_P_1.place(x=90,y=110,width=310,height=190)
                    btn_P_2.place(x=490,y=110,width=310,height=190)
                    btn_P_3.place(x=130,y=350,width=640,height=190)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)
                    def back():
                        P_head.destroy()
                        btn_P_1.destroy()
                        btn_P_2.destroy()
                        btn_P_3.destroy()
                        btn_back.destroy()
                        triugolnik()
                    def next(x):
                        P_head.destroy()
                        btn_P_1.destroy()
                        btn_P_2.destroy()
                        btn_P_3.destroy()
                        btn_back.destroy()
                        if x=="P_1":
                            P_1()
                        elif x=="P_2":
                            P_2()
                        elif x=="P_3":
                            P_3()


                    def P_1():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text=" Сторона a ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text=" Сторона b ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text=" Сторона c ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_P())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=110)
                        bg.place(x=415,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_P()
                        def find_P():
                            a=ent_1.get()
                            b=ent_2.get()
                            c=ent_3.get()
                            txt_1="\n\n   P = a + b + c\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                a=float(a)
                                b=float(b)
                                c=float(c)
                                if a>1000 or b>1000 or c>1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if a=="" or b=="" or c=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if a<=0 or b<=0 or c<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                                if a+b<=c or b+c<=a or a+c<=b:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Вы ввели некоректные значения")
                                    error=1
                                    err=2/0

                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:
                                if int(a)==float(a):
                                    a=int(a)
                                if int(b)==float(b):
                                    b=int(b)
                                if int(c)==float(c):
                                    c=int(c)
                                txt_2=("   P = "+str(a)+" + "+str(b)+" + "+str(c)+"\n\n")
                                txt_3=("   P = "+str(a+b+c))
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)







                    def P_2():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="     Угол ⍺    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text=" Сторона B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_P())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",24,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=110)
                        bg.place(x=415,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_P()

                        def find_P():
                            ugl_1=ent_1.get()
                            A=ent_2.get()
                            B=ent_3.get()
                            txt_1="\n\n\n   P = \u221a(A²+B²-2AB*cos(⍺))+A+B\n\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                ugl_1=float(ugl_1)
                                A=float(A)
                                B=float(B)
                                if A>1000 or B>1000 or ugl_1>=180:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if A=="" or B=="" or ugl_1=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if A<=0 or B<=0 or ugl_1<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:
                                if int(A)==float(A):
                                    A=int(A)
                                if int(B)==float(B):
                                    B=int(B)
                                if int(ugl_1)==float(ugl_1):
                                    ugl_1=int(ugl_1)
                                ugl_1=math.radians(ugl_1)
                                P=(pow(A*A+B*B-2*A*B*math.cos(ugl_1),0.5)+B+A)
                                P=round(P,4)
                                txt=txt_1+"  P = "+str(P)
                                lbl_txt_1.configure(text=txt)


                    def P_3():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="  Площадь S   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="   Радиус r    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_P())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",28,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=110)
                        bg.place(x=415,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=140)
                        ent_1.place(x=50,y=195,width=150,height=45)
                        lbl_2.place(x=40,y=340)
                        ent_2.place(x=50,y=405,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            lbl_txt_1.destroy()
                            triug_P()

                        def find_P():
                            S=ent_1.get()
                            r=ent_2.get()
                            txt_1="\n\n   P = 2 * S / r  \n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                S=float(S)
                                r=float(r)
                                if S>1000 or r>1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if S=="" or r=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if S<=0 or r<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:
                                if int(S)==float(S):
                                    S=int(S)
                                if int(r)==float(r):
                                    r=int(r)
                                txt_2="   P = 2 * "+str(S)+" / "+str(r)+"\n\n"
                                P=(2*S/r)
                                P=round(P,4)
                                txt_3="   P = "+str(P)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)


                def triug_AB():
                    P_head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    P_head.place(x=290,y=10)
                    btn_P_1=Button(text="Периметр и\nдве стороны",command=lambda:next("AB_1"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                    btn_P_2=Button(text="Противолежащий\nугол и две\nстороны",command=lambda:next("AB_2"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                    btn_P_3=Button(text="Противолежащий угол,\n сторона и\nпротиволежащий угол\nк этой стороне",command=lambda:next("AB_3"),fg="#f67300",bg="#362b2b",font=("Calibri",18,"bold"))
                    btn_P_4=Button(text="Сторона и два\n угла\nприлежащие к\nискомой стороне",command=lambda:next("AB_4"),fg="#f67300",bg="#362b2b",font=("Calibri",19,"bold"))
                    btn_P_5=Button(text="Два прилежащих\n угла и площадь",command=lambda:next("AB_5"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                    btn_P_6=Button(text="Площадь и высота,\n проведенная к\nискомой стороне",command=lambda:next("AB_6"),fg="#f67300",bg="#362b2b",font=("Calibri",19,"bold"))
                    btn_P_1.place(x=50,y=110,width=240,height=170)
                    btn_P_2.place(x=330,y=110,width=240,height=170)
                    btn_P_3.place(x=610,y=110,width=250,height=170)
                    btn_P_4.place(x=50,y=350,width=240,height=170)
                    btn_P_5.place(x=330,y=350,width=240,height=170)
                    btn_P_6.place(x=610,y=350,width=250,height=170)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)
                    def back():
                        P_head.destroy()
                        btn_P_1.destroy()
                        btn_P_2.destroy()
                        btn_P_3.destroy()
                        btn_P_4.destroy()
                        btn_P_5.destroy()
                        btn_P_6.destroy()
                        btn_back.destroy()
                        triugolnik()
                    def next(x):
                        P_head.destroy()
                        btn_P_1.destroy()
                        btn_P_2.destroy()
                        btn_P_3.destroy()
                        btn_P_4.destroy()
                        btn_P_5.destroy()
                        btn_P_6.destroy()
                        btn_back.destroy()
                        if x=="AB_1":
                            AB_1()
                        elif x=="AB_2":
                            AB_2()
                        elif x=="AB_3":
                            AB_3()
                        elif x=="AB_4":
                            AB_4()
                        elif x=="AB_5":
                            AB_5()
                        elif x=="AB_6":
                            AB_6()

                    def AB_1():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text=" Периметр P  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="   Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text="   Сторона C  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_AB())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_AB()
                        def find_AB():
                            P=ent_1.get()
                            B=ent_2.get()
                            C=ent_3.get()
                            txt_1="  A = P - (B + C)  \n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                P=float(P)
                                B=float(B)
                                C=float(C)
                                if P>1000 or B>=1000 or C>=1000 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if P=="" or B=="" or C=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if P<=0 or B<=0 or C<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                                if B+C>=P:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите неверные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(P)==float(P):
                                    P=int(P)
                                if int(B)==float(B):
                                    B=int(B)
                                if int(C)==float(C):
                                    C=int(C)
                                txt_2="  A = "+str(P)+" - ("+str(B)+" + "+str(C)+")\n\n"
                                A=P-B-C
                                txt_3="  A = "+str(A)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)


                    def AB_2():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="      Угол α      ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="   Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text="   Сторона C  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_AB())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_AB()
                        def find_AB():
                            ugl=ent_1.get()
                            B=ent_2.get()
                            C=ent_3.get()
                            txt_1="  A = √(B²+C²-2BC*cos(α))  \n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                ugl=float(ugl)
                                B=float(B)
                                C=float(C)
                                if C>1000 or B>=1000 or ugl>=180 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if ugl=="" or B=="" or C=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if ugl<=0 or B<=0 or C<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(ugl)==float(ugl):
                                    ugl=int(ugl)
                                if int(B)==float(B):
                                    B=int(B)
                                if int(C)==float(C):
                                    C=int(C)
                                ugl=math.radians(ugl)
                                A=pow(B*B+C*C-2*B*C*math.cos(ugl),0.5)
                                A=round(A,4)
                                txt_2="  A = "+str(A)
                                txt=txt_1+txt_2
                                lbl_txt_1.configure(text=txt)


                    def AB_3():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="      Угол α      ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="      Угол β      ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text="   Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_AB())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_AB()
                        def find_AB():
                            ugl_1=ent_1.get()
                            ugl_2=ent_2.get()
                            B=ent_3.get()
                            txt_1="  A = (B*sin(α))/ sin(β)  \n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                ugl_1=float(ugl_1)
                                ugl_2=float(ugl_2)
                                B=float(B)
                                if B>1000 or ugl_1+ugl_2>=180 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if ugl_1=="" or B=="" or ugl_2=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if ugl_1<=0 or B<=0 or ugl_2<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(ugl_1)==float(ugl_1):
                                    ugl_1=int(ugl_1)
                                if int(B)==float(B):
                                    B=int(B)
                                if int(ugl_2)==float(ugl_2):
                                    ugl_2=int(ugl_2)
                                txt_2="  A = ("+str(B)+" * sin("+str(ugl_1)+")) / sin("+str(ugl_2)+")\n\n"
                                ugl_1=math.radians(ugl_1)
                                ugl_2=math.radians(ugl_2)
                                A=(B*math.sin(ugl_1)/math.sin(ugl_2))
                                A=round(A,3)
                                txt_3="  A = "+str(A)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)


                    def AB_4():
                        P_head.destroy()
                        btn_P_1.destroy()
                        btn_P_2.destroy()
                        btn_P_3.destroy()
                        btn_P_4.destroy()
                        btn_P_5.destroy()
                        btn_P_6.destroy()
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="      Угол β      ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="      Угол γ      ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text="   Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_AB())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_AB()
                        def find_AB():
                            ugl_1=ent_1.get()
                            ugl_2=ent_2.get()
                            B=ent_3.get()
                            txt_1="  A = B*sin(β+γ)/sin(β)  \n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                ugl_1=float(ugl_1)
                                ugl_2=float(ugl_2)
                                B=float(B)
                                if B>1000 or ugl_1+ugl_2>=180 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if ugl_1=="" or B=="" or ugl_2=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if ugl_1<=0 or B<=0 or ugl_2<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(ugl_1)==float(ugl_1):
                                    ugl_1=int(ugl_1)
                                if int(B)==float(B):
                                    B=int(B)
                                if int(ugl_2)==float(ugl_2):
                                    ugl_2=int(ugl_2)
                                ugl_1=math.radians(ugl_1)
                                ugl_2=math.radians(ugl_2)
                                A=(B*math.sin(ugl_1+ugl_2)/math.sin(ugl_1))
                                A=round(A,3)
                                txt_2="  A = "+str(A)
                                txt=txt_1+txt_2
                                lbl_txt_1.configure(text=txt)



                    def AB_5():
                        P_head.destroy()
                        btn_P_1.destroy()
                        btn_P_2.destroy()
                        btn_P_3.destroy()
                        btn_P_4.destroy()
                        btn_P_5.destroy()
                        btn_P_6.destroy()
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="      Угол β      ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="      Угол γ      ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text="     Площадь S    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_AB())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg_1=Label(bg="#f67300")
                        koren=Label(text="√",font=("Calibri",77),bg="#463b3b",fg="#f87808")
                        A_ravno=Label(text="A =",font=("Calibri",35,"bold"),bg="#463b3b",fg="#f87808")
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            A_ravno.destroy()
                            bg_1.destroy()
                            koren.destroy()
                            triug_AB()
                        def find_AB():
                            ugl_1=ent_1.get()
                            ugl_2=ent_2.get()
                            S=ent_3.get()
                            koren.place(x=515,y=180)
                            A_ravno.place(x=440,y=215)
                            bg_1.place(x=587,y=247,height=4,width=205)
                            txt_1="                     2*S*sin(γ+β)\n                     sin(β)*sin(γ)  \n\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                ugl_1=float(ugl_1)
                                ugl_2=float(ugl_2)
                                S=float(S)
                                if S>1000 or ugl_1+ugl_2>=180 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if ugl_1=="" or S=="" or ugl_2=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if ugl_1<=0 or S<=0 or ugl_2<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(ugl_1)==float(ugl_1):
                                    ugl_1=int(ugl_1)
                                if int(S)==float(S):
                                    S=int(S)
                                if int(ugl_2)==float(ugl_2):
                                    ugl_2=int(ugl_2)
                                ugl_1=math.radians(ugl_1)
                                ugl_2=math.radians(ugl_2)
                                A=(2*S*math.sin(ugl_1+ugl_2)/(math.sin(ugl_1)*math.sin(ugl_2)))
                                A=pow(A,0.5)
                                A=round(A,3)
                                txt_2="  A = "+str(A)
                                txt=txt_1+txt_2
                                lbl_txt_1.configure(text=txt)


                    def AB_6():
                        P_head.destroy()
                        btn_P_1.destroy()
                        btn_P_2.destroy()
                        btn_P_3.destroy()
                        btn_P_4.destroy()
                        btn_P_5.destroy()
                        btn_P_6.destroy()
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="   Высота h    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="   Площадь S  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_AB())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=155)
                        ent_1.place(x=50,y=210,width=150,height=45)
                        lbl_2.place(x=40,y=355)
                        ent_2.place(x=50,y=420,width=150,height=45)
                        btn_P_find.place(x=260,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            lbl_txt_1.destroy()
                            triug_AB()
                        def find_AB():
                            H=ent_1.get()
                            S=ent_2.get()
                            txt_1="   A = 2 * S / h\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                H=float(H)
                                S=float(S)
                                if S>=1000 or H>=1000 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if H=="" or S=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if H<=0 or S<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(H)==float(H):
                                    H=int(H)
                                if int(S)==float(S):
                                    S=int(S)
                                txt_2="   A = 2 * "+str(S)+" / "+str(H)+"\n\n"
                                A=2*S/H
                                if int(A)==float(A):
                                    A=int(A)
                                txt_3="   A = "+str(A)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)





                def triug_a():
                    a_head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    a_head.place(x=290,y=10)
                    btn_a_1=Button(text="Три стороны",command=lambda:next("a_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_a_2=Button(text="Площадь,\nпротиволежащая углу\nсторона,\nвторая сторона",command=lambda:next("a_2"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                    btn_a_3=Button(text="Противолежащая сторона,\nвторая сторона\nи угол, противолежащий второй стороне",command=lambda:next("a_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_a_1.place(x=90,y=110,width=310,height=190)
                    btn_a_2.place(x=490,y=110,width=310,height=190)
                    btn_a_3.place(x=130,y=350,width=640,height=190)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)
                    def back():
                        a_head.destroy()
                        btn_a_1.destroy()
                        btn_a_2.destroy()
                        btn_a_3.destroy()
                        btn_back.destroy()
                        triugolnik()
                    def next(x):
                        a_head.destroy()
                        btn_a_1.destroy()
                        btn_a_2.destroy()
                        btn_a_3.destroy()
                        btn_back.destroy()
                        if x=="a_1":
                            a_1()
                        elif x=="a_2":
                            a_2()
                        elif x=="a_3":
                            a_3()


                    def a_1():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="   Сторона A  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="   Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text="   Сторона C  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_a())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",26,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_a()
                        def find_a():
                            A=ent_1.get()
                            B=ent_2.get()
                            C=ent_3.get()
                            txt_1="  cos(α) = (B\N{SUPERSCRIPT TWO}+C\N{SUPERSCRIPT TWO} -A\N{SUPERSCRIPT TWO})/(2*B*C)\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                C=float(C)
                                A=float(A)
                                B=float(B)
                                if B>1000 or C>1000 or A>1000 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if A=="" or B=="" or C=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if C<=0 or B<=0 or A<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                                if A+B<=C or B+C<=A or A+C<=B:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Вы ввели некоректные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(C)==float(C):
                                    C=int(C)
                                if int(B)==float(B):
                                    B=int(B)
                                if int(A)==float(A):
                                    A=int(A)
                                cos_a=(B*B+C*C-A*A)/(2*B*C)
                                a=math.acos(cos_a)
                                a=round(math.degrees(a),5)
                                txt_2="  cos(α) = "+str(round((cos_a),5))+"\n\n"
                                txt_3="  α = "+str(a)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)



                    def a_2():
                        a_head.destroy()
                        btn_a_1.destroy()
                        btn_a_2.destroy()
                        btn_a_3.destroy()
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="   Сторона A  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="   Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text="   Площадь S  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_a())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_a()
                        def find_a():
                            A=ent_1.get()
                            B=ent_2.get()
                            S=ent_3.get()
                            txt_1="  sin(α) = (2 * S) / (A * B)\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                S=float(S)
                                A=float(A)
                                B=float(B)
                                if B>1000 or S>=1000 or A>1000 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if A=="" or B=="" or S=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if S<=0 or B<=0 or A<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(S)==float(S):
                                    S=int(S)
                                if int(B)==float(B):
                                    B=int(B)
                                if int(A)==float(A):
                                    A=int(A)
                                sin_a=2*S/(A*B)
                                txt_2="  sin(α) = "+str(round((sin_a),5))+"\n\n"
                                a=math.asin(sin_a)
                                a=math.degrees(a)
                                txt_3="  α = "+str(round((a),5))
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)


                    def a_3():
                        a_head.destroy()
                        btn_a_1.destroy()
                        btn_a_2.destroy()
                        btn_a_3.destroy()
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="   Сторона A  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="   Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text="      Угол β      ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_a())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_P_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_P_find.destroy()
                            lbl_1.destroy()
                            lbl_2.destroy()
                            lbl_3.destroy()
                            ent_1.destroy()
                            ent_2.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            triug_a()
                        def find_AB():
                            A=ent_1.get()
                            B=ent_2.get()
                            ugl=ent_3.get()
                            txt_1="  sin(α) = A * sin(β) / B\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                ugl=float(ugl)
                                A=float(A)
                                B=float(B)
                                if B>1000 or ugl>=180 or A>1000 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if A=="" or B=="" or ugl=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if ugl<=0 or B<=0 or A<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(ugl)==float(ugl):
                                    ugl=int(ugl)
                                if int(B)==float(B):
                                    B=int(B)
                                if int(A)==float(A):
                                    A=int(A)
                                sin_b=math.sin(math.radians(ugl))
                                sin_a=A*sin_b/B
                                a=math.asin(sin_a)
                                a=math.degrees(a)
                                a=round(a,5)
                                txt_2="  sin(α) = "+str(round((sin_a),5))+"\n\n"
                                txt_3="  α = "+str(a)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)


            def krug():
                krug_head=Label(text="Что нужно найти",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                krug_head.place(x=290,y=10)
                btn_krug_1=Button(text="Площадь круга",command=lambda:next("krug_S"),bg="#f67300",fg="#362b2b",font=("Calibri",24,"bold"))
                btn_krug_2=Button(text="Площадь сектора",command=lambda:next("krug_s"),bg="#f67300",fg="#362b2b",font=("Calibri",24,"bold"))
                btn_krug_3=Button(text="Радиус окружности",command=lambda:next("krug_R"),bg="#f67300",fg="#362b2b",font=("Calibri",24,"bold"))
                btn_krug_1.place(x=120,y=110,width=300,height=180)
                btn_krug_2.place(x=460,y=110,width=300,height=180)
                btn_krug_3.place(x=120,y=350,width=640,height=190)
                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)
                def next(x):
                    krug_head.destroy()
                    btn_krug_1.destroy()
                    btn_krug_2.destroy()
                    btn_krug_3.destroy()
                    btn_back.destroy()
                    if x=="krug_S":
                        krug_S()
                    elif x=="krug_s":
                        krug_s()
                    elif x=="krug_R":
                        krug_R()
                def back():
                    krug_head.destroy()
                    btn_krug_1.destroy()
                    btn_krug_2.destroy()
                    btn_krug_3.destroy()
                    btn_back.destroy()
                    geom()


                def krug_R():
                    krug_head.destroy()
                    btn_krug_1.destroy()
                    btn_krug_2.destroy()
                    btn_krug_3.destroy()
                    R_head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    R_head.place(x=290,y=10)
                    btn_R_1=Button(text="Длина\nокружности",command=lambda:next("R_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_R_2=Button(text="Площадь круга",command=lambda:next("R_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_R_3=Button(text="Три стороны\nописанного\nтрегуольника",command=lambda:next("R_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_R_4=Button(text="Три стороны\nвписанного\nтрегуольника",command=lambda:next("R_4"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_R_1.place(x=90,y=110,width=310,height=190)
                    btn_R_2.place(x=490,y=110,width=310,height=190)
                    btn_R_3.place(x=90,y=350,width=310,height=190)
                    btn_R_4.place(x=490,y=350,width=310,height=190)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)
                    def next(x):
                        R_head.destroy()
                        btn_R_1.destroy()
                        btn_R_2.destroy()
                        btn_R_3.destroy()
                        btn_R_4.destroy()
                        btn_back.destroy()
                        if x=="R_1":
                            R_1()
                        elif x=="R_2":
                            R_2()
                        elif x=="R_3":
                            R_3()
                        elif x=="R_4":
                            R_4()

                    def back():
                        btn_back.destroy()
                        R_head.destroy()
                        btn_R_1.destroy()
                        btn_R_2.destroy()
                        btn_R_3.destroy()
                        btn_R_4.destroy()
                        krug()


                    def R_1():

                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="Длина окружности",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_R_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_R())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=130)
                        ent_1.place(x=50,y=185,width=150,height=45)
                        btn_R_find.place(x=260,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_R_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_txt_1.destroy()
                            krug_R()


                        def find_R():
                            L=ent_1.get()
                            txt_1="  R = L / (2 * π)\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                L=float(L)
                                if L>=1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if L=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if L<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(L)==float(L):
                                    L=int(L)
                                R=round((L/(2*math.pi)),5)
                                txt_2="  R = "+str(R)
                                txt=txt_1+txt_2
                                lbl_txt_1.configure(text=txt)








                    def R_2():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="   Площадь S  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_R_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_R())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=130)
                        ent_1.place(x=50,y=185,width=150,height=45)
                        btn_R_find.place(x=260,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_R_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_txt_1.destroy()
                            krug_R()

                        def find_R():
                            S=ent_1.get()
                            txt_1="  R = √(S / π)\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                S=float(S)
                                if S>=1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if S=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if S<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(S)==float(S):
                                    S=int(S)
                                txt_2="  R = √("+str(S)+" / "+str(round(math.pi,2))+")\n"
                                R=round(pow((S/math.pi),0.5),4)
                                txt_3="  R = "+str(R)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)


                    def R_3():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text=" Сторона B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text=" Сторона C ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_R_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_R())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=110)
                        bg.place(x=415,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_R_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_R_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_2.destroy()
                            ent_2.destroy()
                            lbl_3.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            krug_R()

                        def find_R():
                            a=ent_1.get()
                            b=ent_2.get()
                            c=ent_3.get()
                            txt_1="\n R = S/p\n p - полупериметр\n p=(A + B + C) / 2\n S = √(p*(p-A)*(p-B)*(p-C))\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try: 
                                a=float(a)
                                b=float(b)
                                c=float(c)
                                if a>1000 or b>1000 or c>1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if a=="" or b=="" or c=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if a<=0 or b<=0 or c<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                                if a+b<=c or b+c<=a or a+c<=b:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Вы ввели некоректные значения")
                                    error=1
                                    err=2/0

                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:
                                if int(a)==float(a):
                                    a=int(a)
                                if int(b)==float(b):
                                    b=int(b)
                                if int(c)==float(c):
                                    c=int(c)
                                p=(a+b+c)/2
                                S1=(p*(p-a)*(p-b)*(p-c))
                                S=round(pow(S1,0.5),4)
                                txt_2=" S = "+str(S)+"\n"
                                R=S/p
                                R=round(R,4)
                                txt_3=" r = "+str(R)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)

                    def R_4():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text=" Сторона B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text=" Сторона C ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_R_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_R())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=110)
                        bg.place(x=415,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_R_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_R_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_2.destroy()
                            ent_2.destroy()
                            lbl_3.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            krug_R()

                        def find_R():
                            a=ent_1.get()
                            b=ent_2.get()
                            c=ent_3.get()
                            txt_1="\n R = A * B * C / (4 * S)\n p - полупериметр\n S - площадь треугольника\n p=(A + B + C) / 2\n S = √(p*(p-A)*(p-B)*(p-C))\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                a=float(a)
                                b=float(b)
                                c=float(c)
                                if a>1000 or b>1000 or c>1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if a=="" or b=="" or c=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if a<=0 or b<=0 or c<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                                if a+b<=c or b+c<=a or a+c<=b:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Вы ввели некоректные значения")
                                    error=1
                                    err=2/0

                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:
                                if int(a)==float(a):
                                    a=int(a)
                                if int(b)==float(b):
                                    b=int(b)
                                if int(c)==float(c):
                                    c=int(c)
                                p=(a+b+c)/2
                                S1=(p*(p-a)*(p-b)*(p-c))
                                S=round(pow(S1,0.5),4)
                                txt_2=" S = "+str(S)+"\n"
                                R=a*b*c/(4*S)
                                R=round(R,4)
                                txt_3=" R = "+str(R)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)


                def krug_S():
                    krug_head.destroy()
                    btn_krug_1.destroy()
                    btn_krug_2.destroy()
                    btn_krug_3.destroy()
                    S_head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    S_head.place(x=290,y=10)
                    btn_S_1=Button(text="Радиус",command=lambda:next("S_1"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                    btn_S_2=Button(text="Диаметр",command=lambda:next("S_2"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                    btn_S_3=Button(text="Длину окружности",command=lambda:next("S_3"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                    btn_S_4=Button(text="Три стороны\nописанного треугольника",command=lambda:next("S_4"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                    btn_S_5=Button(text="Три стороны\nвписанного треугольника",command=lambda:next("S_5"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                    btn_S_1.place(x=50,y=110,width=240,height=170)
                    btn_S_2.place(x=330,y=110,width=240,height=170)
                    btn_S_3.place(x=610,y=110,width=250,height=170)
                    btn_S_4.place(x=50,y=350,width=370,height=170)
                    btn_S_5.place(x=470,y=350,width=385,height=170)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)  
                    def next(x):
                        S_head.destroy()
                        btn_S_1.destroy()
                        btn_S_2.destroy()
                        btn_S_3.destroy()
                        btn_S_4.destroy()
                        btn_S_5.destroy()
                        btn_back.destroy()
                        if x=="S_1":
                            S_1()
                        elif x=="S_2":
                            S_2()
                        elif x=="S_3":
                            S_3()
                        elif x=="S_4":
                            S_4()
                        elif x=="S_5":
                            S_5()
                    def back():
                        btn_back.destroy()
                        S_head.destroy()
                        btn_S_1.destroy()
                        btn_S_2.destroy()
                        btn_S_3.destroy()
                        btn_S_4.destroy()
                        btn_S_5.destroy()
                        krug()


                    def S_1():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="   Радиус R  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_R_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_S())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=130)
                        ent_1.place(x=50,y=185,width=150,height=45)
                        btn_R_find.place(x=260,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_R_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_txt_1.destroy()
                            krug_S()
                        def find_S():
                            R=ent_1.get()
                            txt_1="\n  S = π * R\N{SUPERSCRIPT TWO}\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                R=float(R)
                                if R>=1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if R=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if R<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(R)==float(R):
                                    R=int(R)
                                S=math.pi*R*R
                                S=round(S,5)
                                txt_2="  S = "+str(S)
                                txt=txt_1+txt_2
                                lbl_txt_1.configure(text=txt)



                    def S_2():

                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="   Диаметр D  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_R_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_S())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=130)
                        ent_1.place(x=50,y=185,width=150,height=45)
                        btn_R_find.place(x=260,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_R_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_txt_1.destroy()
                            krug_S()
                        def find_S():
                            D=ent_1.get()
                            txt_1="  S = π * D\N{SUPERSCRIPT TWO} / 4\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                D=float(D)
                                if D>=1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if D=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if D<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(D)==float(D):
                                    D=int(D)
                                S=math.pi*D*D/4
                                S=round(S,5)
                                txt_2="  S = "+str(S)
                                txt=txt_1+txt_2
                                lbl_txt_1.configure(text=txt)



                    def S_3():

                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="Длина окр. L",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_R_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_S())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=130)
                        ent_1.place(x=55,y=185,width=150,height=45)
                        btn_R_find.place(x=260,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_R_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_txt_1.destroy()
                            krug_S()
                        def find_S():
                            L=ent_1.get()
                            txt_1="  S = L\N{SUPERSCRIPT TWO} / (4 * π)\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                L=float(L)
                                if L>=1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if L=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if L<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(L)==float(L):
                                    L=int(L)
                                S=L*L/(math.pi*4)
                                S=round(S,5)
                                txt_2="  S = "+str(S)
                                txt=txt_1+txt_2
                                lbl_txt_1.configure(text=txt)


                    def S_4():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text=" Сторона B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text=" Сторона C ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_S_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_S())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=110)
                        bg.place(x=415,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_S_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_S_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_2.destroy()
                            ent_2.destroy()
                            lbl_3.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            krug_S()
                        def find_S():
                            a=ent_1.get()
                            b=ent_2.get()
                            c=ent_3.get()
                            txt_1="\n p - полупериметр\n S = π * r\N{SUPERSCRIPT TWO}\n S = π * (p-A)*(p-B)*(p-C) / p\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                a=float(a)
                                b=float(b)
                                c=float(c)
                                if a>1000 or b>1000 or c>1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if a=="" or b=="" or c=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if a<=0 or b<=0 or c<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                                if a+b<=c or b+c<=a or a+c<=b:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Вы ввели некоректные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:
                                p=(a+b+c)/2
                                p_2=(p-a)*(p-b)*(p-c)
                                p_2=round(p_2,5)
                                txt_2="  S = π * "+str(p_2)+" / "+str(p)+"\n"
                                S=math.pi*p_2/p
                                S=round(S,5)
                                txt_3="  S = "+str(S)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)


                    def S_5():
                        S_head.destroy()
                        btn_S_1.destroy()
                        btn_S_2.destroy()
                        btn_S_3.destroy()
                        btn_S_4.destroy()
                        btn_S_5.destroy()
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text=" Сторона B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_3=Label(text=" Сторона C ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_S_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_S())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",24,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        cherta=Label(bg="#f67300")
                        lbl_txt_1.place(x=427,y=110)
                        bg.place(x=415,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=90)
                        ent_1.place(x=50,y=155,width=150,height=45)
                        lbl_2.place(x=40,y=260)
                        ent_2.place(x=50,y=325,width=150,height=45)
                        lbl_3.place(x=40,y=430)
                        ent_3.place(x=50,y=495,width=150,height=45)
                        btn_S_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_S_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_2.destroy()
                            ent_2.destroy()
                            lbl_3.destroy()
                            ent_3.destroy()
                            lbl_txt_1.destroy()
                            cherta.destroy()
                            krug_S()

                        def find_S():
                            a=ent_1.get()
                            b=ent_2.get()
                            c=ent_3.get()
                            txt_1="  p - полупериметр\n\n  S =             π * A\N{SUPERSCRIPT TWO} * B\N{SUPERSCRIPT TWO} * C\N{SUPERSCRIPT TWO}\n             16*p*(p-A)*(p-B)*(p-C)\n\n\n"
                            error=0 
                            lbl_txt_1.configure(text=txt_1)
                            cherta.place(x=510,y=228,width=318,height=4)
                            try:
                                a=float(a)
                                b=float(b)
                                c=float(c)
                                if a>1000 or b>1000 or c>1000:
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if a=="" or b=="" or c=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if a<=0 or b<=0 or c<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                                if a+b<=c or b+c<=a or a+c<=b:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Вы ввели некоректные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения")
                            else:
                                p=(a+b+c)/2
                                chisl_sqr=a*a*b*b*c*c
                                znam_perimetr=p*(p-a)*(p-b)*(p-c)
                                S=math.pi*chisl_sqr/(16*znam_perimetr)
                                S=round(S,5)
                                txt_2="  S = "+str(S)
                                txt=txt_1+txt_2
                                lbl_txt_1.configure(text=txt)

                def krug_s():
                    krug_head.destroy()
                    btn_krug_1.destroy()
                    btn_krug_2.destroy()
                    btn_krug_3.destroy()
                    s_head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    s_head.place(x=290,y=10)
                    btn_s_1=Button(text="Радиус окружности и\nугол из центра окружности,\nсмотрящий на сектор",command=lambda:next("s_1"),fg="#f67300",bg="#362b2b",font=("Calibri",20,"bold"))
                    btn_s_2=Button(text="Радиус окружности и\nдлину дуги сектора",command=lambda:next("s_2"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))  
                    btn_s_1.place(x=50,y=200,width=350,height=200)
                    btn_s_2.place(x=500,y=200,width=350,height=200)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)  
                    def next(x):
                        s_head.destroy()
                        btn_s_1.destroy()
                        btn_s_2.destroy()
                        btn_back.destroy()
                        if x=="s_1":
                            s_1()
                        elif x=="s_2":
                            s_2()
                    def back():
                        btn_back.destroy()
                        s_head.destroy()
                        btn_s_1.destroy()
                        btn_s_2.destroy()
                        krug()

                    def s_1():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="   Радиус R  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="     Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_s_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_s())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=155)
                        ent_1.place(x=50,y=210,width=150,height=45)
                        lbl_2.place(x=40,y=355)
                        ent_2.place(x=50,y=420,width=150,height=45)
                        btn_s_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_s_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_2.destroy()
                            ent_2.destroy()
                            lbl_txt_1.destroy()
                            krug_s()
                        def find_s():
                            R=ent_1.get()
                            ugl=ent_2.get()
                            txt_1="  S = π * R\N{SUPERSCRIPT TWO} * α / 360\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                ugl=float(ugl)
                                R=float(R)

                                if ugl>=180 or R>1000 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if R=="" or ugl=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if ugl<=0 or R<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(ugl)==float(ugl):
                                    ugl=int(ugl)
                                if int(R)==float(R):
                                    R=int(R)
                                txt_2="  S = π * "+str(R*R)+" * "+str(ugl)+" / 360\n"
                                S=math.pi*R*R*ugl/360
                                S=round(S,5)
                                txt_3="  S = "+str(S)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)



                    def s_2():
                        head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                        head.place(x=310,y=10)
                        lbl_1=Label(text="   Радиус R  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        lbl_2=Label(text="    Длина L   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                        ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                        btn_s_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find_s())
                        bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                        lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                        lbl_txt_1.place(x=427,y=200)
                        bg.place(x=425,y=90,width=450,height=470)
                        lbl_1.place(x=40,y=155)
                        ent_1.place(x=50,y=210,width=150,height=45)
                        lbl_2.place(x=40,y=355)
                        ent_2.place(x=50,y=420,width=150,height=45)
                        btn_s_find.place(x=255,y=265,height=70)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def back():
                            btn_back.destroy()
                            head.destroy()
                            bg.destroy()
                            btn_s_find.destroy()
                            lbl_1.destroy()
                            ent_1.destroy()
                            lbl_2.destroy()
                            ent_2.destroy()
                            lbl_txt_1.destroy()
                            krug_s()
                        def find_s():
                            L=ent_1.get()
                            R=ent_2.get()
                            txt_1="  S = L * R / 2\n\n"
                            error=0
                            lbl_txt_1.configure(text=txt_1)
                            try:
                                R=float(R)
                                L=float(L)

                                if R>=1000 or L>=1000 :
                                    messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                    error=1
                                    err=2/0
                                if L=="" or R=="":
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите все значения")
                                    error=1
                                    err=2/0
                                if R<=0 or L<=0:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите положительные значения")
                                    error=1
                                    err=2/0
                            except:
                                if error==0:
                                    messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                            else:
                                if int(R)==float(R):
                                    R=int(R)
                                if int(L)==float(L):
                                    L=int(L)
                                txt_2="  S = "+str(L)+" * "+str(R)+" / 2\n"
                                S=L*R/2
                                S=round(S,5)
                                txt_3="  S = "+str(S)
                                txt=txt_1+txt_2+txt_3
                                lbl_txt_1.configure(text=txt)


            def ugolnik_4():
                head_ugl=Label(text="Выберите фигуру",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                head_ugl.place(x=290,y=10)
                btn_ugl_1=Button(text="Квадрат",command=lambda:next("kvadr"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                btn_ugl_2=Button(text="Прямоугольник",command=lambda:next("pryamoug"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                btn_ugl_3=Button(text="Трапеция",command=lambda:next("trapec"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                btn_ugl_4=Button(text="Ромб",command=lambda:next("romb"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                btn_ugl_5=Button(text="Параллелограмм",command=lambda:next("parall"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                btn_ugl_1.place(x=50,y=110,width=240,height=170)
                btn_ugl_2.place(x=325,y=110,width=250,height=170)
                btn_ugl_3.place(x=610,y=110,width=250,height=170)
                btn_ugl_4.place(x=50,y=350,width=370,height=170)
                btn_ugl_5.place(x=470,y=350,width=385,height=170)
                btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                btn_back.place(x=5,y=5)  
                def next(x):
                    head_ugl.destroy()
                    btn_ugl_1.destroy()
                    btn_ugl_2.destroy()
                    btn_ugl_3.destroy()
                    btn_ugl_4.destroy()
                    btn_ugl_5.destroy()
                    btn_back.destroy()
                    if x=="kvadr":
                        kvadr()
                    elif x=="pryamoug":
                        pryamoug()
                    elif x=="romb":
                        romb()
                    elif x=="trapec":
                        trapec()
                    elif x=="parall":
                        parall()
                def back():
                    head_ugl.destroy()
                    btn_ugl_1.destroy()
                    btn_ugl_2.destroy()
                    btn_ugl_3.destroy()
                    btn_ugl_4.destroy()
                    btn_ugl_5.destroy()
                    btn_back.destroy()
                    geom()


                def romb():    
                    head=Label(text="Что нужно найти",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    head.place(x=290,y=10)
                    btn_1=Button(text="Сторону A",command=lambda:next("romb_A"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_2=Button(text="Площадь S",command=lambda:next("romb_S"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_3=Button(text="Диагональ D",command=lambda:next("romb_D"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_1.place(x=120,y=110,width=310,height=190)
                    btn_2.place(x=470,y=110,width=310,height=190)
                    btn_3.place(x=120,y=350,width=650,height=190)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)  
                    def next(x):
                        head.destroy()
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        btn_back.destroy()
                        if x=="romb_A":
                            romb_A()
                        elif x=="romb_S":
                            romb_S()
                        elif x=="romb_D":
                            romb_D()
                    def back():
                        head.destroy()
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        btn_back.destroy()
                        ugolnik_4()


                    def romb_A():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Две диагонали",command=lambda:next("A_1"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_2=Button(text="Площадь и любой\nугол ромба",command=lambda:next("A_2"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_3=Button(text="Диагональ и угол ромба,\nсмотрящий на эту диагональ",command=lambda:next("A_3"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="A_1":
                                A_1()
                            elif x=="A_2":
                                A_2()
                            elif x=="A_3":
                                A_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            romb()

                        
                        def A_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Диагональ d ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                romb_A()

                            def find():
                                D=ent_1.get()
                                d=ent_2.get()
                                txt_1= "  A = √(D\N{SUPERSCRIPT TWO} + d\N{SUPERSCRIPT TWO}) / 2\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    d=float(d)
                                    D=float(D)
                                    if d>=1000 or D>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if d=="" or D=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if d<=0 or D<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(d)==float(d):
                                        d=int(d)
                                    if int(D)==float(D):
                                        D=int(D)
                                    txt_2="  A = √("+str(D)+"\N{SUPERSCRIPT TWO} + "+str(d)+"\N{SUPERSCRIPT TWO}) / 2\n"
                                    A=(D*D+d*d)**0.5/2
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                        def A_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Площадь S ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="   Угол α   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                romb_A()
                            def find():
                                S=ent_1.get()
                                a=ent_2.get()
                                txt_1= "  A = √(S / sin(α))\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    S=float(S)
                                    a=float(a)
                                    if S>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if S=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if S<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(S)==float(S):
                                        S=int(S)
                                    if int(a)==float(a):
                                        a=int(a)

                                    txt_2="  A = √("+str(S)+" / sin("+str(a)+")) \n"
                                    ugl=math.radians(a)
                                    sin=math.sin(ugl)
                                    A=(S/sin)**0.5
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                        def A_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="   Угол α   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                romb_A()
                            def find():
                                D=ent_1.get()
                                a=ent_2.get()
                                txt_1= "  A = D / (2 * sin(α/2))\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    a=float(a)
                                    if D>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if D=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if D<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(D)==float(D):
                                        D=int(D)
                                    if int(a)==float(a):
                                        a=int(a)

                                    txt_2="  A = "+str(D)+" / (2 * sin("+str(a/2)+")) \n"
                                    ugl=math.radians(a/2)
                                    sin=math.sin(ugl)
                                    A=D/(2*sin)
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                    def romb_S():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Две диагонали",command=lambda:next("S_1"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_2=Button(text="Сторона и любой\nугол ромба",command=lambda:next("S_2"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_3=Button(text="Диагональ и угол ромба,\nне смотрящий на эту диагональ",command=lambda:next("S_3"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="S_1":
                                S_1()
                            elif x=="S_2":
                                S_2()
                            elif x=="S_3":
                                S_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            romb()



                        def S_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Диагональ d ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                romb_S()
                            def find():
                                D=ent_1.get()
                                d=ent_2.get()
                                txt_1= "  S = (D * d) / 2\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    d=float(d)
                                    D=float(D)
                                    if d>=1000 or D>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if d=="" or D=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if d<=0 or D<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(d)==float(d):
                                        d=int(d)
                                    if int(D)==float(D):
                                        D=int(D)
                                    txt_2="  S = ("+str(D)+" * "+str(d)+") / 2\n"
                                    S=(D*d)/2
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                        def S_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="    Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                romb_S()
                            def find():
                                A=ent_1.get()
                                a=ent_2.get()
                                txt_1= "  S = A\N{SUPERSCRIPT TWO} * sin(α)\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    a=float(a)
                                    A=float(A)
                                    if a>=180 or A>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if a=="" or A=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if a<=0 or A<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(a)==float(a):
                                        a=int(a)
                                    if int(A)==float(A):
                                        A=int(A)
                                    txt_2="  S = "+str(A)+"\N{SUPERSCRIPT TWO} * sin("+str(a)+")\n"
                                    ugl=math.radians(a)
                                    sin=math.sin(ugl)
                                    S=A*A*sin
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                        def S_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="    Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                romb_S()
                            def find():
                                D=ent_1.get()
                                a=ent_2.get()
                                txt_1= "  S = 0.5 * D\N{SUPERSCRIPT TWO} * tg(α/2) \n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    a=float(a)
                                    D=float(D)
                                    if a>=180 or D>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if a=="" or D=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if a<=0 or D<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(a)==float(a):
                                        a=int(a)
                                    if int(D)==float(D):
                                        D=int(D)
                                    txt_2="  S = 0.5 * "+str(D)+"\N{SUPERSCRIPT TWO} * tg("+str(a/2)+")\n"
                                    ugl=math.radians(a/2)
                                    tg=math.tan(ugl)
                                    S=D*D*tg/2
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)
                
                    def romb_D():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Площадь и\nвторая диагональ",command=lambda:next("D_1"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_2=Button(text="Сторона и угол\nромба, смотрящий\nна диагональ",command=lambda:next("D_2"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_3=Button(text="Сторона и\nвторая диагональ",command=lambda:next("D_3"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_4=Button(text="Диагональ и угол\nромба, смотрящий\nна диагональ",command=lambda:next("D_4"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_1.place(x=90,y=110,width=310,height=190)
                        _btn_2.place(x=490,y=110,width=310,height=190)
                        _btn_3.place(x=90,y=350,width=310,height=190)
                        _btn_4.place(x=490,y=350,width=310,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            _btn_4.destroy()
                            btn_back.destroy()
                            if x=="D_1":
                                D_1()
                            elif x=="D_2":
                                D_2()
                            elif x=="D_3":
                                D_3()
                            elif x=="D_4":
                                D_4()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            _btn_4.destroy()
                            btn_back.destroy()
                            romb()



                        def D_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Площадь S  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                romb_D()
                            def find():
                                D=ent_1.get()
                                S=ent_2.get()
                                txt_1= "  d = 2 * S / D\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    S=float(S)
                                    D=float(D)
                                    if S>=1000 or D>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if S=="" or D=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if S<=0 or D<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(S)==float(S):
                                        S=int(S)
                                    if int(D)==float(D):
                                        D=int(D)
                                    txt_2="  d = 2 * "+str(S)+" / "+str(D)+"\n"
                                    d=2*S/D
                                    d=round(d,5)
                                    txt_3="  d = "+str(d)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                        def D_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="    Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                romb_D()
                            def find():
                                A=ent_1.get()
                                a=ent_2.get()
                                txt_1= "  d = A * √(2 - 2*cos(α))\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    a=float(a)
                                    if A>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    if int(a)==float(a):
                                        a=int(a)
                                    txt_2="  d = "+str(A)+" *  √(2 - 2*cos("+str(a)+"))\n"
                                    ugl=math.radians(a)
                                    cos=math.cos(ugl)
                                    d=A*((2-2*cos)**0.5)
                                    d=round(d,5)
                                    txt_3="  d = "+str(d)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def D_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Сторона A  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                romb_D()
                            def find():
                                A=ent_1.get()
                                D=ent_2.get()
                                txt_1= "  d = √(4*A\N{SUPERSCRIPT TWO} - D\N{SUPERSCRIPT TWO})\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    D=float(D)
                                    if A>=1000 or D>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="" or D=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0 or D<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                    if A>=D or 4*A*A<=D:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введены некорректные значения")
                                        error=1
                                        err=2/0

                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    if int(D)==float(D):
                                        D=int(D)
                                    txt_2="  d = √(4*"+str(A)+"\N{SUPERSCRIPT TWO} - "+str(D)+"\N{SUPERSCRIPT TWO})\n"
                                    d=((4*A*A-D*D)**0.5)
                                    d=round(d,5)
                                    txt_3="  d = "+str(d)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                        def D_4():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="    Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                romb_D()
                            def find():
                                a=ent_1.get()
                                D=ent_2.get()
                                txt_1= "  d = D * tg(α/2)\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    a=float(a)
                                    D=float(D)
                                    if a>=1000 or D>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if a=="" or D=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if a<=0 or D<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(a)==float(a):
                                        a=int(a)
                                    if int(D)==float(D):
                                        D=int(D)
                                    txt_2="  d = "+str(D)+" * tg("+str(a/2)+")\n"
                                    ugl=math.radians(a/2)
                                    tg=math.tan(ugl)
                                    d=D*tg
                                    d=round(d,5)
                                    txt_3="  d = "+str(d)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                def parall():
                    head=Label(text="Что нужно найти",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    head.place(x=290,y=10)
                    btn_1=Button(text="Сторону A",command=lambda:next("parall_A"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_2=Button(text="Площадь S",command=lambda:next("parall_S"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_3=Button(text="Диагональ D",command=lambda:next("parall_D"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_1.place(x=120,y=110,width=310,height=190)
                    btn_2.place(x=470,y=110,width=310,height=190)
                    btn_3.place(x=120,y=350,width=650,height=190)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)  
                    def next(x):
                        head.destroy()
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        btn_back.destroy()
                        if x=="parall_A":
                            parall_A()
                        elif x=="parall_S":
                            parall_S()
                        elif x=="parall_D":
                            parall_D()
                    def back():
                        head.destroy()
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        btn_back.destroy()
                        ugolnik_4()

                    def parall_A():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Высота, проведенная\nк искомой стороне\nи любой угол\nпараллелограмма",command=lambda:next("A_1"),fg="#f67300",bg="#362b2b",font=("Calibri",21,"bold"))
                        _btn_2=Button(text="Две диагонали и\nвторая сторона",command=lambda:next("A_2"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                        _btn_3=Button(text="Две диагонали и угол образованный ими,\nсмотрящий на искомую сторону",command=lambda:next("A_3"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="A_1":
                                A_1()
                            elif x=="A_2":
                                A_2()
                            elif x=="A_3":
                                A_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            parall()




                        def A_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Высота H  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="    Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                parall_A()
                            def find():
                                H=ent_1.get()
                                a=ent_2.get()
                                txt_1="  A = H / sin(α)\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    H=float(H)
                                    a=float(a)
                                    if H>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if H=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if H<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(H)==float(H):
                                        H=int(H)
                                    if int(a)==float(a):
                                        a=int(a)
                                    txt_2="  A = "+str(H)+" / sin("+str(a)+")\n"
                                    ugl=math.radians(a)
                                    sin=math.sin(ugl)
                                    A=H/sin
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                        def A_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Диагональ d ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="  Сторона B   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                parall_A()
                            def find():
                                D=ent_1.get()
                                d=ent_2.get()
                                B=ent_3.get()
                                txt_1="\n A = √( (D\N{SUPERSCRIPT TWO}+d\N{SUPERSCRIPT TWO}-2*B\N{SUPERSCRIPT TWO}) / 2)\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    d=float(d)
                                    B=float(B)
                                    if D>=1000 or d>=1000 or B>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if D=="" or d=="" or B=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if D<=0 or d<=0 or B<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                    if B>=D or B>=d:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введены некоректные значения")
                                        error=1
                                        err=2/0

                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(D)==float(D):
                                        D=int(D)
                                    if int(d)==float(d):
                                        d=int(d)
                                    if int(B)==float(B):
                                        B=int(B)
                                    skobka=(D*D+d*d-2*B*B)/2
                                    txt_2=" A =  √("+str(skobka)+")\n"
                                    A=pow(skobka,0.5)
                                    A=round(A,5)
                                    txt_3=" A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def A_3():
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            _head.destroy()
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Диагональ d ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="    Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",23,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                parall_A()
                            def find():
                                D=ent_1.get()
                                d=ent_2.get()
                                a=ent_3.get()
                                txt_1=" A = 0.5*√(D\N{SUPERSCRIPT TWO} + d\N{SUPERSCRIPT TWO} - 2*D*d*cos(α))\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    d=float(d)
                                    a=float(a)
                                    if D>=1000 or d>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if D=="" or d=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if D<=0 or d<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(D)==float(D):
                                        D=int(D)
                                    if int(d)==float(d):
                                        d=int(d)
                                    ugl=math.radians(a)
                                    cos=math.cos(ugl)
                                    skobka=D*D+d*d-D*d*cos
                                    skobka=round(skobka,5)
                                    txt_2=" A = 0.5 * √("+str(skobka)+")\n"
                                    A=pow(skobka,0.5)
                                    A=round(A,5)
                                    txt_3=" A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                    def parall_S():
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        head.destroy()
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Сторона и высота,\nпроведенная к этой\nстороне",command=lambda:next("S_1"),fg="#f67300",bg="#362b2b",font=("Calibri",21,"bold"))
                        _btn_2=Button(text="Две диагонали и \nлюбой угол,\nобразованный ими",command=lambda:next("S_2"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                        _btn_3=Button(text="Две стороны и\nлюбой угол параллелограмма",command=lambda:next("S_3"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="S_1":
                                S_1()
                            elif x=="S_2":
                                S_2()
                            elif x=="S_3":
                                S_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            parall()



                        def S_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Высота H ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                parall_S()
                            def find():
                                H=ent_1.get()
                                A=ent_2.get()
                                txt_1="  S = A * H\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    H=float(H)
                                    A=float(A)
                                    if H>=1000 or A>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if H=="" or A=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if H<=0 or A<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(H)==float(H):
                                        H=int(H)
                                    if int(A)==float(A):
                                        A=int(A)
                                    txt_2="  S = "+str(A)+" * "+str(H)+"\n"
                                    S=A*H
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                        def S_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Диагональ d ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="    Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",26,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                parall_S()
                            def find():
                                D=ent_1.get()
                                d=ent_2.get()
                                a=ent_3.get()
                                txt_1="  S = D * d * sin(α) / 2\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    d=float(d)
                                    a=float(a)
                                    if D>=1000 or d>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if D=="" or d=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if D<=0 or d<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(D)==float(D):
                                        D=int(D)
                                    if int(d)==float(d):
                                        d=int(d)
                                    if int(a)==float(a):
                                        a=int(a)
                                    txt_2="  S = "+str(D)+" * "+str(d)+" * sin("+str(a)+") / 2\n"
                                    ugl=math.radians(a)
                                    sin=math.sin(ugl)
                                    S=D*d*sin/2
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def S_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Сторона B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="   Угол α   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",26,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                parall_S()
                            def find():
                                A=ent_1.get()
                                B=ent_2.get()
                                a=ent_3.get()
                                txt_1="  S = A * B * sin(α)\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    B=float(B)
                                    a=float(a)
                                    if A>=1000 or B>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="" or B=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0 or B<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    if int(B)==float(B):
                                        B=int(B)
                                    if int(a)==float(a):
                                        a=int(a)
                                    txt_2="  S = "+str(A)+" * "+str(B)+" * sin("+str(a)+")\n"
                                    ugl=math.radians(a)
                                    sin=math.sin(ugl)
                                    S=A*B*sin
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                    def parall_D():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Две стороны и\nвторая диагональ",command=lambda:next("D_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_2=Button(text="Площадь,\nвторая диагональ и\nугол, образованный\nдиагоналями",command=lambda:next("D_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_3=Button(text="Две стороны и\n угол параллелограмма, смотрящий\nна искомую диагональ",command=lambda:next("D_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="D_1":
                                D_1()
                            elif x=="D_2":
                                D_2()
                            elif x=="D_3":
                                D_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            parall()

                        def D_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Сторона A  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="  Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 24 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                parall_D()
                            def find():
                                D=ent_1.get()
                                A=ent_2.get()
                                B=ent_3.get()
                                txt_1="\n  d = √(2*A\N{SUPERSCRIPT TWO} + 2*B\N{SUPERSCRIPT TWO} - D\N{SUPERSCRIPT TWO})\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    A=float(A)
                                    B=float(B)
                                    if D>=1000 or A>=1000 or B>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if D=="" or A=="" or B=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if D<=0 or A<=0 or B<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                    if B>=D or A>=D:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введены некоректные значения")
                                        error=1
                                        err=2/0

                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(D)==float(D):
                                        D=int(D)
                                    if int(A)==float(A):
                                        A=int(A)
                                    if int(B)==float(B):
                                        B=int(B)
                                    skobka=2*A*A+2*B*B-D*D
                                    if skobka>0:
                                        skobka=round(skobka,4)
                                        txt_2="  d =  √("+str(skobka)+")\n"
                                        d=pow(skobka,0.5)
                                        d=round(d,5)
                                        txt_3="  d = "+str(d)
                                        txt=txt_1+txt_2+txt_3
                                        lbl_txt_1.configure(text=txt)
                                    else:
                                        messagebox.showinfo("Ошибка","Введены некоректные значения")


                        def D_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Площадь S ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="Диагональ D",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="    Угол α   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                parall_D()
                            def find():
                                S=ent_1.get()
                                D=ent_2.get()
                                a=ent_3.get()
                                txt_1="\n  d = 2 * S / (D * sin(α))\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    S=float(S)
                                    a=float(a)
                                    if D>=1000 or S>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if D=="" or S=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if D<=0 or S<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0

                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(D)==float(D):
                                        D=int(D)
                                    if int(S)==float(S):
                                        S=int(S)
                                    if int(a)==float(a):
                                        a=int(a)

                                    txt_2=" d = 2 * "+str(S)+" / ("+str(D)+" * sin("+str(a)+"))\n"
                                    ugl=math.radians(a)
                                    sin=math.sin(ugl)
                                    d=2*S/(D*sin)
                                    d=round(d,5)
                                    txt_3=" d = "+str(d)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                        def D_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Сторона B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="     Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",25,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                parall_D()
                            def find():
                                A=ent_1.get()
                                B=ent_2.get()
                                a=ent_3.get()
                                txt_1="\n  d = √(A\N{SUPERSCRIPT TWO} + B\N{SUPERSCRIPT TWO} - 2*A*B*sin(α))\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    B=float(B)
                                    a=float(a)
                                    if A>=1000 or B>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="" or B=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0 or B<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0

                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    if int(B)==float(B):
                                        B=int(B)
                                    if int(a)==float(a):
                                        a=int(a)

                                    
                                    ugl=math.radians(a)
                                    cos=math.cos(ugl)
                                    scobka=A*A+B*B-2*A*B*cos
                                    scobka=round(scobka,5)
                                    txt_2=" d = √(" + str(scobka)+ ")\n"
                                    d=scobka**0.5
                                    d=round(d,5)
                                    txt_3=" d = "+str(d)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                def pryamoug():
                    head=Label(text="Что нужно найти",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    head.place(x=290,y=10)
                    btn_1=Button(text="Сторону A",command=lambda:next("pryamoug_A"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_2=Button(text="Площадь S",command=lambda:next("pryamoug_S"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_3=Button(text="Диагональ D",command=lambda:next("pryamoug_D"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_1.place(x=120,y=110,width=310,height=190)
                    btn_2.place(x=470,y=110,width=310,height=190)
                    btn_3.place(x=120,y=350,width=650,height=190)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)  
                    def next(x):
                        head.destroy()
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        btn_back.destroy()
                        if x=="pryamoug_A":
                            pryamoug_A()
                        elif x=="pryamoug_S":
                            pryamoug_S()
                        elif x=="pryamoug_D":
                            pryamoug_D()
                    def back():
                        head.destroy()
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        btn_back.destroy()
                        ugolnik_4()


                    def pryamoug_A():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Диагональ D\nи вторую сторону",command=lambda:next("A_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_2=Button(text="Периметр P\nи вторую сторону",command=lambda:next("A_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_3=Button(text="Площадь S\nи вторую сторону",command=lambda:next("A_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="A_1":
                                A_1()
                            elif x=="A_2":
                                A_2()
                            elif x=="A_3":
                                A_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            pryamoug()

                        def A_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                pryamoug_A()
                            def find():
                                D=ent_1.get()
                                B=ent_2.get()
                                txt_1="  A = √(D\N{SUPERSCRIPT TWO} - B\N{SUPERSCRIPT TWO})\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    B=float(B)
                                    if D>=1000 or B>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if D=="" or B=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if D<=0 or B<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(D)==float(D):
                                        D=int(D)
                                    if int(B)==float(B):
                                        B=int(B)
                                    txt_2="  A = √("+str(D)+"\N{SUPERSCRIPT TWO} - "+str(B)+"\N{SUPERSCRIPT TWO})\n"
                                    A=D*D-B*B
                                    A=pow(A,0.5)
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def A_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Периметр P ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                pryamoug_A()
                            def find():
                                P=ent_1.get()
                                B=ent_2.get()
                                txt_1="  A = P/2 - B \n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    P=float(P)
                                    B=float(B)
                                    if P>=1000 or B>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if P=="" or B=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if P<=0 or B<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                    if B*2>=P:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введены некоректные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(P)==float(P):
                                        P=int(P)
                                    if int(B)==float(B):
                                        B=int(B)
                                    txt_2="  A = "+str(P)+" / 2 - "+str(B)+"\n"
                                    A=P/2-B
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def A_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Площадь S ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Сторона B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                pryamoug_A()
                            def find():
                                S=ent_1.get()
                                B=ent_2.get()
                                txt_1="  A = S / B \n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    S=float(S)
                                    B=float(B)
                                    if S>=1000 or B>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if S=="" or B=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if S<=0 or B<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(S)==float(S):
                                        S=int(S)
                                    if int(B)==float(B):
                                        B=int(B)
                                    txt_2="  A = "+str(S)+" / "+str(B)+"\n"
                                    A=S/B
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                    def pryamoug_S():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Две стороны",command=lambda:next("S_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_2=Button(text="Диагональ\nи меньший угол\nмежду диагоналями",command=lambda:next("S_2"),fg="#f67300",bg="#362b2b",font=("Calibri",22,"bold"))
                        _btn_3=Button(text="Периметр и\nодну сторону",command=lambda:next("S_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_4=Button(text="Диагональ и\nодну сторону",command=lambda:next("S_4"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_1.place(x=90,y=110,width=310,height=190)
                        _btn_2.place(x=490,y=110,width=310,height=190)
                        _btn_3.place(x=90,y=350,width=310,height=190)
                        _btn_4.place(x=490,y=350,width=310,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="S_1":
                                S_1()
                            elif x=="S_2":
                                S_2()
                            elif x=="S_3":
                                S_3()
                            elif x=="S_4":
                                S_4()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            pryamoug()

                        def S_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Сторона B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                pryamoug_S()
                            def find():
                                A=ent_1.get()
                                B=ent_2.get()
                                txt_1="  S = A * B\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    B=float(B)
                                    if A>=1000 or B>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="" or B=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0 or B<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    if int(B)==float(B):
                                        B=int(B)
                                    txt_2="  S = "+str(A)+" * "+str(B)+"\n"
                                    S = A * B 
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                        def S_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="    Угол α     ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                pryamoug_S()
                            def find():
                                D=ent_1.get()
                                a=ent_2.get()
                                txt_1="  S = D\N{SUPERSCRIPT TWO} * sin(α) / 2\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    a=float(a)
                                    if a>=180 or D>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if a=="" or D=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if a<=0 or D<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(a)==float(a):
                                        a=int(a)
                                    if int(D)==float(D):
                                        D=int(D)
                                    txt_2="  S = "+str(D)+"\N{SUPERSCRIPT TWO} * sin("+str(a)+") / 2\n"
                                    ugl=math.radians(a)
                                    sin=math.sin(ugl)
                                    S = D*D*sin/2
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def S_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Периметр P ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                pryamoug_S()
                            def find():
                                P=ent_1.get()
                                B=ent_2.get()
                                txt_1="  S = A * B\n  S = (P/2 - B) * B\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    P=float(P)
                                    B=float(B)
                                    if B>=1000 or P>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if B=="" or P=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if B<=0 or P<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                    if B*2>=P:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введены некоректные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(B)==float(B):
                                        B=int(B)
                                    if int(P)==float(P):
                                        P=int(P)
                                    txt_2="  S = ("+str(P)+"/2 -"+str(B)+") * "+str(B)+"\n"
                                    A = P/2-B
                                    S = A*B
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def S_4():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                pryamoug_S()
                            def find():
                                D=ent_1.get()
                                B=ent_2.get()
                                txt_1="  S = A * B\n  S = √(D\N{SUPERSCRIPT TWO}-B\N{SUPERSCRIPT TWO}) * B\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    B=float(B)
                                    if B>=1000 or D>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if B=="" or D=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if B<=0 or D<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                    if D<=B:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введены некоректные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(B)==float(B):
                                        B=int(B)
                                    if int(D)==float(D):
                                        D=int(D)
                                    txt_2="  S = √("+str(D)+"\N{SUPERSCRIPT TWO} - "+str(B)+"\N{SUPERSCRIPT TWO}) * "+str(B)+"\n"
                                    A = D*D-B*B
                                    A = pow(A,0.5)
                                    S = A*B
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                    def pryamoug_D():
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        head.destroy()
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Две стороны",command=lambda:next("D_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_2=Button(text="Площадь и\nменьший угол\nмежду диагоналями",command=lambda:next("D_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_3=Button(text="Площадь и\nодна сторона",command=lambda:next("D_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="D_1":
                                D_1()
                            elif x=="D_2":
                                D_2()
                            elif x=="D_3":
                                D_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            pryamoug()

                        def D_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Сторона A  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                pryamoug_D()
                            def find():
                                A=ent_1.get()
                                B=ent_2.get()
                                txt_1="  D = √(A\N{SUPERSCRIPT TWO} + B\N{SUPERSCRIPT TWO})\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    B=float(B)
                                    if A>=1000 or B>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="" or B=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0 or B<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    if int(B)==float(B):
                                        B=int(B)
                                    txt_2="  D = √("+str(A)+"\N{SUPERSCRIPT TWO} + "+str(B)+"\N{SUPERSCRIPT TWO})\n"
                                    D=A*A+B*B
                                    D=pow(D,0.5)
                                    D=round(D,5)
                                    txt_3="  D = "+str(D)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def D_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Площадь S  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="    Угол α   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                pryamoug_D()
                            def find():
                                S=ent_1.get()
                                a=ent_2.get()
                                txt_1="  D = √(2*S / sin(α))\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    S=float(S)
                                    a=float(a)
                                    if S>=1000 or a>=90:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if S=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if S<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(S)==float(S):
                                        S=int(S)
                                    if int(a)==float(a):
                                        a=int(a)
                                    txt_2="  D = √(2 * "+str(S)+" / sin("+str(a)+")\n"
                                    ugl=math.radians(a)
                                    sin=math.sin(ugl)
                                    D=2*S/sin
                                    D=pow(D,0.5)
                                    D=round(D,5)
                                    txt_3="  D = "+str(D)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                        def D_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Сторона B  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Площадь S  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                pryamoug_D()
                            def find():
                                B=ent_1.get()
                                S=ent_2.get()
                                txt_1="  D = √(A\N{SUPERSCRIPT TWO} + B\N{SUPERSCRIPT TWO})\n  D = √(S\N{SUPERSCRIPT TWO} / B\N{SUPERSCRIPT TWO} + B\N{SUPERSCRIPT TWO})\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    B=float(B)
                                    S=float(S)
                                    if B>=1000 or S>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if B=="" or S=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if B<=0 or S<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(B)==float(B):
                                        B=int(B)
                                    if int(S)==float(S):
                                        S=int(S)
                                    txt_2="  D = √("+str(S)+"\N{SUPERSCRIPT TWO} / "+str(B)+"\N{SUPERSCRIPT TWO} + "+str(B)+"\N{SUPERSCRIPT TWO})\n"
                                    A=S/B
                                    D=A*A+B*B
                                    D=pow(D,0.5)
                                    D=round(D,5)
                                    txt_3="  D = "+str(D)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                def kvadr():
                    head=Label(text="Что нужно найти",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    head.place(x=290,y=10)
                    btn_1=Button(text="Сторону A",command=lambda:next("kvadr_A"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_2=Button(text="Площадь S",command=lambda:next("kvadr_S"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_3=Button(text="Диагональ D",command=lambda:next("kvadr_D"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_1.place(x=120,y=110,width=310,height=190)
                    btn_2.place(x=470,y=110,width=310,height=190)
                    btn_3.place(x=120,y=350,width=650,height=190)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)  
                    def next(x):
                        head.destroy()
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        btn_back.destroy()
                        if x=="kvadr_A":
                            kvadr_A()
                        elif x=="kvadr_S":
                            kvadr_S()
                        elif x=="kvadr_D":
                            kvadr_D()
                    def back():
                        head.destroy()
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        btn_back.destroy()
                        ugolnik_4()

                    def kvadr_A():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Площадь S",command=lambda:next("A_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_2=Button(text="Диагональ D",command=lambda:next("A_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_3=Button(text="Периметр P",command=lambda:next("A_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="A_1":
                                A_1()
                            elif x=="A_2":
                                A_2()
                            elif x=="A_3":
                                A_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            kvadr()

                        def A_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Площадь S  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_txt_1.destroy()
                                kvadr_A()
                            def find():
                                S=ent_1.get()
                                txt_1="  A = √(S)\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    S=float(S)
                                    if S>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if S=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if S<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(S)==float(S):
                                        S=int(S)
                                    txt_2="  A = √"+str(S)+"\n"
                                    A=pow(S,0.5)
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                        def A_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_txt_1.destroy()
                                kvadr_A()

                            def find():
                                D=ent_1.get()
                                txt_1="  A = D / √(2)\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    if D>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if D=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if D<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(D)==float(D):
                                        D=int(D)
                                    txt_2="  A = "+str(D)+" / √2\n"
                                    A=D/pow(2,0.5)
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def A_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Периметр P ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_txt_1.destroy()
                                kvadr_A()

                            def find():
                                P=ent_1.get()
                                txt_1="  A = P / 4\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    P=float(P)
                                    if P>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if P=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if P<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(P)==float(P):
                                        P=int(P)
                                    txt_2="  A = "+str(P)+" / 4\n"
                                    A=P/4
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                    def kvadr_S():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Сторона A",command=lambda:next("S_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_2=Button(text="Диагональ D",command=lambda:next("S_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_3=Button(text="Периметр P",command=lambda:next("S_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="S_1":
                                S_1()
                            elif x=="S_2":
                                S_2()
                            elif x=="S_3":
                                S_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            kvadr()

                        def S_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Сторона A  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_txt_1.destroy()
                                kvadr_S()
                            def find():
                                A=ent_1.get()
                                txt_1="  S = A\N{SUPERSCRIPT TWO}\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    if A>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    txt_2="  S = "+str(A)+"\N{SUPERSCRIPT TWO}\n"
                                    S=A*A
                                    S=round(S,5)                                    
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                        def S_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Диагональ D  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_txt_1.destroy()
                                kvadr_S()
                            def find():
                                D=ent_1.get()
                                txt_1="  S = D\N{SUPERSCRIPT TWO} / 2\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    if D>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if D=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if D<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(D)==float(D):
                                        D=int(D)
                                    txt_2="  S = "+str(D)+"\N{SUPERSCRIPT TWO}"+" / 2\n"
                                    S=D*D/2
                                    S=round(S,5)                                    
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def S_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Периметр P  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_txt_1.destroy()
                                kvadr_S()
                            def find():
                                P=ent_1.get()
                                txt_1="  S = P\N{SUPERSCRIPT TWO} / 16\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    P=float(P)
                                    if P>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if P=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if P<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(P)==float(P):
                                        P=int(P)
                                    txt_2="  S = "+str(P)+"\N{SUPERSCRIPT TWO}"+" / 16\n"
                                    S=P*P/16
                                    S=round(S,5)                                    
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                    def kvadr_D():
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        head.destroy()
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Сторона A",command=lambda:next("D_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_2=Button(text="Площадь S",command=lambda:next("D_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_3=Button(text="Периметр P",command=lambda:next("D_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="D_1":
                                D_1()
                            elif x=="D_2":
                                D_2()
                            elif x=="D_3":
                                D_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            kvadr()

                        def D_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Сторона A  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_txt_1.destroy()
                                kvadr_D()
                            def find():
                                A=ent_1.get()
                                txt_1="  D = A * √(2)\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    if A>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    txt_2="  D = "+str(A)+" * √2\n"
                                    S=A*pow(2,0.5)
                                    S=round(S,5)                                    
                                    txt_3="  D = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def D_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Площадь S  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_txt_1.destroy()
                                kvadr_D()
                            def find():
                                S=ent_1.get()
                                txt_1="  A = √(2 * S)\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    S=float(S)
                                    if S>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if S=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if S<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(S)==float(S):
                                        S=int(S)
                                    txt_2="  D = √(2 *"+str(S)+")\n"
                                    D=pow(2*S,0.5)
                                    D=round(D,5)
                                    txt_3="  D = "+str(D)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                        def D_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="  Периметр P  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_txt_1.destroy()
                                kvadr_D()
                            def find():
                                P=ent_1.get()
                                txt_1="  D = √(2) * P / 4\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    P=float(P)
                                    if P>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if P=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if P<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(P)==float(P):
                                        P=int(P)
                                    txt_2="  D = √(2) * "+str(P)+" / 4\n"
                                    D=P*pow(2,0.5)/4
                                    D=round(D,5)                                    
                                    txt_3="  D = "+str(D)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                def trapec():
                    head=Label(text="Что нужно найти",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                    head.place(x=290,y=10)
                    btn_1=Button(text="Основание A",command=lambda:next("trapec_A"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_2=Button(text="Площадь S",command=lambda:next("trapec_S"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_3=Button(text="Диагональ D",command=lambda:next("trapec_D"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                    btn_1.place(x=120,y=110,width=310,height=190)
                    btn_2.place(x=470,y=110,width=310,height=190)
                    btn_3.place(x=120,y=350,width=650,height=190)
                    btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                    btn_back.place(x=5,y=5)  
                    def next(x):
                        head.destroy()
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        btn_back.destroy()
                        if x=="trapec_A":
                            trapec_A()
                        elif x=="trapec_S":
                            trapec_S()
                        elif x=="trapec_D":
                            trapec_D()
                    def back():
                        head.destroy()
                        btn_1.destroy()
                        btn_2.destroy()
                        btn_3.destroy()
                        btn_back.destroy()
                        ugolnik_4()

                    def trapec_A():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Средняя линия и\nвторое основание",command=lambda:next("A_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_2=Button(text="Площадь,\nвысота и\nвторое основание",command=lambda:next("A_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_3=Button(text="Высота,вторая сторона\nуглы при искомом основании",command=lambda:next("A_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="A_1":
                                A_1()
                            elif x=="A_2":
                                A_2()
                            elif x=="A_3":
                                A_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            trapec()

                        def A_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Ср. линия K ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Основание B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_P_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=200)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=155)
                            ent_1.place(x=50,y=215,width=150,height=45)
                            lbl_2.place(x=40,y=355)
                            ent_2.place(x=50,y=420,width=150,height=45)
                            btn_P_find.place(x=255,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_P_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                trapec_A()
                            def find():
                                K=ent_1.get()
                                B=ent_2.get()
                                txt_1="  A = 2*K - B\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    K=float(K)
                                    B=float(B)
                                    if K>=1000 or B>=10000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if K=="" or B=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if K<=0 or B<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                    if 2*K-B<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введены некоректные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(K)==float(K):
                                        K=int(K)
                                    if int(B)==float(B):
                                        B=int(B)
                                    txt_2="  A = 2 * "+str(K)+" - "+str(B)+"\n"
                                    A=2*K-B
                                    A=round(A,6)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def A_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Площадь S ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Высота H ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text=" Основание B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",25,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                trapec_A()
                            def find():
                                S=ent_1.get()
                                H=ent_2.get()
                                B=ent_3.get()
                                txt_1="  A = 2*k - B\n  A = 2*S/h - B\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    S=float(S)
                                    B=float(B)
                                    H=float(H)
                                    if S>=1000 or B>=1000 or H>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if S=="" or B=="" or H=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if S<=0 or B<=0 or H<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                    if 2*S/H - B <=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введены некоректные значения")
                                        error=1
                                        err=2/0

                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(S)==float(S):
                                        S=int(S)
                                    if int(B)==float(B):
                                        B=int(B)
                                    if int(H)==float(H):
                                        H=int(H)
                                    txt_2="  A = 2*"+str(S)+" / "+str(H)+" - "+str(B)+"\n"
                                    A=2*S/H-B
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                        def A_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text="Основание B",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Высота H  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="     Угол α     ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_4=Label(text="     Угол β     ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_4=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",26,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=90)
                            ent_1.place(x=55,y=145,width=150,height=45)
                            lbl_2.place(x=40,y=215)
                            ent_2.place(x=50,y=270,width=150,height=45)
                            lbl_3.place(x=40,y=340)
                            ent_3.place(x=50,y=395,width=150,height=45)
                            lbl_4.place(x=40,y=465)
                            ent_4.place(x=50,y=520,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_4.destroy()
                                ent_4.destroy()
                                lbl_txt_1.destroy()
                                trapec_A()
                            def find():
                                B=ent_1.get()
                                H=ent_2.get()
                                a=ent_3.get()
                                b=ent_3.get()
                                txt_1="  A = B + H*(ctg(α) + ctg(β))\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    a=float(a)
                                    b=float(b)
                                    B=float(B)
                                    H=float(H)
                                    if a>=180 or b>=180 or B>=1000 or H>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if a=="" or b=="" or B=="" or H=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if a<=0 or b<=0 or B<=0 or H<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0

                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(a)==float(a):
                                        a=int(a)
                                    if int(b)==float(b):
                                        b=int(b)
                                    if int(B)==float(B):
                                        B=int(B)
                                    if int(H)==float(H):
                                        H=int(H)

                                    ugl_1=math.radians(a)
                                    tg_1=math.tan(ugl_1)
                                    ctg_1=1/tg_1

                                    ugl_2=math.radians(b)
                                    tg_2=math.tan(ugl_2)
                                    ctg_2=1/tg_2

                                    txt_2="  A = "+str(B)+" + "+str(H)+"*( "+str(round((ctg_1+ctg_2),4))+" )\n"
                                    A=B + H*(ctg_1+ctg_2)
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                        

                    def trapec_S():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Две стороны\nи высота",command=lambda:next("S_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_2=Button(text="Средняя линия\nи высота",command=lambda:next("S_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_3=Button(text="Две диагонали и любой угол,\nобразованный пересечением диагоналей",command=lambda:next("S_3"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="S_1":
                                S_1()
                            elif x=="S_2":
                                S_2()
                            elif x=="S_3":
                                S_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            trapec()


                        def S_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Сторона B ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="  Высота H  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",25,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                trapec_S()
                            def find():
                                A=ent_1.get()
                                B=ent_2.get()
                                H=ent_3.get()
                                txt_1="  S = H * (A + B) / 2\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    B=float(B)
                                    H=float(H)
                                    if A>=1000 or B>=1000 or H>=1000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="" or B=="" or H=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0 or B<=0 or H<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0


                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    if int(B)==float(B):
                                        B=int(B)
                                    if int(H)==float(H):
                                        H=int(H)
                                    txt_2="  S = "+str(H)+" * ("+str(A)+" + "+str(B)+") / 2\n"
                                    S=H * (A+B) / 2
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                        def S_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Ср. линия K ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Высота H ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",27,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=200)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=155)
                            ent_1.place(x=50,y=215,width=150,height=45)
                            lbl_2.place(x=40,y=355)
                            ent_2.place(x=50,y=420,width=150,height=45)
                            btn_find.place(x=255,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_txt_1.destroy()
                                trapec_S()
                            def find():
                                K=ent_1.get()
                                H=ent_2.get()
                                txt_1="  S = K * H\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    K=float(K)
                                    H=float(H)
                                    if K>=1000 or H>=10000:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if K=="" or H=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if K<=0 or H<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(K)==float(K):
                                        K=int(K)
                                    if int(H)==float(H):
                                        H=int(H)
                                    txt_2="  S = "+str(K)+" * "+str(H)+"\n"
                                    A=K*H
                                    A=round(A,5)
                                    txt_3="  A = "+str(A)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                        def S_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Диагональ D ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text=" Диагональ d ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="     Угол α    ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",25,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                trapec_S()
                            def find():
                                D=ent_1.get()
                                d=ent_2.get()
                                a=ent_3.get()
                                txt_1="  S = D * d * sin(α) / 2\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    D=float(D)
                                    d=float(d)
                                    a=float(a)
                                    if D>=1000 or d>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if D=="" or d=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if D<=0 or d<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(D)==float(D):
                                        D=int(D)
                                    if int(d)==float(d):
                                        d=int(d)
                                    if int(a)==float(a):
                                        a=int(a)
                                    txt_2="  S = "+str(D)+" * "+str(d)+" * sin("+str(a)+") / 2\n"
                                    ugl=math.radians(a)
                                    sin=math.sin(ugl)
                                    S=D*d*sin/ 2
                                    S=round(S,5)
                                    txt_3="  S = "+str(S)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)



                    def trapec_D():
                        _head=Label(text="Что вам известно",font="Calibri 31 bold",justify="center",bg="#362b2b",fg="#f67300")
                        _head.place(x=290,y=10)
                        _btn_1=Button(text="Площадь,\nвторая диагональ\nи угол между\nдиагоналями",command=lambda:next("D_1"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_2=Button(text="Высота,\nсторона и угол\nпри этой стороне,\nсмотрящий\nна диагональ",command=lambda:next("D_2"),fg="#f67300",bg="#362b2b",font=("Calibri",24,"bold"))
                        _btn_3=Button(text="Вторая диагональ, сторона\n и угол при этой стороне,\n смотрящий на искомую диагональ",command=lambda:next("D_3"),fg="#f67300",bg="#362b2b",font=("Calibri",23,"bold"))
                        _btn_1.place(x=120,y=110,width=310,height=190)
                        _btn_2.place(x=470,y=110,width=310,height=190)
                        _btn_3.place(x=120,y=350,width=650,height=190)
                        btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                        btn_back.place(x=5,y=5)  
                        def next(x):
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            if x=="D_1":
                                D_1()
                            elif x=="D_2":
                                D_2()
                            elif x=="D_3":
                                D_3()
                        def back():
                            _head.destroy()
                            _btn_1.destroy()
                            _btn_2.destroy()
                            _btn_3.destroy()
                            btn_back.destroy()
                            trapec()

                        def D_1():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Площадь S ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="Диагональ d",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="   Угол α   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",25,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                trapec_D()
                            def find():
                                S=ent_1.get()
                                d=ent_2.get()
                                a=ent_3.get()
                                txt_1="  D = (2 * S) / (d * sin(α))\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    S=float(S)
                                    d=float(d)
                                    a=float(a)
                                    if S>=1000 or d>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if S=="" or d=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if S<=0 or d<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0


                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(d)==float(d):
                                        d=int(d)
                                    if int(S)==float(S):
                                        S=int(S)
                                    if int(a)==float(a):
                                        a=int(a)
                                    ugl=math.radians(a)
                                    sin=math.sin(ugl)
                                    scobka_1=2*S
                                    scobka_2=d*sin
                                    scobka_1=round(scobka_1,5)
                                    scobka_2=round(scobka_2,5)
                                    txt_2="  D = "+str(scobka_1)+" / "+str(scobka_2)+"\n"
                                    D=scobka_1/scobka_2
                                    D=round(D,5)
                                    txt_3="  D = "+str(D)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)


                        def D_2():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="  Высота H  ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="   Угол α   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",25,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                trapec_D()
                            def find():
                                A=ent_1.get()
                                H=ent_2.get()
                                a=ent_3.get()
                                txt_1="  D = √(H\N{SUPERSCRIPT TWO} + (A - H*ctg(α))\N{SUPERSCRIPT TWO})\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    H=float(H)
                                    a=float(a)
                                    if A>=1000 or H>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="" or H=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0 or H<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0


                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    if int(H)==float(H):
                                        H=int(H)
                                    if int(a)==float(a):
                                        a=int(a)
                                    ugl=math.radians(a)
                                    tg=math.tan(ugl)
                                    ctg=1/tg
                                    scobka=H*H+(A-H*ctg)**2
                                    scobka=round(scobka,5)
                                    txt_2="  D = √( "+str(scobka)+" )\n"
                                    D=scobka**0.5
                                    D=round(D,5)
                                    txt_3="  D = "+str(D)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

                        def D_3():
                            head=Label(text="Введите значения",font="Calibri 30 bold",justify="center",bg="#362b2b",fg="#f67300")
                            head.place(x=310,y=10)
                            lbl_1=Label(text=" Сторона A ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_2=Label(text="Диагональ d",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            lbl_3=Label(text="   Угол α   ",font=("Calibri",26,"bold"),bg="#f67300",fg="#362b2b")
                            ent_1=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_2=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            ent_3=Entry(font=("Calibri",26,"bold"),bg="white",fg="black")
                            btn_find=Button(text="Найти",font="Calibri 28 bold",justify="center",bg="#362b2b",fg="#f67300",command=lambda:find())
                            bg=Label(bg="#463b3b",font=("Calibri",26,"bold"),fg="#362b2b")
                            lbl_txt_1=Label(text="",font=("Calibri",25,"bold"),bg="#463b3b",fg="#f87808",justify="left")
                            lbl_txt_1.place(x=427,y=150)
                            bg.place(x=425,y=90,width=450,height=470)
                            lbl_1.place(x=40,y=130)
                            ent_1.place(x=55,y=185,width=150,height=45)
                            lbl_2.place(x=40,y=280)
                            ent_2.place(x=50,y=345,width=150,height=45)
                            lbl_3.place(x=40,y=430)
                            ent_3.place(x=50,y=495,width=150,height=45)
                            btn_find.place(x=260,y=265,height=70)
                            btn_back=Button(text="Назад",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:back())
                            btn_back.place(x=5,y=5)
                            def back():
                                btn_back.destroy()
                                head.destroy()
                                bg.destroy()
                                btn_find.destroy()
                                lbl_1.destroy()
                                ent_1.destroy()
                                lbl_2.destroy()
                                ent_2.destroy()
                                lbl_3.destroy()
                                ent_3.destroy()
                                lbl_txt_1.destroy()
                                trapec_D()
                            def find():
                                A=ent_1.get()
                                d=ent_2.get()
                                a=ent_3.get()
                                txt_1="  D = √(A\N{SUPERSCRIPT TWO} + d\N{SUPERSCRIPT TWO} - 2*A*d*cos(α))\n\n"
                                error=0
                                lbl_txt_1.configure(text=txt_1)
                                try:
                                    A=float(A)
                                    d=float(d)
                                    a=float(a)
                                    if A>=1000 or d>=1000 or a>=180:
                                        messagebox.showinfo("Ошибка","Слишком большие значения  ")
                                        error=1
                                        err=2/0
                                    if A=="" or d=="" or a=="":
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите все значения")
                                        error=1
                                        err=2/0
                                    if A<=0 or d<=0 or a<=0:
                                        if error==0:
                                            messagebox.showinfo("Ошибка","Введите положительные значения")
                                        error=1
                                        err=2/0
                                except:
                                    if error==0:
                                        messagebox.showinfo("Ошибка","Введите числовые значения\nДля ввода нецелой части используйте точку")
                                else:
                                    if int(A)==float(A):
                                        A=int(A)
                                    if int(d)==float(d):
                                        d=int(d)
                                    if int(a)==float(a):
                                        a=int(a)
                                    ugl=math.radians(a)
                                    cos=math.cos(ugl)
                                    scobka=A*A+d*d-2*A*d*cos
                                    scobka=round(scobka,5)
                                    txt_2="  D = √( "+str(scobka)+" )\n"
                                    D=scobka**0.5
                                    D=round(D,5)
                                    txt_3="  D = "+str(D)
                                    txt=txt_1+txt_2+txt_3
                                    lbl_txt_1.configure(text=txt)

first_build()
window.mainloop()
"""α β γ π √"""