from tkinter import*
import random
import time
#from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import mysql.connector


root = Tk()
root.geometry("1600x800+0+0")
root.title("Tech Dhaba Management System")



Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops,font=("Times" ,30,"bold"),text="Tech Dhaba Management System",fg="crimson",
                bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=("Times",30,"bold"),text=localtime,fg="black",anchor=W,)
lblinfo.grid(row=1,column=0)

#---------------Calculator------------------
text_Input=StringVar()
operator =""



def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=eval(operator)

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger +
                              costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service=str('%.2f'% Ser_Charge)
    OverAllCost=str( PayTax + Totalcost + Ser_Charge)
    PaidTax=str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)
    
    mydb = mysql.connector.connect(host="localhost", user="root", password="abhay", database="pp")
    mycursor = mydb.cursor()
    insert = ("INSERT INTO  bils(orde,fries,lunch,burger,pizza,cheese,drinks,cost,servicecharge,tax,subtotal,total)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    values = [rand.get(),Fries.get(),Largefries.get(),Burger.get(),Filet.get(),Cheese_burger.get(),(Drinks.get())
              ,cost.get(),Service_Charge.get(),Tax.get(),Subtotal.get(),Total.get()]
    mycursor.execute(insert,values)
    print(values)
    mydb.commit()
    messagebox.showinfo("Notification","Your order is received")

rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Cheese_burger = StringVar()
Drinks = StringVar()
cost = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Subtotal = StringVar()
Total = StringVar()

def qexit():
    qexit = tmsg.askyesno("Tech Foodies Management System","Are you sure you want to Exit")
    yes = root.destroy()   
    

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")
#====================================Calculator===================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator=""

txtDispaly = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input, bd=30, insertwidth=4,
                  bg='powder blue',justify='right')
txtDispaly.grid(columnspan=4)


btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='7',bg='powder blue', command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='8',bg='powder blue', command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='9',bg='powder blue', command=lambda: btnClick(9)).grid(row=2,column=2)


Addition=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='+',bg='powder blue', command=lambda: btnClick("+")).grid(row=2,column=3)
#-------------------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='4',bg='powder blue', command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='5',bg='powder blue', command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='6',bg='powder blue', command=lambda: btnClick(6)).grid(row=3,column=2)


Substration=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='-',bg='powder blue', command=lambda: btnClick("-")).grid(row=3,column=3)
#--------------------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='1',bg='powder blue', command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='2',bg='powder blue', command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='3',bg='powder blue', command=lambda: btnClick(3)).grid(row=4,column=2)


Multiply=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='*',bg='powder blue', command=lambda: btnClick("*")).grid(row=4,column=3)
#--------------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='0',bg='powder blue', command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='C',bg='powder blue',command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='=',bg='powder blue',command=btnEqualsInput).grid(row=5,column=2)


Division=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text='/',bg='powder blue', command=lambda: btnClick("/")).grid(row=5,column=3)



#---------------------------------------------------------------------------------------
lblreference = Label(f1,font=('arial',20,'bold'),text="Bill no.",bd=16,anchor='w')
lblreference.grid(row=0,column=0)
txtreference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=16,insertwidth=4,
                  bg='powder blue', justify = 'right')
txtreference.grid(row=0,column=1)
#=====================================================================================
lblfries = Label(f1,font=('arial',16,'bold'),       text="Fries                       Rs.25",bd=16,anchor='w')
lblfries.grid(row=1,column=0)
txtfries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=16,insertwidth=4,
                  bg='powder blue', justify = 'right')
txtfries.grid(row=1,column=1)
#=======================================================================================
lblLargefries = Label(f1,font=('arial',16,'bold'),       text="Large Fries             Rs.40",bd=16,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries=Entry(f1,font=('arial',16,'bold'),textvariable=Largefries,bd=16,insertwidth=4,
                  bg='powder blue', justify = 'right')
txtLargefries.grid(row=2,column=1)
#=======================================================================================

lblburger = Label(f1,font=('arial',16,'bold'),       text="Large Burger          Rs.35",bd=16,anchor='w')
lblburger.grid(row=3,column=0)
txtburger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=16,insertwidth=4,
                  bg='powder blue', justify = 'right')
txtburger.grid(row=3,column=1)
#============================================================================================

lblFilet = Label(f1,font=('arial',16,'bold'),         text="Aloo Tikki Burger    Rs.50",bd=16,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet=Entry(f1,font=('arial',16,'bold'),textvariable=Filet,bd=16,insertwidth=4,
                  bg='powder blue', justify = 'right')
txtFilet.grid(row=4,column=1)
#================================================================================================

#==================================================================================================
lblCheese_burger = Label(f1,font=('arial',16,'bold'), text="Cheese Buger         Rs.50",bd=16,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger=Entry(f1,font=('arial',16,'bold'),textvariable=Cheese_burger,bd=16,insertwidth=4,
                  bg='powder blue', justify = 'right')
txtCheese_burger.grid(row=5,column=1)
#===========================================Tech Foodies Info 2=====================================================
lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks              Rs.35",bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,
                  bg='#ffffff', justify = 'right')
txtDrinks.grid(row=0,column=3)
#==================================================================================================
lblcost = Label(f1,font=('arial',16,'bold'),text="Cost                          ",bd=16,anchor='w')
lblcost.grid(row=1,column=2)
txtcost=Entry(f1,font=('arial',16,'bold'),textvariable=cost,bd=10,insertwidth=4,
                  bg='#ffffff', justify = 'right')
txtcost.grid(row=1,column=3)
#=====================================================================================
lblService_Charge = Label(f1,font=('arial',16,'bold'),  text="Service Charge          ",bd=16,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,
                  bg='#ffffff', justify = 'right')
txtService_Charge.grid(row=2,column=3)
#=======================================================================================

lblTax = Label(f1,font=('arial',16,'bold'), text="Tax                            ",bd=16,anchor='w')
lblTax.grid(row=3,column=2)
txtTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,
                  bg='#ffffff', justify = 'right')
txtTax.grid(row=3,column=3)
#============================================================================================

lblSubtotal = Label(f1,font=('arial',16,'bold'),  text="Subtotal                   ",bd=16,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal=Entry(f1,font=('arial',16,'bold'),textvariable=Subtotal,bd=10,insertwidth=4,
                  bg='#ffffff', justify = 'right')
txtSubtotal.grid(row=4,column=3)
#================================================================================================
lblTotal = Label(f1,font=('arial',16,'bold'),  text="Total                         ",bd=16,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,
                  bg='#ffffff', justify = 'right')
txtTotal.grid(row=5,column=3)






#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Generate Bill No.",
                bg="yellow",command=Ref)
btnTotal.grid(row=7, column=0)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET",
                bg="yellow1",command=reset)
btnreset.grid(row=7, column=1)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT",
               bg="gold",command=qexit)
btnexit.grid(row=7, column=2)

btntotalamount=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Total Amount",
                bg="darkgoldenrod1",command = Ref )
btntotalamount.grid(row=7, column=3)


root.mainloop()
