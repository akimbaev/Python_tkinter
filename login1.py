from tkinter import *
import sqlite3
import tkinter.messagebox

from PIL import ImageTk, Image
def open_dialog():
    window=Tk()
    window.geometry("500x350")
    window.title("User Registration Form")
    window.resizable(False, False)

    usr=StringVar()
    ln=StringVar()
    ps=StringVar()
    DOB=StringVar()
    num=StringVar()
    cit=StringVar()
    c1=StringVar()


    def printt():
        tkinter.messagebox.showinfo("Success", "Successfully Registered!")
        window.destroy()


    def exitt():
        window.destroy()



    def database():
        username=usr.get()
        password=ps.get()
        name=ln.get()
        date=DOB.get()
        sex=c1.get()
        contact=num.get()
        city1=cit.get()
        conn=sqlite3.connect("Form.db")
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Student(username TEXT,password TEXT,name TEXT,DOB TEXT,Gender TEXT,Contact TEXT,City TEXT)')
        cursor.execute('INSERT INTO Student(username,password,name,DOB,Gender,Contact,City) VALUES (?,?,?,?,?,?,?)' , (username,password,name,date,sex,contact,city1),)
        conn.commit()


    #HEADER
    Tops = Frame(window,bg="white",width = 1600,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = Frame(window,width = 900,height=700,relief=SUNKEN)
    f1.pack(side=LEFT)

    f2 = Frame(window ,width = 400,height=700,relief=SUNKEN)
    f2.pack(side=RIGHT)
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Registration",fg="black",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)
    #ENTRYFIELD FOR Username
    label1=Label(f1,text="Username")
    label1.grid(row=0, column=0)
    field1=Entry(f1,textvar=usr)
    field1.grid(row=0,column=1)
    #ENTRYFIELD FOR Password
    label2=Label(f1,text="Password")
    label2.grid(row=1,column=0)   
    field2=Entry(f1,show="*")
    field2.grid(row=1,column=1)
    # #ENTRYFIELD FOR NAME
    label3=Label(f1,text="Name")
    label3.grid(row=2,column=0)
    field3=Entry(f1,textvar=ln)
    field3.grid(row=2,column=1)
    # #ENTRY FIELD FOR  DOB
    label4=Label(f1,text="Date of Birth : \n (DD/MM/YYYY) ")
    label4.grid(row=3,column=0)
    field4=Entry(f1,textvar=DOB)
    field4.grid(row=3,column=1)
    # #ENTRYFIELD FOR CITY
    label5=Label(f1,text="City : ")
    label5.grid(row=4,column=0)
    variable = StringVar(window)

    CITIES = [ 
        "Hof",
        "Munich",
        "Nurnberg",
        "Bamberg"
        ]        
    variable.set(CITIES[0]) # default value
    

    field5 = OptionMenu(f1, variable, *CITIES)
    field5.grid(row=4,column=1)
    
    
    #ENTRY FIELD FOR GENDER
    gender=Label(f1,text="Gender: ", font=("Arial",14))
    gender.grid(row=5,column=0)
    c1=StringVar()
    ch1=Radiobutton(f1,text="Male", variable=c1, value=" ").grid(row=5, column=1, sticky="W")
    ch2=Radiobutton(f1, text="Female", variable=c1, value=" ").grid(row=5, column=2, sticky="W")
    ch3=Radiobutton(f1, text="Others", variable=c1, value="").grid(row=5, column=3, sticky="W")
    #ENTRYFIELD FOR CONTACT NO.
    cont=Label(f1,text="Contact No.:", font=("Arial",14))
    cont.grid(row=6,column=0)
    field6=Entry(f1,textvar=num)
    field6.grid(row=6,column=1)

    #BUTTONS
    but1 = Button(window,text="SignUp", width=20, height=2, font=("Arial", 12), command=lambda: [printt(), database()])
    but1.place(x=330, y=120)
    window.bind("<Return>", database)
    but2=Button(window,text="Exit", width=20, height=2, font=("Arial",12), command=exitt)
    but2.place(x=330, y=170)

    window.mainloop()



if __name__ == "__main__":
    open_dialog()


def change():
    print("running change")
